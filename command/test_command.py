from telnetlib import Telnet

tn = Telnet("10.9.114.193", 60001)

tn.read_until(b"> ", timeout=10)

tn.write("analog:proportional?".encode('ascii')+b"\n")
return_str = tn.read_until(b"> ", timeout=1).decode('ascii')
splitted_str = return_str.split('\n')
del splitted_str[-1]
del splitted_str[0]
splitted_str[0] = splitted_str[0].split('=')[1]

for command in splitted_str:
    print(command)

tn.write("exit".encode('ascii')+b"\n")
tn.read_all()
tn.close()
