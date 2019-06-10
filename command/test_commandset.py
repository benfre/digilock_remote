import digilockUI
from commandlist import digilockUI_commands, Command_type
import matplotlib.pyplot as plt

dui = digilockUI.DigilockUI("10.9.114.193", 60001)

for command in digilockUI_commands:
    if command.settable:
        print(command.name+' range='+dui.query_enum(command.name+'.range'))

for command in digilockUI_commands:
    if command.queryable:
        if command.type == Command_type.Enum:
            print(command.name+'={}'.format( dui.query_enum(command.name)))
        if command.type == Command_type.Numeric:
            print(command.name+'={}'.format(dui.query_numeric(command.name)))
        if command.type == Command_type.Bool:
            print(command.name+'={}'.format(dui.query_bool(command.name)))
dui.close()
