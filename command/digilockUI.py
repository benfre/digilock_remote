import telnetlib
from typing import List

class DigilockUI:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.tn = telnetlib.Telnet(host, port)
        self.tn.read_until(b"> ", timeout=10) # wait to first prompt
    
    def close (self) -> None:
        self.tn.close()

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
    
    def query_bool(self, command: str) -> bool:
        line = self.query_lines(command)
        return line[0].strip().lower() == "true"
