import matplotlib.pyplot as plt
import numpy as np

def WinLosePieChart(percentages, fig_name=None):
    activities = ["Win", "Lose", "Draw"]

    fig, ax = plt.subplots()

    size = 0.5

    cmap = plt.get_cmap("tab20c")
    outer_colors = cmap(np.arange(3) * 4)

    ax.pie(percentages, radius=1, colors=outer_colors,
           startangle=135, labels=activities, labeldistance=0.7,
           wedgeprops=dict(width=size, edgecolor='w'))

    if fig_name == None:
        plt.show()
    else:
        plt.savefig(fig_name)

#WinLosePieChart([44.3, 51.0, 4.7], "fig1.png")
WinLosePieChart(np.array([48, 43, 9]), "fig2.png")
#WinLosePieChart(np.array([49.466, 46.786, 3.748]))
