import pandas as pd
import matplotlib.pyplot as plt

# openen van de datasets
buis1 = pd.read_excel('Audio Spectrum 2024-Buis 1.xlsx')
buis2 = pd.read_excel('Audio Spectrum Buis 2 .xlsx')

# creëren van de plot voor beide datasets
plt.plot(buis1['Frequency (Hz)'], buis1['FFT Mag (a.u.)'], label='Buis 1')
plt.plot(buis2['Frequency (Hz)'], buis2['FFT Mag (a.u.)'], label='Buis 2')

# tekst op de assen toevoegen
plt.xlabel('Frequentie (Hz)')
plt.ylabel('FFT Magnitude (a.u.)')

# legenda en rasters toevoegen
plt.legend()
plt.grid(True)

# Opslaan van het plotje als svg bestand
plt.savefig('plotje.svg', format='svg')

# tonen van de plot
plt.show()
