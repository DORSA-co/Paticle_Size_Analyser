import logging
from typing import Callable, Union
import time
import threading

from opcua import Client
from opcua import ua
from opcua.common.node import Node
from PySide6.QtCore import QObject, Signal





class singleNodeHandler:
    
    def __init__(self, 
                 name:str,
                 node:Node, 
                 auto_read:bool=False, 
                 read_change_event:Callable=None,
                 read_refresh_time:int= 100,
                 auto_write:bool=False,
                 write_program:list[dict]=[], 
                 ) -> None:
       
        if auto_write:
            assert len(write_program), "auto write is enalble but no program given"
        

        self.name = name
        self.node = node

        self.auto_read = auto_read
        self.read_change_event = read_change_event
        self.read_refresh_time = read_refresh_time
        self.auto_write = auto_write
        self.write_program = write_program

        self.write_program_idx = 0
        self.auto_write_value = None
        self.write_timer = 0
        self.read_timer = 0

        try:
            self.__type = self.node.get_data_type_as_variant_type()
        except:
            self.__type = None
        #---------------------------------------------------------
        try:
            self.adress = self.node.nodeid.to_string()
        except:
            self.__type = None
        
    def set_auto_read(self, auto_read,  read_change_event=None):
        self.auto_read = auto_read

        if read_change_event is not None:
            self.read_change_event = read_change_event
    
    def change_node(self, node:Node):
        self.node = node
        try:
            self.__type = self.node.get_data_type_as_variant_type()
        except:
            self.__type = None

        try:
            self.adress = self.node.nodeid.to_string()
        except:
            self.__type = None

    def time_counter_read(self, t):
        self.read_timer += t

    def time_counter_write(self, t):
        self.write_timer += t

    def is_auto_read(self,):
        return self.auto_read
    
    def is_auto_write(self,):
        return self.auto_write
    
    

    def is_time_to_read(self,):
        if self.read_timer > self.read_refresh_time:
            self.read_timer = 0
            return True
        return False 
    
    def is_time_to_write(self,):
        if self.write_timer > self.write_program[self.write_program_idx]['time']:
            self.auto_write_value = self.write_program[self.write_program_idx]['value']
            self.write_program_idx += 1
            if self.write_program_idx >= len(self.write_program):
                self.write_program_idx = 0
            self.write_timer = 0
            return True
        return False

    def get_auto_write_value(self,):
        return self.auto_write_value
    
    def get_value(self,):
        return self.node.get_value()
    
    
    def get_name(self, ) -> str:
        return self.name
    
    def get_addres(self, ) -> str:
        return self.adress

    def set_value(self, value):
        data = self.make_data_value(value)
        self.node.set_data_value(data)
    
    def make_data_value(self, value):
        data = ua.DataValue(ua.Variant(value, self.__type))
        return data
    







class nodesHandler:

    def __init__(self, client:Client) -> None:
        self.names2node:dict[str, singleNodeHandler] = {}
        self.address2node:dict[str, singleNodeHandler] = {}
        self.client = client
        self.external_change_data_event = None

    def rebuild(self, client:Client):
        """this function update nodes base on change self.client
        """
        self.client = client

        for name in self.names2node.keys():
            node_handler = self.names2node[name]
            adrr = node_handler.get_addres()
            node = self.client.get_node(adrr)
            node_handler.change_node(node)

            self.address2node[name] = node_handler
            self.names2node[name] = node_handler


    def change_node_address(self, name:str, addr:str):
        node = self.client.get_node(addr)
        node_handler = self.get_by_name(name)
        node_handler.change_node(node)

            

    
    def get_by_name(self, name:str) -> singleNodeHandler:
        return self.names2node.get(name)
    
    def set_change_value_event(self, func:Callable):
        self.external_change_data_event  = func


    def define_node(self,
                    name:str,
                    address:Union[str, dict],
                    auto_read:bool=False, 
                    read_change_event:Callable=None,
                    read_refresh_time:int= 100,
                    auto_write:bool=False,
                    write_program:list[float, int]=[], 
                    ) -> None:
        
        if isinstance(address, dict):
            address = f"ns={address['ns']};i={address['i']}"

        node = self.client.get_node(address)
        snode_handler = singleNodeHandler(name, 
                                          node,
                                          auto_read=auto_read,
                                          auto_write=auto_write,
                                          read_change_event=read_change_event,
                                          read_refresh_time=read_refresh_time,
                                          write_program=write_program)
        self.names2node[name] = snode_handler
        self.address2node[address] = snode_handler

    def clear_all(self,):
        self.names2node:dict[str, singleNodeHandler] = {}
        self.address2node:dict[str, singleNodeHandler] = {}

    def get_names(self,) -> list[str]:
        return list(self.names2node.keys())


    def set_values(self, dict_values:dict ):
        nodes = []
        data_values = []
        for name, value in dict_values.items():
            snode_handler = self.get_by_name(name)
            if snode_handler is None:
                continue
            nodes.append(snode_handler.node)
            data_values.append( snode_handler.make_data_value(value) )

        try:
            self.client.set_values(nodes, data_values)
            return True
        except Exception as e:
            print('set_values:', e)
            return False

    
    def get_values(self, names:list) -> dict:
        nodes = []
        for name in names:
            snode_handler = self.get_by_name(name)
            if snode_handler is None:
                continue
            nodes.append(snode_handler.node)
        try:
            values = self.client.get_values(nodes)
            res = {}
            for i in range(len(names)):
                res[names[i]] = values[i]
            return res
        except:
            #plc not connect
            return None
    

    
    


    
       

        


    



class PLCHandler:
    log = 0

    def __init__(self, url:str) -> None:
        self.url = url
        self.client = None 

        self.write_thread = None
        self.write_worker = None

        self.read_thread = None
        self.read_worker = None

        self.connector_worker = None
        self.connector_thread = None

        self.__build_client()
        self.nodesHandler = nodesHandler(self.client)

        self.external_connected_event = None
        self.external_disconnected_event = None

        self.run_threads_after_connect = False
        self.__connect_flag = False

        self.__read_requests = {}


    def set_connected_event(self, func):
        self.external_connected_event = func
    
    def set_disconnected_event(self, func):
        self.external_disconnected_event = func
    
    def set_change_data_event(self, func):
        self.nodesHandler.set_change_value_event(func)

        
    def __build_client(self,):
        self.client = Client(self.url)

    def is_connect(self,) -> bool:
        return self.__connect_flag

    def connect(self, url=None):
        if url is not None:
            url = self.url
            self.__build_client()
            self.nodesHandler.rebuild(self.client)

        try:
            self.client.connect()
            return True
        except Exception as e:
            if self.log>0:
                print('PLC connect:', e)
            return False
        
    def connect_request(self, url=None, run_threads_after_connect=True):
        """the diffrence of this method and connect method is
           that this method run on thread
        """
        self.run_threads_after_connect = run_threads_after_connect
        if url is not None:
            self.url = url
            self.__build_client()

        if self.connector_thread is not None:
            if self.connector_thread.is_alive():
                self.connector_worker.stop()

        self.connector_worker = PLCConnectorWorker(self.client)
        self.connector_worker.plc_connected_signal.connect(self.__connected_event)
        self.connector_thread = threading.Thread( target= self.connector_worker.run)
        self.connector_thread.start()
    
    def __connected_event(self,):
        self.nodesHandler.rebuild(self.client)
        self.__connect_flag = True

        if self.run_threads_after_connect:
            self.run_threads()
        if self.external_connected_event:
            self.external_connected_event()
        

    def disconnect(self,):
        try:
            self.client.disconnect()
            return True
        except Exception as e:
            print('PLC disconnect', e)
            return False
        
    
    def __disconnect_event(self,):
        self.__connect_flag = False
        if self.log>1:
            print('PLC disconnected')
        self.kill_threads()
        self.connect_request()
        if self.external_disconnected_event:
            self.external_disconnected_event()

    def kill_threads(self,):
        if self.read_thread is not None:
            if self.read_thread.is_alive():
                self.read_worker.stop()

        
        if self.write_thread is not None:
            if self.write_thread.is_alive():
                self.write_worker.stop()
    
    def run_threads(self,):
        self.read_worker = PLCReadWoker(self.nodesHandler, loop_time=10)
        self.read_worker.change_value_signal.connect(self.__change_data_event)
        self.read_worker.disconnected_singal.connect(self.__disconnect_event)
        self.read_worker.request_value_signal.connect(self.__request_answer_event)
        self.read_thread = threading.Thread(target=self.read_worker.run)
        self.read_thread.start()

        self.write_worker = PLCWriteWorker(self.nodesHandler, loop_time=10)
        self.write_thread = threading.Thread(target=self.write_worker.run)
        self.write_thread.start()

    def send_read_request(self,request_id:str, node_names:list, answer_func:Callable):
        """get values on thread
        """
        if not self.read_thread.is_alive():
            if self.log > 0:
                print(f"ERROR: read request {request_id} send befor running_threads!")
            return
        
        self.__read_requests[request_id] = {
            'func': answer_func
        }

        self.read_worker.read_requests(request_id, node_names)

    def send_write_request(self, values:dict):
        """write node on thread

        Args:
            values (dict): dictionary that keys are node's name and it's values are node's value
        """
        if self.write_thread is None or not self.write_thread.is_alive():
            if self.log > 0:
                print(f"ERROR: write request send befor running_threads!")
            return
        
        self.write_worker.write_request(values)


    def __change_data_event(self, data:dict):
        name = data['name']
        single_node_handler = self.nodesHandler.get_by_name(name)
        if single_node_handler is None:
            return
        
        if single_node_handler.read_change_event is not None:
            single_node_handler.read_change_event(data)
        
        elif self.nodesHandler.external_change_data_event is not None:
            self.nodesHandler.external_change_data_event(data)

        else:
            if self.log > 1:
                print("WARNING: PLC node change but no event found for it", data)


    def __request_answer_event(self, req:dict):
        req_id = req['id']
        values = req['values']
        func = self.__read_requests[req_id]['func']
        self.__read_requests.pop(req_id)
        func(values )





class PLCConnectorWorker(QObject):
    plc_connected_signal = Signal()

    def __init__(self, client:Client) -> None:
        super().__init__()
        self.client = client
        self.__running = True

    def run(self,):
        while self.__running:
            try:
                self.client.connect()
                self.plc_connected_signal.emit()
                break
            except:
                pass
            time.sleep(0.5)

    def stop(self):
        self.__running = False






class PLCWriteWorker(QObject):
    data_received = Signal(str)

    def __init__(self, nodes_handler:nodesHandler, loop_time:int):
        super().__init__()
        self.loop_time = loop_time
        self.nodesHandler = nodes_handler
        self.writes_value = {}
        self.__running = True



    def write_request(self, writes_value:dict):
        for name, value in writes_value.items():
            self.writes_value[name] = value

    
    def hanle_auto_write_values(self,):
        for name in self.nodesHandler.get_names():
            snode_handler = self.nodesHandler.get_by_name(name)
            if snode_handler is None:
                continue

            #check if node is not auto write
            if not snode_handler.is_auto_write():
                continue

            #check if write request send handly
            if self.writes_value.get(name):
                continue

            snode_handler.time_counter_write(self.loop_time)
            if snode_handler.is_time_to_write():
                self.writes_value[name] = snode_handler.get_auto_write_value()

    
    def run(self):
        
        while self.__running:
            
            self.hanle_auto_write_values()


            if len(self.writes_value):
                ret = self.nodesHandler.set_values(self.writes_value)
                if ret:
                    self.writes_value = {}
                    

            #WARNING: don't hardcode self.loop_time
            time.sleep(self.loop_time / 1000)

    def stop(self,):
        self.__running=False



class PLCReadWoker(QObject):
    change_value_signal = Signal(dict)
    request_value_signal = Signal(dict)
    disconnected_singal = Signal()

    def __init__(self, nodes_handler:nodesHandler, loop_time:int, max_failed=3):
        super().__init__()
        self.loop_time = loop_time
        self.nodesHandler = nodes_handler
        self.is_connect  = True
        self.max_failed = max_failed
        self.faild_counter = 0
        self.new_values = {}
        self.old_values = {}
        self.__running = True
        self.requsts = []

    def read_requests(self,request_id:str, nodes_names:list[str]):
        self.requsts.append(
            {'id': request_id,
             'nodes_names': nodes_names
             }
        )
        pass

        


        
    def get_nodes_for_atuo_read(self,) -> list[str]:
        node_names = []
        for name in self.nodesHandler.get_names():
            snode_handler = self.nodesHandler.get_by_name(name)
            if not snode_handler.is_auto_read():
                continue

            snode_handler.time_counter_read(self.loop_time)

            if snode_handler.is_time_to_read():
                node_names.append(name)
        return node_names
    
    def get_nodes_for_request_reads(self,) -> list[str]:
        node_names = []
        for req in self.requsts:
            node_names = node_names + req['nodes_names']
        
        node_names = list(set(node_names))
      
        return node_names
    
    def call_event_for_changes(self):
        for name, value in self.new_values.items():
            if self.old_values.get(name) is None or self.old_values[name] != self.new_values[name]:
                self.old_values[name] = self.new_values[name]
                self.change_value_signal.emit(
                    {'name':name,
                    'value':value}
                )


    def call_event_for_request(self, node_values:dict):
        complete_reqs = []

        for req in self.requsts:
            names = req['nodes_names']
            answer = {'id': req['id'],
                      'values':{}
                      }
            for name in names:
                value = node_values.get(name)
                #if value is not None:
                answer['values'][name] = value
                #else:
                #    break
            else:
                self.request_value_signal.emit(answer)
                complete_reqs.append(req)

        
        for req in complete_reqs:
            self.requsts.remove(req)
                
                

        

    def run(self):        
        
        while self.__running:
            auto_node_names = self.get_nodes_for_atuo_read()
            request_nodes_names = self.get_nodes_for_request_reads()
            node_names = list( set(auto_node_names + request_nodes_names) )

            if len(node_names):
                #t = time.time()
                node_values = self.nodesHandler.get_values(node_names)        
                
                if node_values is None:
                    self.faild_counter+=1
                else:
                    self.new_values = {}
                    #seprate auto read node
                    for name, value in node_values.items():
                        if name in auto_node_names:
                            self.new_values[name] = value
                    

                    self.faild_counter=0
                    self.call_event_for_changes()
                    self.call_event_for_request(node_values)

                #print(time.time() - t)
                
            if self.faild_counter > self.max_failed:
                self.disconnected_singal.emit()
                    
                    

            #WARNING: don't hardcode self.loop_time.
            time.sleep(self.loop_time / 1000)


    def stop(self,):
        self.__running=False


if __name__ == "__main__":
    #from IPython import embed
    logging.basicConfig(level=logging.WARN)

    def test():
        plc.nodesHandler.define_node('run_stop', 
                                    "ns=4;i=3", 
                                    auto_read=True,
                                    read_refresh_time=100 )
        

        plc.nodesHandler.define_node('run_stop2', 
                                    "ns=4;i=2", 
                                    auto_write=True,
                                    write_program=[{'value':True, 'time':1000},
                                                    {'value':False, 'time':3000}] )

    #plc = PLCHandler("opc.tcp://192.168.0.1:4840")
    plc = PLCHandler("opc.tcp://192.168.0.1:4840")

    plc.connect_request()
    plc.set_connected_event(test)

    
    #plc.disconnect()
    #plc.run_threads()

    from PySide6.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)

    app.exec()

