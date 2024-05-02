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
plt.plot(data_x, p(data_x))
plt.scatter(data_x, data_y)

#voeg aslabels toe
plt.xlabel('P (mmHg)')
plt.ylabel('U (V)')

#toevoegen legenda en rasterlijnen
plt.legend()
plt.grid(True)

plt.show()