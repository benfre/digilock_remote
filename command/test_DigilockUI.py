import digilockUI

dui = digilockUI.DigilockUI("10.9.114.193", 60001)

analogP = dui.query_numeric("analog:proportional")
print(analogP)

dui.close()
