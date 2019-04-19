import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('my_df2.csv',index_col=0)
groups = df.groupby("Category")

categb = "Black Rating exceeds White by "
categw = "White Rating exceeds Black by "

categ_points = list(range(500, 0, -50))
categ_points += list(range(0, 501, 50))

#print(groups.describe())

plt_items = groups.count()
print(plt_items)
plt_items.plot(kind='bar')
plt.savefig("charts/distribution.png", bbox_inches = "tight")

for i in range(21):
    df2 = groups.get_group(i)
    df3 = pd.DataFrame(df2.Result.value_counts(normalize=True) * 100)
    df_out = "data/df" + str(i) + ".csv"
    df3.to_csv(df_out)
    if i == 0 or i == 20:
        pts_str = "500 points or more"
    if i < 11:
        if i != 0:
            pts_str = str(categ_points[i]) + " to " + str(categ_points[i-1]) + " points"
        title = categb + pts_str
    else:
        if i != 20:
            pts_str = str(categ_points[i-1]) + " to " + str(categ_points[i]) + " points"
        title = categw + pts_str
    print("\nCategory", i, '-', title)
    print(df3)
    out_path = "charts/chart" + str(i) + ".png"
    #title = "Category " + str(i)

    #df3.plot(kind='bar', ylim=(0,100), title=title)
    #plt.savefig(out_path, bbox_inches = "tight")

#plt.show()
