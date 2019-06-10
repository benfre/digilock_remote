import digilockUI
import matplotlib.pyplot as plt

dui = digilockUI.DigilockUI("10.9.114.193", 60001)

analogP = dui.query_numeric("analog:proportional")
pid1_gain = dui.query_numeric("pid1:gain")
print(analogP)
print(pid1_gain)

autolock_enable = dui.query_bool("autolock:enable")
print(autolock_enable)

autolock_relock_enable = dui.query_bool("autolock:relock:enable")
print(autolock_relock_enable)

graph1 = dui.query_graph("autolock:display:graph")
print(graph1[0])
print(graph1.shape)

figsize = (10, 8)
fig1, axs = plt.subplots(2, 3, figsize=figsize, constrained_layout=True)

for count, ax in enumerate(axs.flatten()):
    ax.plot(graph1[:,count])
dui.close()
plt.show()