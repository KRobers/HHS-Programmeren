import pandas as pd
import plotly.express as px

def plot(path, title):

    data = pd.read_excel(path)
    fig = px.line(data, x='Frequency (Hz)', y= 'FFT Mag (a.u.)', title=title)
    fig.show()

plot('Audio Spectrum 2024-Buis 1.xlsx', 'Buis 1' )
plot('Audio Spectrum Buis 2 .xlsx', 'Buis 2')
plot('Audio Spectrum Buis 3.xlsx', 'Buis 3')
plot('Audio Spectrum Buis 4.xlsx', 'Buis 4')
plot('Audio Spectrum Buis 5.xlsx', 'Buis 5')
