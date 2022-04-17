from config import config
from get_data import get_data
import time
import streamlit as st
import plotly.graph_objects as go

time_list = []
temp_list = []
pres_list = []
humi_list = []
alti_list = []

st.set_page_config(layout="wide")
st.title("Vrijeme RITEH")
st.header("Trenutno stanje")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)

fig_temp = go.Figure()
fig_temp.update_layout(title="Temperatura", xaxis_title="Vrijeme", yaxis_title="Temperatura °C")
fig_pres = go.Figure()
fig_pres.update_layout(title="Tlak", xaxis_title="Vrijeme", yaxis_title="Tlak hPa")
fig_humi = go.Figure()
fig_humi.update_layout(title="Vlažnost", xaxis_title="Vrijeme", yaxis_title="Vlažnost %")
fig_alti = go.Figure()
fig_alti.update_layout(title="Nadmorska visina", xaxis_title="Vrijeme", yaxis_title="Visina m")
fig_temp.add_trace(go.Scatter(x=time_list, y=temp_list))
fig_pres.add_trace(go.Scatter(x=time_list, y=pres_list))
fig_humi.add_trace(go.Scatter(x=time_list, y=humi_list))
fig_alti.add_trace(go.Scatter(x=time_list, y=alti_list))

data_list = get_data(12)
for data in data_list:
    temp_list.insert(0, data[1])
    pres_list.insert(0, data[2])
    humi_list.insert(0, data[3])
    alti_list.insert(0, data[4])
    time_list.insert(0, data[5])
    
last_temp = "{} °C".format(temp_list[-1])
last_pres = "{} hPa".format(pres_list[-1])
last_humi = "{} %".format(humi_list[-1])
last_alti = "{} m".format(alti_list[-1])
delta_temp = "{} °C".format(round(temp_list[-1]-temp_list[-2], 2))
delta_pres = "{} hPa".format(round(pres_list[-1]-pres_list[-2], 2))
delta_humi = "{} %".format(round(humi_list[-1]-humi_list[-2], 2))
delta_alti = "{} m".format(round(alti_list[-1]-alti_list[-2], 2))

fig_temp = go.Figure()
fig_temp.update_layout(title="Temperatura", xaxis_title="Vrijeme", yaxis_title="Temperatura °C")
fig_pres = go.Figure()
fig_pres.update_layout(title="Tlak", xaxis_title="Vrijeme", yaxis_title="Tlak hPa")
fig_humi = go.Figure()
fig_humi.update_layout(title="Vlažnost", xaxis_title="Vrijeme", yaxis_title="Vlažnost %")
fig_alti = go.Figure()
fig_alti.update_layout(title="Nadmorska visina", xaxis_title="Vrijeme", yaxis_title="Visina m")
fig_temp.add_trace(go.Scatter(x=time_list, y=temp_list))
fig_pres.add_trace(go.Scatter(x=time_list, y=pres_list))
fig_humi.add_trace(go.Scatter(x=time_list, y=humi_list))
fig_alti.add_trace(go.Scatter(x=time_list, y=alti_list))

col1, col2, col3, col4 = st.columns(4)
col1.metric("Temperatura", last_temp, delta_temp)
col2.metric("Tlak", last_pres, delta_pres)
col3.metric("Vlažnost", last_humi, delta_humi)
col4.metric("Nadmorska visina", last_alti, delta_alti)

col5, col6 = st.columns(2)
col5.plotly_chart(fig_temp, use_container_width=True)
col5.plotly_chart(fig_pres, use_container_width=True)
col6.plotly_chart(fig_humi, use_container_width=True)
col6.plotly_chart(fig_alti, use_container_width=True)
time.sleep(10)
st.experimental_rerun()
    