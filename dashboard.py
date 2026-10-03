import streamlit as st
import pandas as pd
import numpy as np
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


def weather_scatter(data, column, label, color, unit):
    rentals = data['Rented Bike Count']
    correlation = data[column].corr(rentals)
    x_values = data[column].to_numpy()
    trend_x = np.linspace(x_values.min(), x_values.max(), 100)
    trend_y = np.polyval(np.polyfit(x_values, rentals.to_numpy(), 1), trend_x)

    fig = px.scatter(
        data,
        x=column,
        y='Rented Bike Count',
        opacity=0.35,
        color_discrete_sequence=[color],
        title=f"{label} (r={correlation:.3f})",
    )
    fig.add_scatter(x=trend_x, y=trend_y, mode='lines', line=dict(color=color, width=2),
                    name='Xu hướng', hoverinfo='skip', showlegend=False)
    fig.update_traces(
        selector=dict(type='scatter', mode='markers'),
        marker=dict(size=5),
        hovertemplate=f'{label}: %{{x:.1f}} {unit}<br>Lượt thuê: %{{y:,.0f}}<extra></extra>',
    )
    fig.update_xaxes(title=label)
    fig.update_yaxes(title='Số lượt thuê (lượt/giờ)')
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

hourly_season_avg = df.groupby(['Hour', 'Seasons'])['Rented Bike Count'].mean().reset_index()
fig1 = px.line(hourly_season_avg, x='Hour', y='Rented Bike Count', color='Seasons', markers=True,
               category_orders={'Seasons': SEASON_ORDER}, color_discrete_map=SEASON_COLORS,
               title="Trung bình lượt thuê theo giờ trong ngày")
fig1.update_traces(hovertemplate='Giờ: %{x}:00<br>Trung bình: %{y:,.0f} lượt<extra>%{fullData.name}</extra>')
fig1.update_xaxes(dtick=2, title='Giờ trong ngày')
fig1.update_yaxes(title='Lượt thuê trung bình')

dow_avg = df.groupby('Day of Week')['Rented Bike Count'].mean().reset_index()
fig2 = px.bar(dow_avg, x='Day of Week', y='Rented Bike Count',
              category_orders={'Day of Week': DOW_ORDER}, color_discrete_sequence=['#2A9D8F'],
              text_auto='.0f', title="Trung bình lượt thuê theo ngày")
fig2.update_traces(hovertemplate='%{x}<br>Trung bình: %{y:,.0f} lượt<extra></extra>')
fig2.update_xaxes(title='Ngày trong tuần', tickangle=-25)
fig2.update_yaxes(title='Lượt thuê trung bình')

fig3 = weather_scatter(df, 'Temperature(°C)', 'Nhiệt độ (°C)', '#E53935', '°C')

fig4 = px.box(df, x='Seasons', y='Rented Bike Count', color='Seasons',
              points='outliers', category_orders={'Seasons': SEASON_ORDER},
              color_discrete_map=SEASON_COLORS, title="Phân phối lượt thuê theo mùa")
fig4.update_traces(hovertemplate='Mùa: %{x}<br>Lượt thuê: %{y:,.0f}<extra></extra>')
fig4.update_xaxes(title='Mùa')
fig4.update_yaxes(title='Lượt thuê trong một giờ')

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

holiday_avg = df.groupby('Holiday')['Rented Bike Count'].mean().reset_index()
fig6 = px.bar(holiday_avg, x='Holiday', y='Rented Bike Count', text_auto='.0f',
              color='Holiday', color_discrete_map={'Holiday': '#E76F51', 'No Holiday': '#2A9D8F'},
              title="Trung bình lượt thuê: ngày lễ và ngày thường")
fig6.update_traces(hovertemplate='%{x}<br>Trung bình: %{y:,.0f} lượt<extra></extra>')
fig6.update_xaxes(title='Loại ngày')
fig6.update_yaxes(title='Lượt thuê trung bình')

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
corr = df[numeric_cols].corr()
fig7 = px.imshow(corr, text_auto=".2f", aspect="auto", color_continuous_scale='RdBu_r',
                 zmin=-1, zmax=1, title="Tương quan Pearson giữa các biến số")
fig7.update_layout(coloraxis_colorbar_title='r')

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

rain_df = df[df['Rainfall(mm)'] > 0]
fig9 = px.scatter(rain_df, x='Rainfall(mm)', y='Rented Bike Count',
                  opacity=0.55, color_discrete_sequence=['#E76F51'],
                  title="Lượt thuê trong 528 giờ có mưa")
fig9.update_traces(hovertemplate='Lượng mưa: %{x:.1f} mm<br>Lượt thuê: %{y:,.0f}<extra></extra>')
fig9.update_xaxes(title='Lượng mưa (mm)')
fig9.update_yaxes(title='Lượt thuê trong một giờ')

fig10 = weather_scatter(df, 'Humidity(%)', 'Độ ẩm (%)', '#2837D9', '%')
fig11 = weather_scatter(df, 'Visibility (10m)', 'Tầm nhìn (10m)', '#138D24', '10m')
fig12 = weather_scatter(
    df, 'Solar Radiation (MJ/m2)', 'Bức xạ mặt trời (MJ/m²)', '#F39C12', 'MJ/m²'
)
fig13 = weather_scatter(df, 'Wind speed (m/s)', 'Tốc độ gió (m/s)', '#A93226', 'm/s')

rainfall_bins = pd.cut(
    df['Rainfall(mm)'],
    bins=[-np.inf, 0, 2.5, 5, 10, np.inf],
    labels=['Không mưa', '0–2.5mm', '2.5–5mm', '5–10mm', '>10mm'],
    ordered=True,
)
rainfall_avg = (
    df.assign(rainfall_band=rainfall_bins)
    .groupby('rainfall_band', observed=False)['Rented Bike Count']
    .mean()
    .reset_index()
)
fig14 = px.bar(
    rainfall_avg,
    x='rainfall_band',
    y='Rented Bike Count',
    color='rainfall_band',
    color_discrete_sequence=['green', 'lightblue', 'blue', 'navy', 'purple'],
    title='Nhu cầu theo lượng mưa',
)
fig14.update_traces(
    hovertemplate='Lượng mưa: %{x}<br>Trung bình: %{y:,.0f} lượt/giờ<extra></extra>'
)
fig14.update_xaxes(title='Lượng mưa', tickangle=-25)
fig14.update_yaxes(title='Trung bình nhu cầu (lượt/giờ)')

# Thay đổi thứ tự trong danh sách này để di chuyển biểu đồ trên dashboard.
charts = [
    ("Xu hướng Nhu cầu Hàng giờ theo Mùa", fig1),
    ("Nhu cầu theo Ngày trong Tuần", fig2),
    ("Nhiệt độ & Lượt thuê", fig3),
    ("Phân phối lượt thuê theo Mùa", fig4),
    ("Mức độ Độ ẩm", fig5),
    ("Ngày lễ vs Ngày thường", fig6),
    ("Ma trận Tương quan Đặc trưng", fig7),
    ("Phân phối số lượt thuê", fig8),
    ("Tác động của Lượng mưa", fig9),
    ("Độ ẩm & Nhu cầu thuê", fig10),
    
    ("Nhu cầu theo lượng mưa", fig14),
    ("Tầm nhìn & Nhu cầu thuê", fig11),
    ("Bức xạ mặt trời & Nhu cầu thuê", fig12),
    ("Tốc độ gió & Nhu cầu thuê", fig13),
]

for row_start in range(0, len(charts), 2):
    columns = st.columns(2)
    for column, (title, figure) in zip(columns, charts[row_start:row_start + 2]):
        with column:
            st.subheader(str(row_start + 1) +  ". " + title)
            st.plotly_chart(style_chart(figure), width='stretch')