import telnetlib
from typing import List, Dict
import numpy as np
from enum import Enum

from commandlist import Command, digilockUI_commands, Command_type

class DigilockUI:
    def __init__(self, host: str, port: int, commandset:List[Command] = None):
        self.host = host
        self.port = port
        self.tn = telnetlib.Telnet(host, port)
        self.tn.read_until(b"> ", timeout=10) # wait to first prompt
        if commandset:
            self.commandset = commandset
        else:
            self.commandset = digilockUI_commands
    
    def close (self) -> None:
        self.tn.close()

    def get_command_info(self, command: str) -> Command:
        coms = [com for com in self.commandset if com.name == command]
        if coms:
            return coms[0]
        else:
            return None
        
    def query_lines(self, command: str) -> List[str]:
        self.tn.write((command+"?").encode('ascii')+b"\n")
        return_str = self.tn.read_until(b"> ", timeout=1).decode('ascii')
        splitted_str = return_str.split('\n')
        del splitted_str[-1]
        del splitted_str[0]
        splitted_str[0] = splitted_str[0].split('=')[1]
        return splitted_str

    def query_numeric(self, command: str) -> float:
        line = self.query_lines(command)
        return float(line[0])

    def query_enum(self, command: str) -> str:
        com = self.get_command_info(command)
        if com:
            line = self.query_lines(com.name)
            value = line[0].strip()
            if com.enum_type !=None:
                items = [item for item in com.enum_type if item.value == value]
                if items:
                    return items[0] # should only one matched
        else:
            line = self.query_lines(command)
            value = line[0].strip()
            return value

    
    def query_bool(self, command: str) -> bool:
        line = self.query_lines(command)
        return line[0].strip().lower() == "true"

    def query_graph(self, command: str) -> np.ndarray:
        lines = self.query_lines(command)
        nums = lines[0].split()
        data = np.ndarray((len(lines), len(nums)))
        for count, line in enumerate(lines):
            line_num = np.fromstring(line, sep=' ')
            data[count] = line_num
        return data

    def set_numeric(self, command: str, value: float) -> None:
        self.tn.write((command+"={}".format(value)).encode('ascii')+b"\n")
        self.tn.read_until(b"> ", timeout=1)
    
    def set_bool(self, command: str, value: bool) -> None:
        tf = "{}".format(value).lower()
        self.tn.write((command+"="+tf).encode('ascii')+b"\n")
        self.tn.read_until(b"> ", timeout=1)

    def set_enum(self, command: str, item: Enum) -> None:
        value = "{}".format(item.value)
        self.tn.write((command+"="+value).encode('ascii')+b"\n")
        self.tn.read_until(b"> ", timeout=1)
    