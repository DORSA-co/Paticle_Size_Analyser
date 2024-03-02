from Constants.CONSTANTS import serialInfo
import serial

class armSerial:


    def __init__(self) -> None:
        self.port = None
        self.serial = None
        self.connection_status = False

    def set_port(self, port:str):
        self.port = port.upper()
    
    def connect(self,):
        if self.port is not None:
            try:
                self.serial = serial.Serial(self.port, serialInfo.BAUD_RATE)
                self.connection_status = True

            except Exception as e:
                print(str(e))
                self.connection_status = False
        else:
            print('ERROR:port is not defined')
            self.connection_status = False

        return self.connection_status

    
    def set_fps(self, fps:int):
        self.write(f'%{{:02d}}'.format(fps))

    def write(self, packet:str):
        if self.connection_status:
            self.serial.write(packet.encode())
    
    def read_all(self,) -> str:
        if self.connection_status:
            return self.serial.read(2).decode("utf-8") 

    
    def disconnect(self,):
        if self.serial is not None:
            self.serial.close()
        self.connection_status = False

        
        

    def get_serial_pots(self,):
        ports = []
        for i in range(1, serialInfo.MAX_PORT_COM+1):
            com = f'COM{i}'
            ports.append(com)
        return ports
