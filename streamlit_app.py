import streamlit as st
import pandas as pd

if upload_file is not None:
    df = pd.read_csv(
            upload_file,
            sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
            engine='python',
            na_values='_',
            header=None
            )
    st.markdown('### access log (head 5lines)')
    st.write(df.head(5))
