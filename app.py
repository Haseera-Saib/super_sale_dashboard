import streamlit as st
import pandas as pd

data=pd.read_csv('/workspaces/super_sale_dashboard/mentornow/superSales.csv')
#st.write(data)
st.header('Super Store DATA')
a=data['Product_line'].unique()
s= st.sidebar.selectbox("Product Name",(a))
st.write('Top Stats')    

c=st.container(border=True)

c1,c2,c3=c.columns(3)

b=data[data['Product_line']==s]
c1.metric(label='Total Invoice', value=b['Invoice_ID'].size)

c2.metric(label='Average Rating', value=round(b['Rating'].mean(), 2))