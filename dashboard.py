import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard về Chia sẻ Xe đạp ở Seoul", layout="wide")
st.title("🚲 Dashboard về Nhu cầu Chia sẻ Xe đạp ở Seoul")
st.markdown("Phân tích tương tác về nhu cầu thuê xe đạp hàng giờ dựa trên dữ liệu thời tiết và lịch.")

SEASON_ORDER = ['Spring', 'Summer', 'Autumn', 'Winter']
SEASON_COLORS = {
    'Spring': '#2A9D8F',
    'Summer': '#E9C46A',
    'Autumn': '#E76F51',
    'Winter': '#457B9D',
}
DOW_ORDER = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def style_chart(fig):
    fig.update_layout(
        template='plotly_white',
        height=390,
        margin=dict(l=12, r=12, t=52, b=12),
        font=dict(family='Arial', size=12, color='#243447'),
        legend=dict(orientation='h', y=1.08, x=0, title=None),
        hoverlabel=dict(bgcolor='white', font_size=12),
    )
    return fig

@st.cache_data
def load_data():
    df = pd.read_csv("./data/SeoulBikeData.csv", encoding="utf-8-sig")

    df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")
    df['Month'] = df['Date'].dt.month_name()
    df['Day of Week'] = df['Date'].dt.day_name()

    df['Seasons'] = pd.Categorical(df['Seasons'], categories=['Spring', 'Summer', 'Autumn', 'Winter'], ordered=True)
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df['Day of Week'] = pd.Categorical(df['Day of Week'], categories=days_order, ordered=True)
    df = df.loc[df['Functioning Day'].eq('Yes')].copy()

    return df

df = load_data()
st.caption("Các chỉ số và biểu đồ chỉ tính những giờ hệ thống hoạt động.")

st.subheader("Các Chỉ Số Hiệu Suất Chính")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Tổng Số Lượt Thuê", f"{df['Rented Bike Count'].sum():,}")
col2.metric("Trung Bình Lượt Thuê Hàng Ngày", f"{int(df.groupby('Date')['Rented Bike Count'].sum().mean()):,}")
col3.metric("Giờ Cao Điểm", f"{df.groupby('Hour')['Rented Bike Count'].sum().idxmax()}:00")
col4.metric("Mùa Phổ Biến Nhất", df.groupby('Seasons')['Rented Bike Count'].sum().idxmax())

st.divider()

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("1. Xu hướng Nhu cầu Hàng giờ theo Mùa")
    hourly_season_avg = df.groupby(['Hour', 'Seasons'])['Rented Bike Count'].mean().reset_index()
    fig1 = px.line(hourly_season_avg, x='Hour', y='Rented Bike Count', color='Seasons', markers=True,
                   category_orders={'Seasons': SEASON_ORDER}, color_discrete_map=SEASON_COLORS,
                   title="Trung bình lượt thuê theo giờ trong ngày")
    fig1.update_traces(hovertemplate='Giờ: %{x}:00<br>Trung bình: %{y:,.0f} lượt<extra>%{fullData.name}</extra>')
    fig1.update_xaxes(dtick=2, title='Giờ trong ngày')
    fig1.update_yaxes(title='Lượt thuê trung bình')
    st.plotly_chart(style_chart(fig1), width='stretch')

with col_b:
    st.subheader("2. Nhu cầu theo Ngày trong Tuần")
    dow_avg = df.groupby('Day of Week')['Rented Bike Count'].mean().reset_index()
    fig2 = px.bar(dow_avg, x='Day of Week', y='Rented Bike Count',
                  category_orders={'Day of Week': DOW_ORDER}, color_discrete_sequence=['#2A9D8F'],
                  text_auto='.0f', title="Trung bình lượt thuê theo ngày")
    fig2.update_traces(hovertemplate='%{x}<br>Trung bình: %{y:,.0f} lượt<extra></extra>')
    fig2.update_xaxes(title='Ngày trong tuần', tickangle=-25)
    fig2.update_yaxes(title='Lượt thuê trung bình')
    st.plotly_chart(style_chart(fig2), width='stretch')

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("3. Nhiệt độ & Lượt thuê")
    fig3 = px.scatter(df, x='Temperature(°C)', y='Rented Bike Count', color='Seasons',
                      opacity=0.45, category_orders={'Seasons': SEASON_ORDER}, color_discrete_map=SEASON_COLORS,
                      title="Mối liên hệ giữa nhiệt độ và nhu cầu")
    fig3.update_traces(hovertemplate='Nhiệt độ: %{x:.1f}°C<br>Lượt thuê: %{y:,.0f}<extra>%{fullData.name}</extra>')
    fig3.update_xaxes(title='Nhiệt độ (°C)')
    fig3.update_yaxes(title='Lượt thuê trong một giờ')
    st.plotly_chart(style_chart(fig3), width='stretch')

with col_b:
    st.subheader("4. Phân phối lượt thuê theo Mùa")
    fig4 = px.box(df, x='Seasons', y='Rented Bike Count', color='Seasons',
                  points='outliers', category_orders={'Seasons': SEASON_ORDER},
                  color_discrete_map=SEASON_COLORS, title="Phân phối lượt thuê theo mùa")
    fig4.update_traces(hovertemplate='Mùa: %{x}<br>Lượt thuê: %{y:,.0f}<extra></extra>')
    fig4.update_xaxes(title='Mùa')
    fig4.update_yaxes(title='Lượt thuê trong một giờ')
    st.plotly_chart(style_chart(fig4), width='stretch')

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("5. Mức độ Độ ẩm")
    humidity_bins = pd.cut(df['Humidity(%)'], bins=[-1, 20, 40, 60, 80, 100],
                           labels=['0–20%', '21–40%', '41–60%', '61–80%', '81–100%'])
    humidity_avg = (df.assign(humidity_band=humidity_bins)
                    .groupby('humidity_band', observed=False)['Rented Bike Count']
                    .mean().reset_index())
    fig5 = px.bar(humidity_avg, x='humidity_band', y='Rented Bike Count', text_auto='.0f',
                  color_discrete_sequence=['#457B9D'], title="Trung bình lượt thuê theo khoảng độ ẩm")
    fig5.update_traces(hovertemplate='Độ ẩm: %{x}<br>Trung bình: %{y:,.0f} lượt<extra></extra>')
    fig5.update_xaxes(title='Độ ẩm tương đối')
    fig5.update_yaxes(title='Lượt thuê trung bình')
    st.plotly_chart(style_chart(fig5), width='stretch')

with col_b:
    st.subheader("6. Ngày lễ vs Ngày thường")
    holiday_avg = df.groupby('Holiday')['Rented Bike Count'].mean().reset_index()
    fig6 = px.bar(holiday_avg, x='Holiday', y='Rented Bike Count', text_auto='.0f',
                  color='Holiday', color_discrete_map={'Holiday': '#E76F51', 'No Holiday': '#2A9D8F'},
                  title="Trung bình lượt thuê: ngày lễ và ngày thường")
    fig6.update_traces(hovertemplate='%{x}<br>Trung bình: %{y:,.0f} lượt<extra></extra>')
    fig6.update_xaxes(title='Loại ngày')
    fig6.update_yaxes(title='Lượt thuê trung bình')
    st.plotly_chart(style_chart(fig6), width='stretch')

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("7. Ma trận Tương quan Đặc trưng")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    corr = df[numeric_cols].corr()
    fig7 = px.imshow(corr, text_auto=".2f", aspect="auto", color_continuous_scale='RdBu_r',
                     zmin=-1, zmax=1, title="Tương quan Pearson giữa các biến số")
    fig7.update_layout(coloraxis_colorbar_title='r')
    st.plotly_chart(style_chart(fig7), width='stretch')

with col_b:
    st.subheader("8. Phân phối số lượt thuê")
    fig8 = px.histogram(df, x='Rented Bike Count', nbins=40, histnorm='probability density',
                        color_discrete_sequence=['#2A9D8F'], title="Phân phối lượt thuê mỗi giờ")
    mean_rented = df['Rented Bike Count'].mean()
    median_rented = df['Rented Bike Count'].median()
    fig8.add_vline(x=mean_rented, line_dash='dash', line_color='#D1495B')
    fig8.add_vline(x=median_rented, line_dash='dot', line_color='#264653')
    fig8.add_annotation(
        x=mean_rented, y=1, yref='paper', text='Trung bình',
        showarrow=False, xanchor='left', yanchor='bottom', yshift=8,
        font=dict(color='#D1495B', size=11), bgcolor='rgba(255,255,255,0.85)',
    )
    fig8.add_annotation(
        x=median_rented, y=1, yref='paper', text='Trung vị',
        showarrow=False, xanchor='right', yanchor='bottom', yshift=8,
        font=dict(color='#264653', size=11), bgcolor='rgba(255,255,255,0.85)',
    )
    fig8.update_traces(hovertemplate='Khoảng lượt thuê: %{x}<br>Mật độ: %{y:.4f}<extra></extra>')
    fig8.update_layout(xaxis_title='Số lượt thuê trong một giờ', yaxis_title='Mật độ xác suất')
    st.plotly_chart(style_chart(fig8), width='stretch')

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("9. Tác động của Lượng mưa")
    rain_df = df[df['Rainfall(mm)'] > 0]
    fig9 = px.scatter(rain_df, x='Rainfall(mm)', y='Rented Bike Count',
                      opacity=0.55, color_discrete_sequence=['#E76F51'],
                      title="Lượt thuê trong 528 giờ có mưa")
    fig9.update_traces(hovertemplate='Lượng mưa: %{x:.1f} mm<br>Lượt thuê: %{y:,.0f}<extra></extra>')
    fig9.update_xaxes(title='Lượng mưa (mm)')
    fig9.update_yaxes(title='Lượt thuê trong một giờ')
    st.plotly_chart(style_chart(fig9), width='stretch')