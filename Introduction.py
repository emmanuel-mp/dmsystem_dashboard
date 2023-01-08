# -*- coding: utf-8 -*-
"""
CHALLENGE BASE MODULE
PROJECT LOAD MANAGEMENT SYSTEM
DASHBOARD OF THE PROPOSED SYSTEM
JANUARY 2023
EMMANUEL AF MOMPREMIER
"""


import pandas as pd
import streamlit as st
from PIL import Image



st.set_page_config(page_title='DMSystem',
                   page_icon=":tractor:",
                   layout='wide')


st.title("DMSystems")




dms_logo = Image.open('./images/projectLogo.png')

#create empty columns to center the logo
col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.image(dms_logo, width = 500)

with col3:
    st.write("")


st.write('This project involves the design of a fast-response demand-management system capable of coping with unexpected reductions in power generation availability to ensure reliability and guard against unexpected power outages.')


st.markdown("""---""")


st.write('DMSystems can deliver on the technical requirement of responding to an electrical fault – observed through a reduction in grid frequency below the desired threshold – within the desired roundtrip response time of 10 milliseconds.')
st.write('The fundamental utility of this system lies in its ability to delay the onset of imminent blackouts to the entire plant due to the loss of power generation, by disconnecting low priority load groups to maintain system frequency.')
    

electric_diagram = Image.open('./images/line_diagram.png')

#create empty columns to center the image
col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.image(electric_diagram, width = 700, caption = 'Single line diagram depicting electrical setup of plant')

with col3:
    st.write("")



st.write('The disconnection commands will reach the circuit breakers on the load side via the proposed communication network involving fiber optic cables and TCP/IP protocol.')

network_diagram = Image.open('./images/communication_network.png')

#create empty columns to center the image
col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")
 
with col2:
    st.image(network_diagram, width = 600, caption = 'Proposed communication network to trasmit the load shedding commands')

with col3:
    st.write("")



