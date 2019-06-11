from enum import Enum

class StrEnum(Enum):
    def __str__(self):
        return self.value

class Command_type(Enum):
    Enum = 1
    Numeric = 2
    Bool = 3
    Array = 4
    Graph = 5

class Access_control_enum(StrEnum):
    pass

class Analog_tab_enum(StrEnum):
    General = 'General'

class Autolock_display_active_trace_enum(StrEnum):
    Spectrum = 'Spectrum'
    Input = 'Input'

class Autolock_display_channel(StrEnum):
    Main_in = 'Main in'
    Aux_in = 'Aux in'

class Pid_output_enum(StrEnum):
    Main_out ='Main out'
    Aux_out ='Aux out'
    SC110_out ='SC110 out'
    DCC_Iset = 'DCC Iset'
    DTC_Tset = 'DTC_Tset'
    AIO_1_out ='AIO 1 out'
    AIO_2_out ='AIO 2 out'

class Command():
    def __init__(self,name: str,command_type: Command_type, enum_type=None, queryable=False,settable=False):
        self.name=name
        self.type=command_type
        self.enum_type = enum_type
        self.queryable = queryable
        self.settable = settable

digilockUI_commands = [
    Command(name='analog:lock:enable', command_type=Command_type.Bool, enum_type= None, queryable=True, settable=True),
    Command(name='analog:proportional', command_type=Command_type.Numeric, enum_type= None, queryable=True, settable=True),
    Command(name='analog:tab', command_type=Command_type.Enum, enum_type= Analog_tab_enum,queryable=True, settable=True),
    Command(name='autolock:display:graph', command_type=Command_type.Graph, enum_type= None,queryable=True, settable=False),
    Command(name='autolock:display:ch1:channel', command_type=Command_type.Enum, enum_type= Autolock_display_channel,queryable=True, settable=True),
    Command(name='pid2:output', command_type=Command_type.Enum, enum_type= Pid_output_enum,queryable=True, settable=True)
]
