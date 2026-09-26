import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard về Chia sẻ Xe đạp ở Seoul", layout="wide")
st.title("🚲 Dashboard về Nhu cầu Chia sẻ Xe đạp ở Seoul")
st.markdown("Phân tích tương tác về nhu cầu thuê xe đạp hàng giờ dựa trên dữ liệu thời tiết và lịch.")

@st.cache_data
def load_data():
    df = pd.read_csv("./data/SeoulBikeData.csv", encoding="latin1")

    df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")
    df['Month'] = df['Date'].dt.month_name()
    df['Day of Week'] = df['Date'].dt.day_name()

    df['Seasons'] = pd.Categorical(df['Seasons'], categories=['Spring', 'Summer', 'Autumn', 'Winter'], ordered=True)
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df['Day of Week'] = pd.Categorical(df['Day of Week'], categories=days_order, ordered=True)

    return df

df = load_data()

st.subheader("Các Chỉ Số Hiệu Suất Chính")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Tổng Số Lượt Thuê", f"{df['Rented Bike Count'].sum():,}")
col2.metric("Trung Bình Lượt Thuê Hàng Ngày", f"{int(df.groupby('Date')['Rented Bike Count'].sum().mean()):,}")
col3.metric("Giờ Cao Điểm", f"{df.groupby('Hour')['Rented Bike Count'].sum().idxmax()}:00")
col4.metric("Mùa Phổ Biến Nhất", df.groupby('Seasons')['Rented Bike Count'].sum().idxmax())

st.divider()

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.subheader("1. Xu hướng Nhu cầu Hàng giờ theo Mùa")
    hourly_season_avg = df.groupby(['Hour', 'Seasons'])['Rented Bike Count'].mean().reset_index()
    fig1 = px.line(hourly_season_avg, x='Hour', y='Rented Bike Count', color='Seasons', markers=True,
                   title="Trung bình Lượt thuê theo Giờ trong Ngày (Theo Mùa)")
    st.plotly_chart(fig1, use_container_width=True)

with col_b:
    st.subheader("2. Nhu cầu theo Ngày trong Tuần")
    dow_avg = df.groupby('Day of Week')['Rented Bike Count'].mean().reset_index()
    fig2 = px.bar(dow_avg, x='Day of Week', y='Rented Bike Count', color='Day of Week',
                  title="Trung bình Lượt thuê trong Tuần")
    st.plotly_chart(fig2, use_container_width=True)

with col_c:
    st.subheader("3. Nhiệt độ & Lượt thuê")
    fig3 = px.scatter(df, x='Temperature(°C)', y='Rented Bike Count', color='Seasons',
                      opacity=0.6, title="Tác động của Nhiệt độ đến Lượt thuê")
    st.plotly_chart(fig3, use_container_width=True)

col_d, col_e, col_f = st.columns(3)


with col_d:
    st.subheader("4. Phân bố theo Mùa")
    fig4 = px.box(df, x='Seasons', y='Rented Bike Count', color='Seasons',
                  title="Sự biến thiên Phân bố Lượt thuê theo Mùa")
    st.plotly_chart(fig4, use_container_width=True)

with col_e:
    st.subheader("5. Tác động của Lượng mưa")
    rain_df = df[df['Rainfall(mm)'] > 0]
    fig5 = px.scatter(rain_df, x='Rainfall(mm)', y='Rented Bike Count', size='Rainfall(mm)',
                      title="Lượt thuê trong những ngày có Mưa")
    st.plotly_chart(fig5, use_container_width=True)

with col_f:
    st.subheader("6. Mức độ Độ ẩm")
    fig6 = px.histogram(df, x='Humidity(%)', y='Rented Bike Count', histfunc='avg', nbins=20,
                        title="Trung bình Lượt thuê theo Mức Độ ẩm")
    st.plotly_chart(fig6, use_container_width=True)
col_g, col_h, col_i = st.columns(3)

with col_g:
    st.subheader("7. Ngày lễ vs Ngày thường")
    holiday_avg = df.groupby('Holiday')['Rented Bike Count'].mean().reset_index()
    fig7 = px.bar(holiday_avg, x='Holiday', y='Rented Bike Count', text_auto='.0f',
                  color='Holiday', title="Trung bình Lượt thuê: Ngày lễ vs Ngày thường")
    st.plotly_chart(fig7, use_container_width=True)

with col_h:
    st.subheader("8. Ma trận Tương quan Đặc trưng")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    corr = df[numeric_cols].corr()
    fig8 = px.imshow(corr, text_auto=".2f", aspect="auto", color_continuous_scale="RdBu_r",
                     title="Tương quan Tuyến tính của các Đặc trưng Số")
    st.plotly_chart(fig8, use_container_width=True)

col_i.empty()