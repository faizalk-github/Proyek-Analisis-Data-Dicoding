import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Memuat data dari CSV
customers_df = pd.read_csv('customers_dataset.csv')
orders_df = pd.read_csv('orders_dataset.csv')
order_reviews_df = pd.read_csv('order_reviews_dataset.csv')

# Menggabungkan customers_df dengan orders_df berdasarkan customer_id
merged_df = pd.merge(customers_df, orders_df, on='customer_id', how='inner')

# Menggabungkan hasil gabungan pertama dengan order_reviews_df berdasarkan order_id
all_df = pd.merge(merged_df, order_reviews_df, on='order_id', how='inner')

# Menghitung jumlah pelanggan untuk setiap kota
city_distribution = all_df['customer_city'].value_counts()

# Memilih 10 kota dengan pelanggan terbanyak
top_10_cities = city_distribution.head(10)

# Memfilter hasil gabungan berdasarkan top 10 kota
all_df_top_10_cities = all_df[all_df['customer_city'].isin(top_10_cities.index)]

# Streamlit Dashboard
st.title('Customer Analysis Dashboard')

# Visualisasi 1: Distribusi Geografis Pelanggan untuk 10 Kota Teratas
st.header('Distribusi Geografis Pelanggan')
st.subheader('Top 10 Kota dengan Jumlah Pelanggan Terbanyak')
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_10_cities.values, y=top_10_cities.index, palette='viridis', ax=ax1)
ax1.set_title('Distribusi Lokasi Geografis Pelanggan (Top 10 Kota)')
ax1.set_xlabel('Jumlah Pelanggan')
ax1.set_ylabel('Kota')
st.pyplot(fig1)

# Visualisasi 2: Distribusi Review Score
st.header('Distribusi Review Score')
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.countplot(x='review_score', data=order_reviews_df, palette='viridis', ax=ax2)
ax2.set_title('Distribusi Review Score')
ax2.set_xlabel('Review Score')
ax2.set_ylabel('Jumlah Review')
st.pyplot(fig2)

# Visualisasi 3: Distribusi Review Score untuk 10 Kota dengan Pelanggan Terbanyak
st.header('Distribusi Review Score untuk Top 10 Kota dengan Pelanggan Terbanyak')
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.countplot(x='review_score', data=all_df_top_10_cities, palette='viridis', ax=ax3)
ax3.set_title('Distribusi Review Score Top 10 Kota Teratas')
ax3.set_xlabel('Review Score')
ax3.set_ylabel('Jumlah Review')
st.pyplot(fig3)
 
st.caption('Copyright (c) Faizal Kurniawan 2024')

