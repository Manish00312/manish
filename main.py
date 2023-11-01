import pandas as pd
import datetime
import xgboost as xb
import streamlit as st
def main():
    html_temp="""
      <h1>car price
       prediction</h1>
       """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.markdown("this app will help you to predict car selling price ")
    p1=st.number_input("please enter ex showroom price(in lakhs) ",2.5,25.0,step=1.0)
    p2=st.number_input("please enter car driven (in kilometers)",100,5000,step=100)

if __name__=='__main__':
    main()



