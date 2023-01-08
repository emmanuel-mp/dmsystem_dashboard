# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 22:07:44 2023
@author: EMMNAUEL AF MOMPREMIER
"""


import streamlit as st
import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
from PIL import Image



st.header('Key Features of the Grid on August 1, 2021')
st.markdown("""---""")


df = pd.read_excel('Mining1.xls')
df = df[['Date','Time', 'Controller', 'Reason', 'Pwr','Gfrq', 'Bfrq', 'Ig1', 'Ig2', 'Ig3']].copy()

df['Date'] = "2021-08-01"
df['Time'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])




#------SIDEBAR--------

generator = st.sidebar.multiselect('Select one or several controllers:',
                                   options=df['Controller'].unique(),default=df['Controller'].unique())



notification = st.sidebar.multiselect('Select one or several alarms from the ComAp controllers:',
                                   options=df['Reason'].unique())#,default=df['Reason'].unique())
  

df_selection = df.query(
    "Reason == @notification & Controller == @generator")

df_plot = df.query("Controller == @generator")
df_plot.sort_values(by='Time', inplace=True)
                                   






#------MAINPAGE--------

# creating a single-element container.
placeholder = st.empty()


#change the fontsize of the metric values
st.markdown(
    """
<style>
[data-testid="stMetricValue"] {
    font-size: 20px;
}
</style>
""",
    unsafe_allow_html=True,
)


with placeholder.container():
    # create three columns
    kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns([0.9,0.9,1,1.1,1.1])

    # fill in those three columns with respective metrics or KPIs 
    kpi1.metric(label="Active Generators", value= 6)
    kpi2.metric(label="Active Loads", value= 7)
    kpi3.metric(label="Disconnected Loads", value= 2)
    kpi4.metric(label="Time of First Fault", value= '16:59:59.3')
    kpi5.metric(label="First Generator to Trip", value= 'C01 - SGB 1603')


st.markdown("""---""")




st.subheader('1. Variations in the Electrical Parameters')

st.markdown("##### Active Power")
fig1 = px.line(data_frame=df_plot, y = 'Pwr', x = 'Time', color = 'Controller')
fig1.update_layout(template="simple_white")
st.write(fig1)

st.markdown("##### Grid Frequency")
fig2 = px.line(data_frame=df_plot, y = 'Gfrq', x = 'Time', color = 'Controller')
fig2.update_layout(template="simple_white")
st.write(fig2)

st.markdown("##### Generator Frequency")
fig3 = px.line(data_frame = df_plot, y = 'Bfrq', x = 'Time', color = 'Controller')
fig3.update_layout(template="simple_white")
st.write(fig3)



st.markdown("""---""")





st.subheader('2. Variations in the Load Status After Shedding')


load_names = ['Tunnel Feeder', 'Secondary 1', 'Secondary 2', 'Camp & Worsh.','Primary 2', 'Primary 1', 'Primary 3']
load_rated_power = [50, 1653, 234, 400, 434, 362, 419]
load_adjusted_consumption = [26, 827, 117, 200, 217, 181, 210]


load_names_disconnected = ['Tunnel Feeder', 'Secondary 1']
load_shed = [26, 827]

load_names_connected = ['Secondary 2', 'Camp & Worsh.','Primary 2', 'Primary 1', 'Primary 3']
load_connected = [117, 200, 217, 181, 210]




st.markdown("##### Consumption of Different Loads Under No-Fault Condition")


fig4 = go.Figure()
fig4.add_trace(go.Bar(
    y=load_names,
    x=load_rated_power,
    name='Rated Power [kW]',
    orientation='h',
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=1)
    )
))
fig4.add_trace(go.Bar(
    y=load_names,
    x=load_adjusted_consumption,
    name='Adjusted Consumption [kW]',
    orientation='h',
    marker=dict(
        color='rgba(95, 193, 99, 0.8)', 
        line=dict(color='rgba(75, 176, 80, 1.0)', width=1)
    )
))

fig4.update_layout(template="simple_white")
st.write(fig4)




st.markdown("##### Consumption of the Loads After Fast Shedding")


fig5 = go.Figure()
fig5.add_trace(go.Bar(
    y=load_names,
    x=load_rated_power,
    name='Rated Power [kW]',
    orientation='h',
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=1)
    )
))


fig5.add_trace(go.Bar(
    y=load_names_connected,
    x=load_connected,
    name='Power Consumed After Shedding [kW]',
    orientation='h',
    marker=dict(
        color='rgba(95, 193, 99, 0.8)', 
        line=dict(color='rgba(75, 176, 80, 1.0)', width=1)
    )
))


fig5.add_trace(go.Bar(
    y=load_names_disconnected,
    x=load_shed,
    name='Power Shed [kW]',
    orientation='h',
    marker=dict(
        color='rgba(205, 43, 7, 0.8)', 
        line=dict(color='rgba(205, 43, 7, 0.8)', width=1)
    )
))

fig5.update_layout(template="simple_white")
st.write(fig5)





st.markdown("##### Comparisons: Power Generated Prior to Fault, Power Lost, Power Shed")


colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']
labels = ['Power Generated Prior to Fault [kW]', 'Power Lost [kW]']
values = [1778, 506]

power_generated_prior_fault = 1778
power_lost = 506
power_shed = 852.458


fig6 = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig6.update_traces(hoverinfo='label', textinfo='value', textfont_size=20,
              marker=dict(colors=colors, line=dict(color='#000000', width=2)))
st.write(fig6)


abscissa = ['Power [kW]']    
fig7 = go.Figure(data=[
    go.Bar(name = 'Power Lost [kW]', x = abscissa, y=[506], text = [506], textposition = 'auto'),
    go.Bar(name = 'Power Shed [kW]', x = abscissa, y=[852.458], text = [852.458], textposition = 'auto')])

st.write(fig7)



st.markdown("""---""")



st.subheader('3. Validation of the Load Shedding Strategy Using Simulink')

frequency_simulink = Image.open('frequency.png')

#create empty columns to center the image
col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.image(frequency_simulink, width = 500, caption = 'Without Load-Shedding, the system frequency decreases (orange line). \n With Fast Load-Shedding, the system frequency increases (blue line) because the load shed in this case is higher than the generation capacity lost. ')

with col3:
    st.write("")





st.markdown("""---""")



st.subheader("4. Detailed Data Overview")
del df_selection['Date']
st.table(df_selection)