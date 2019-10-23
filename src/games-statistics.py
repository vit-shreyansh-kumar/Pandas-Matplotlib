import pandas as pd
import matplotlib.pyplot as plt

# Question 1 Ans

readdata = pd.read_csv('summer.csv')
df = readdata.groupby(by=['Year', 'Athlete', 'Gender'],as_index=False).Medal.count()
dfobj = pd.DataFrame(columns=['Year','Athlete','Gender','MedalCount'])
years = df['Year'].unique().tolist()
for year in years:
    mframe = df.loc[(df['Year'] == year) & (df['Gender'] == 'Men')]
    mframe = mframe[mframe['Medal'] == mframe['Medal'].max()]
    if mframe.shape[0] != 0:
        mframe = mframe.iloc[0]
        dfobj =dfobj.append({'Year': mframe['Year'],
                      'Athlete': mframe['Athlete'],
                      'Gender': mframe['Gender'],
                      'MedalCount': mframe['Medal']}, ignore_index=True)

    fframe = df.loc[(df['Year'] == year) & (df['Gender'] == 'Women')]
    fframe = fframe[fframe['Medal'] == fframe['Medal'].max()]
    if fframe.shape[0] != 0:
        fframe = fframe.iloc[0]
        dfobj =dfobj.append({'Year': fframe['Year'],
                      'Athlete': fframe['Athlete'],
                      'Gender': fframe['Gender'],
                      'MedalCount': fframe['Medal']}, ignore_index=True)

dfobj = dfobj.drop_duplicates()
""" Result of the 1st Question """
print("Yearwise Men and Women athelete", dfobj)

""" Plot of the 1st Question """
dcobj = dfobj.set_index("Year","Athlete")

ax = dcobj.plot(kind="bar", title="Summer Olympics Performance 1896-2012", figsize=(15, 10))
ax.set_xlabel("Athlete", fontsize=12)
ax.set_ylabel("Medal Count", fontsize=12)
plt.show()

#Question 2 Ans


df = pd.read_csv("summer.csv")
# Group data by Year, Gender and Country
countries = df['Country'].unique().tolist()
dcobj = pd.DataFrame(columns=['Country','Men','Women','MedalCount'])

for country in countries:
    mcount = df.loc[(df['Country'] == country) & (df['Gender'] == 'Men')].shape[0]
    fcount = df.loc[(df['Country'] == country) & (df['Gender'] == 'Women')].shape[0]
    dcobj = dcobj.append({'Country': country,
                          'Men': mcount,
                          'Women': fcount,
                          'MedalCount': mcount+fcount }, ignore_index=True)

dcobj = dcobj.sort_values('MedalCount',ascending=False).head(10)

dcobj = dcobj.set_index("Country")
ax = dcobj.plot(kind="bar", title="Summer Olympics Performance 1896-2012", figsize=(15, 10))
ax.set_xlabel("Country", fontsize=12)
ax.set_ylabel("Medal Count", fontsize=12)
plt.show()