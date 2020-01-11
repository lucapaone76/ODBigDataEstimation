import streamlit as st
import pandas as pd
import numpy as np
import google_polylines_code_decode

print('cioa')
points = google_polylines_code_decode.decode("e`miGhmocNs@Rm@N]JmA^KBcAXQDUFg@JMD]Le@Xc@H")
#st.write(points)
# Create the pandas DataFrame 
df = pd.DataFrame(points, columns = ['lon', 'lat']) 
# initialize list of lists 
#data = [['tom', 10], ['nick', 15], ['juli', 14]] 
  
# Create the pandas DataFrame 
#df = pd.DataFrame(data, columns = ['Name', 'Age']) 
  
# print dataframe. 
st.deck_gl_chart(layers = [{
        'data': df,
        'type': 'ScatterplotLayer'
    }])

#first leg of google asnwer
# #note that there can b emultiple routes ... 
#j['routes'][0]