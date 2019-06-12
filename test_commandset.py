from digilock_UI import Digilock_UI
from command import Command_type
import matplotlib.pyplot as plt

dui = Digilock_UI("10.9.114.193", 60001)

for command in dui.commandset:
    if command.settable:
        print(command.name+'.range='+dui.query_range(command.name))

for command in dui.commandset:
    if command.queryable:
        if command.type == Command_type.Enum:
            print('{command.name}={value}'.format(command=command, value=dui.query_enum(command)))
        if command.type == Command_type.Numeric:
            print('{command.name}={value}'.format(command=command, value=dui.query_numeric(command)))
        if command.type == Command_type.Bool:
            print('{command.name}={value}'.format(command=command, value=dui.query_bool(command)))
dui.close()
