import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data inlezen
data = pd.read_excel('Metingen Bloeddruk.xlsx', 1, usecols='D:E')
data_x = data['P']
data_y = data['U']

#berekenen formule voor de trendlijn
z = np.polyfit(data_x, data_y, 1)
p = np.poly1d(z)


#plot de trendlijn en data
plt.plot(data_x, p(data_x), c='grey', label='Trendlijn')
plt.scatter(data_x, data_y, c='black', label='Meetdata')

#plot van de foutmarges
plt.errorbar(data_x,data_y, 0.01, capsize=4, linestyle='', c='black')

#voeg aslabels toe
plt.xlabel('$\it{P}$ (mmHg)')
plt.ylabel('$\it{U}$ (V)')

#toevoegen legenda en rasterlijnen
plt.legend()
plt.grid(True)

plt.savefig(fname='Bloeddruk_1.svg', format='svg')
plt.show()