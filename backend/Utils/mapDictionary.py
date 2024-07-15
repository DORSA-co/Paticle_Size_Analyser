class mapDictionary:

    def __init__(self,maps:dict[str,dict]) -> None:
        self.maps = maps

    def add_map(self, map_name:str, maps:dict):
        self.maps[map_name] = maps

    def get_maps_names(self,):
        return list(self.maps.keys())

    def get_values(self, map_name):
        return list(self.maps[map_name].values())
    
    def get_keys(self, map_name):
        return list(self.maps[map_name].keys())
    
    def map_exist(self, map_name):
        return map_name in self.maps.keys()
    
    def value2key(self, map_name:str, value):
        if self.map_exist(map_name):
            return self.__find_key(
                _dict = self.maps[map_name],
                subject_value = value
            )
        return value
    
    def key2value(self, map_name:str, key:str):
        if self.map_exist(map_name):
            return self.maps[map_name][key]
        return key
    

    def multi_key2value(self, transitions:dict):
        """a dictionary that keys are map name and values are
           transition_key. if map_name doesn't exist,
           it returns self value

        Args:
            transitions (dict): _description_

        Returns:
            _type_: _description_
        """
        for map_name, key in transitions.items():
            transitions[map_name] = self.key2value(map_name, key=key)
        return transitions
    

    def multi_value2key(self, transitions:dict):
        """a dictionary that keys are map name and values are
           transition_key. if map_name doesn't exist,
           it returns self value

        Args:
            transitions (dict): _description_

        Returns:
            _type_: _description_
        """
        for map_name, value in transitions.items():
            if self.map_exist(map_name):
                transitions[map_name] = self.value2key(map_name, value=value)
                
        return transitions

    
    def __find_key(self, _dict:dict, subject_value):
        for key, value in _dict.items():
            if value == subject_value:
                return key
        return None