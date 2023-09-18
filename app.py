import pandas as pd
import streamlit as st
import streamlit.components.v1 as stc # streamlit 機能を拡張
import openpyxl
import pygwalker as pyg

# pip install pandas streamlit openpyxl pygwalker

st.set_page_config(page_title='PyGWalker', layout='wide')
st.title('PyGWalker')

#encoding設定
selected_encoding = st.selectbox(
    'encodingを選択', 
    ['utf-8', 'shift_jis', 'cp932'],
    key='encoding')

uploaded_file = st.file_uploader('files of csv', type='csv')

if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding=selected_encoding)
    
    # # PyGWalkerを使用してHTMLに変換 return_html=Trueとすることで、HTML形式の文字列
    pyg_html = pyg.walk(df, return_html=True)
    ## 生成したHTMLをStreamlitアプリケーションに埋め込む
    stc.html(pyg_html, scrolling=True, height=1000) #CSS pixels
