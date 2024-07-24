

import streamlit as st
import pandas as pd 
import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt


link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(link)

st.write(df)


# Liste des continents uniques (avec une option "Tous")
continents = ["Tous"] + df['continent'].unique().tolist()

# Bouton de sélection du continent
selected_continent = st.selectbox("Filtrer par continent :", continents)

# Filtrage du DataFrame
if selected_continent == "Tous":
    filtered_df = df
else:
    filtered_df = df[df['continent'] == selected_continent]

# Affichage du DataFrame filtré
st.dataframe(filtered_df)



plt.figure(figsize=(10, 6))

linechart = sns.lineplot(data=df, x="year", y = "mpg")
st.write("ici on peux voir que les voitures des année 1981 ET 1982 sont plus économe en carburant que celal étant anteriures ")
st.pyplot(linechart.figure)
plt.figure(figsize=(10, 6))
linechart1 = sns.lineplot(data=df, x="year", y = "cylinders")
st.write("ici on peux voir qu'a partir de 1981 on chute brutalement de 6 cylindres a 4 cylindres dans les moteurs des voitures ")
st.pyplot(linechart1.figure)
plt.figure(figsize=(10, 6))
linechart3 = sns.lineplot(data=df, x="year", y = "hp")
st.write("ici on peux voir qu'apres une stabilité autour de 100 hp de puissances les votures on chutée a 80 hp a partir de 1980 ")
st.pyplot(linechart3.figure)
plt.figure(figsize=(10, 6))
linechart4 = sns.lineplot(data=df, x="year", y = "weightlbs" )
st.write("ici nous pouvosn voir qu'a partir de 1980 les poids des voitures on diminués drastiquement de 800 lbs ")
st.pyplot(linechart4.figure)
plt.figure(figsize=(10, 6))
linechart5 = sns.lineplot(data=df, x="year", y = "time-to-60" )
st.write("ici on peucx voir en revanche que c'est avant 1970 que les voiture atteignais 60 MPH le plus rapidement mais par la suite cela s'est stabilisé autour des 17 Secondes ")
st.pyplot(linechart5.figure)
viz_correlation = sns.heatmap(df.iloc[:, 0:6].corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)


