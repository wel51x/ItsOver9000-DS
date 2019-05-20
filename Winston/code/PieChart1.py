import matplotlib.pyplot as plt

def WinLosePieChart(percentages, fig_name=None):
    activities = ["Win", "Lose", "Draw"]
    colors = ['b', 'magenta', 'cyan']

    plt.pie(percentages, labels=activities, colors=colors,
            startangle=90, autopct='%.1f%%')

    my_circle = plt.Circle((0, 0), 0.4, color='white')
    p = plt.gcf()
    p.gca().add_artist(my_circle)

    if fig_name == None:
        plt.show()
    else:
        plt.savefig(fig_name)

WinLosePieChart([44.1, 50.2, 5.7], "fig1.png")
#WinLosePieChart([49, 44, 7])
