

import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import calendar


#LOAD DATASET
df_day = pd.read_csv("./Bike Sharing/Dataset.csv")


def pertanyaan1(df):

    st.subheader('Bagaimana penyewaan pada setiap musimnya?')
    
    season_sum = df_day.groupby('season')['cnt'].sum()
    fig, ax = plt.subplots()
    ax.bar(x=season_sum.index, height=season_sum.values)
    plt.title('Bar Chart Penyewaan Sepeda Pada Setiap Musimnya')
    st.pyplot(fig)

    fig, ax = plt.subplots()
    colors = ('#f59642', '#eff542', '#57eba1', '#42cbf5')
    ax.pie(
        x=season_sum.values,
        autopct='%1.1f%%',
        labels = season_sum.index,
        colors=colors,
    )
    plt.title('Pie Chart Penyewaan Sepeda Pada Setiap Musimnya')
    st.pyplot(fig)
    

def pertanyaan2(df):
    weather_situations = {
        1: 'Clear, Few clouds, Partly cloudy, Partly cloudy',
        2: 'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist',
        3: 'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds',
        4: 'Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog'
    }

    # Create a pie chart
    st.subheader('Bagaimana Pengaruh cuaca terhadap penyewaan sepeda?')
    
    weathersum = df_day.groupby('weathersit')['cnt'].sum()
    fig, ax = plt.subplots(figsize=(15, 3))  # Adjust the size here
    colors = ('#32a2a8', '#7aeb57', '#57eba1', '#E67F0D')
    patches, texts, autotexts = ax.pie(
        x=weathersum,
        autopct='%1.1f%%',
        colors=colors,
    )
    plt.title("pie chart dari jumlah penyewaan sepeda berdasarkan cuaca")
    
    ax.legend(patches, weather_situations.values(), title="Weather Situations", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    st.pyplot(fig)

def pertanyaan3(df):
    year_2011 = df[df['yr'] == 0]

    grouped = year_2011.groupby('mnth')

    casual_sum = grouped['casual'].sum()
    registered_sum = grouped['registered'].sum()

    casual_sum = casual_sum.sort_index()
    registered_sum = registered_sum.sort_index()

    st.subheader('Bagaimana penyewaan sepeda di tahun 2011 setiap bulannya berdasarkan penyewa registered dan casual?')
    fig, ax = plt.subplots()
    colors = ('#f5a442', '#42a7f5')
    types = ['registered','casual']
    ax.pie(
        x=year_2011[types].sum(),
        autopct='%1.1f%%',
        labels = types,
        colors=colors,
    )
    plt.title('Pie Chart Penyewaan oleh penyewa registered and casual Sepeda Pada tahun 2011')
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(10, 5))

    plt.xticks(range(1, 13), calendar.month_name[1:13],rotation=45)
    plt.plot(casual_sum.index, casual_sum.values, label='Casual')
    plt.plot(registered_sum.index, registered_sum.values, label='Registered')

    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Penyewaan sepeda di tahun 2011 setiap bulannya berdasarkan penyewa registered dan casual')

    plt.legend()

    st.pyplot(fig)

tab1, tab2, tab3 = st.tabs(["Pertanyaan 1", "Pertanyaan 2", "Pertanyaan 3"])
 
with tab1:
    pertanyaan1(df_day)
    st.text_area("CONCLUSION","Penyewaan sepeda pada tiap musimnya fall merupakan season dengan penyewa terbanyak. Penyewaan sepeda paling sedikit adalah ketika musim springer. Dan penyewa winter dan summer hampir sama yaitu hanya berbeda sekitar 1 persen dengan penyewaan di musim winter lebih banyak dari summer.",disabled = True,height =120)
with tab2:
    pertanyaan2(df_day)
    st.text_area("CONCLUSION","Cuaca sangat berpengaruh pada penyewaan sepedah. Sekitar 68 persen orang menyewa sepedah ketika cuaca cerah atau berawan. Sedangkan pada cuaca ekstrim seperti badai, hujan, atau hujan salju orang jarang menyewa sepeda berdasarkan pie chart hanya sekitar 1 persen saja.",disabled = True)
with tab3:
    pertanyaan3(df_day)
    st.text_area("CONCLUSION","Angka penyewaan oleh penyewa yang teregistrasi lebih tinggi dibandingkan penyewa casual di setiap bulan pada tahun 2011. Penyewaan oleh penyewa yang teregistrasi memiliki kenaikan yang tinggi pada bulan maret hingga mei dan memiliki kecenderungan turun pada bulan juni hingga desember. begitu juga penyewaan sepeda yang dilakukan oleh penyewa casual yang cenderung naik pada bulan januari hingga juni dan mengalami penurunan dari bulan juli hingga desember.",disabled = True,height =150)
 
with st.sidebar:
    st.title('PROYEK AKHIR DICODING - Belajar Analisis Data dengan Python ')
    st.text('NAMA : HANIF ADITIA SOFIAN')
    st.text('EMAIL BANGKIT : m012d4ky3007@bangkit.academy')
    st.text('ID DICODING : hanifaditia')
    
