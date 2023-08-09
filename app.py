# ====================================================================
# Chargement des librairies
# ===================================================================
import streamlit as st
from PIL import Image
import os
from streamlit_option_menu import option_menu


# ====================================================================
# HEADER - TITRE
# ====================================================================
html_header="""
    <head>
        <title>Application Dashboard Crédit Score</title>
        <meta charset="utf-8">
        <meta name="keywords" content="Home Crédit Group, Dashboard, prêt, crédit score">
        <meta name="description" content="Application de Crédit Score - dashboard">
        <meta name="author" content="Loetitia Rabier">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>             
    <h1 style="font-size:300%; color:Crimson; font-family:Arial"> AI TOOL FOR FLECHTECK <br>
        <h2 style="color:Gray; font-family:Georgia"> DASHBOARD</h2>
        <hr style= "  display: block;
          margin-top: 0;
          margin-bottom: 0;
          margin-left: auto;
          margin-right: auto;
          border-style: inset;
          border-width: 1.5px;"/>
     </h1>
"""
# Logo de l'entreprise
logo_path = 'exemple_image/logo1.jpeg'
if os.path.exists(logo_path):
    logo_image = Image.open(logo_path)
    st.sidebar.image(logo_image, width=300)
#st.set_page_config(page_title="Prêt à dépenser - Dashboard", page_icon="", layout="wide")
st.markdown('<style>body{background-color: #fbfff0}</style>',unsafe_allow_html=True)
st.markdown(html_header, unsafe_allow_html=True)





# 1. as sidebar menu
with st.sidebar:
    sidebar_selection = option_menu(" Menu", ['Home','URL','pdf2_image','Layout parser','Extract Table','Question Answering','footprint','Chatboot','Upload json file','Settings','contact' ], 
        icons=['house','file-earmark-pdf-fill','bi bi-file-earmark-image','bi bi-columns-gap','table','bi bi-patch-question-fill','bi bi-app','bi bi-chat-left-dots-fill','bi bi-filetype-json','gear','bi bi-person-lines-fill'], menu_icon="cast", default_index=1)
    sidebar_selection





if sidebar_selection == 'Home':
    video_file = open('exemple_image/Flechtec.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
