import pandas as pd

df = pd.read_csv('my_df1.csv',index_col=0)
df_low100 = df[(df["diff"] < -90) & (df["diff"] > -110)]
df_hi100 = df[(df["diff"] > 90) & (df["diff"] < 110)]
df_low200 = df[(df["diff"] < -180) & (df["diff"] > -220)]
df_hi200 = df[(df["diff"] > 180) & (df["diff"] < 220)]
df_low300 = df[(df["diff"] < -270) & (df["diff"] > -330)]
df_hi300 = df[(df["diff"] > 270) & (df["diff"] < 330)]

print("\ndf shape =", df.shape)
print(df.Result.value_counts(normalize=True)*100)
print("\ndf_low100 shape =", df_low100.shape)
print(df_low100.Result.value_counts(normalize=True)*100)
print("\ndf_hi100 shape =", df_hi100.shape)
print(df_hi100.Result.value_counts(normalize=True)*100)
print("\ndf_low200 shape =", df_low200.shape)
print(df_low200.Result.value_counts(normalize=True)*100)
print("\ndf_hi200 shape =", df_hi200.shape)
print(df_hi200.Result.value_counts(normalize=True)*100)
print("\ndf_low300 shape =", df_low300.shape)
print(df_low300.Result.value_counts(normalize=True)*100)
print("\ndf_hi300 shape =", df_hi300.shape)
print(df_hi300.Result.value_counts(normalize=True)*100)
