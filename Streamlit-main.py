import pandas as pd
import numpy as np
import streamlit as st

st.write("Table time")
st.write(pd.DataFrame({
    'first column' : [1, 2, 3, 4],
    'second column' : [10, 20, 30, 40],
}))

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['A','B','C'])

st.line_chart(chart_data)