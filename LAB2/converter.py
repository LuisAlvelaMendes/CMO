"""
Range	60,0dB	-120,0dBm
Mobile unit	1	Mobile Terminal	 00,00000	 000,00000	0,0
Fixed unit	2	Monte da Virgem	 41,11313	-008,59838	200,1
Fixed unit	3	Sardoura	 41,04918	-008,31171	316,6
Fixed unit	4	Resende	 41,13410	-007,98018	552,6
Fixed unit	7	Exercise3Celorico	 41,33887	-007,84056	1301,0
Fixed unit	8	Exercise3Felgueiras	 41,32088	-008,28529	502,6
"""

import pandas as pd 
from pandas import ExcelWriter
from pandas import ExcelFile 

df = pd.read_excel('question3/exercise3.xlsx', sheet_name='Sheet2')

""" histogram
import matplotlib.pyplot as plt
powersReceived = df['Pr(dBm)']
powersReceived.hist(normed=0, histtype='stepfilled', bins=20)
plt.xlabel('Power Received (dBm)',fontsize=15)
plt.ylabel('Samples',fontsize=15)
plt.show()
"""

""" scatter plots
plt.subplot(1,2,1)
plt.scatter(df['BestUnit'], df['Pr(dBm)'],color='b',s=120, linewidths=2,zorder=10)
plt.xlabel('Unit',fontsize=15)
plt.ylabel('Power Received (dBm)',fontsize=15)
plt.gcf().set_size_inches((20,6))
"""

"""
used for exercises 1, 2 and 3
"""
lessThan120 = df[(df['Pr(dBm)'] < -120)]
lessThan110 = df[(df['Pr(dBm)'] < -110)]

print("Percentagem Pr < -120:",(len(lessThan120.index))/float(len(df.index)) * 100)
print("Percentagem Pr < -110:",(len(lessThan110.index))/float(len(df.index)) * 100)

between0and10 = df[(df['Rx(dB)'] < 10) & (df['Rx(dB)'] >= 0)]
between10and20 = df[(df['Rx(dB)'] < 20) & (df['Rx(dB)'] >= 10)]
between20and30 = df[(df['Rx(dB)'] < 30) & (df['Rx(dB)'] >= 20)]
between30and40 = df[(df['Rx(dB)'] < 40) & (df['Rx(dB)'] >= 30)]
between40and50 = df[(df['Rx(dB)'] < 50) & (df['Rx(dB)'] >= 40)]
between50and60 = df[(df['Rx(dB)'] < 60) & (df['Rx(dB)'] >= 50)]
above60 = df[(df['Rx(dB)'] >= 60)]

print("Percentagem maior: ", (len(between20and30.index))/float(len(df.index)) * 100)

"""
used for exercise 4
"""
newSitesAsBestUnit = df[(df['BestUnit'] == 8) | (df['BestUnit'] == 7)]
siteAsBestUnit7 = df[(df['BestUnit'] == 7)]
siteAsBestUnit8 = df[(df['BestUnit'] == 8)]

print("Locations with new sites as best unit:", len(newSitesAsBestUnit.index))
print("Locations with site 7 as best unit (celorico):", len(siteAsBestUnit7.index))
print("Locations with site 8 as best unit (felgueiras):", len(siteAsBestUnit8.index))