df = pd.read_csv('https://raw.githubusercontent.com/hungitnoi/model-for-project/refs/heads/master/df_voz.csv?token=GHSAT0AAAAAACZP4P5EEH26LEWSV7VO2RVAZZTMLGQ')
# print(df)

#data preparation
#data separation as X and Y
y = df['label']
print(y)
