import pandas as pd

df_1 = pd.read_csv("pod1.csv")
df_2 = pd.read_csv("pod2.csv")
df_3 = pd.read_csv("pod3.csv")

# join df_1 and df_2

df = pd.merge(df_1, df_2, on=["localID", "email", "insertID", "messageID", "waitTime"])

# join df and df_3
df = pd.merge(df, df_3, on=["localID", "email", "insertID", "messageID", "waitTime"])

# print df
print(df)