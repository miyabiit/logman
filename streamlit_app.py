import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("please upload access log file")

if uploaded_file is not None:
    df = pd.read_csv(
            uploaded_file,
            sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
            engine='python',
            na_values='-',
            header=None
            )
    st.markdown('### access log (head 5lines)')
    st.write(df.head(5))
