import pandas as pd

df_1 = pd.read_csv("pod1.csv")
df_2 = pd.read_csv("pod2.csv")
df_3 = pd.read_csv("pod3.csv")

# join df_1 and df_2 on email, localID, and insertID using pd.join

df = pd.merge(df_1, df_2, on=["messageID", "email", "localID", "insertID"])

# join df on email, localID, and insertID
df = pd.merge(df, df_3, on=["messageID", "email", "localID", "insertID"])

# print df
print(df)