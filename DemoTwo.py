import streamlit as st 

st.title('Linear Regression Web App')

st.write("""
# Simply use this web app to predict your dataset here
""")

choice = st.sidebar.radio(
    "Choose a dataset",   
    ('Default', 'User-defined '),
    index = 0
    
)

st.write(f"## You Have Selected <font color='Aquamarine'>{choice}</font> Dataset", unsafe_allow_html=True)

