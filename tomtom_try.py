import streamlit as st
import pandas as pd
import numpy as np
import json
from pprint import pprint

print('ciao')

with open('./tomtom response.txt') as f:
    data = json.load(f)

pprint(data)

# Create the pandas DataFrame 
df = pd.DataFrame(data['flowSegmentData']['coordinates']['coordinate'], columns=['latitude', 'longitude'])
# initialize list of lists 
# data = [['tom', 10], ['nick', 15], ['juli', 14]]

# Create the pandas DataFrame 
# df = pd.DataFrame(data, columns = ['Name', 'Age'])
st.write(df)
# print dataframe. 
st.deck_gl_chart(layers=[{
    'data': df,
    'type': 'ScatterplotLayer'
}])

# first leg of google asnwer
# #note that there can b emultiple routes ... 
# j['routes'][0]
