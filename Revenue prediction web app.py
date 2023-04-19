"""19-04-2023
Author @Arnav Saini"""

import pickle
import streamlit as st
import numpy as np


trained_model=pickle.load(open("D:\Learnbay notes\Machine Learning\Learnbay__interview_project_1\Trained_model.sav",'rb'))


def prediction(input):
    result=trained_model.predict(np.array(input).reshape(1,-1))
    if result==1:
        return 'Customer will generate Revenue'
    else:
        return 'Customer will not generate Revenue'

def main():

    st.title('Supply Chain management for a FMCG company')
    st.header('Predicting weight in tons to be stored in Warehouse')

    Administrative = st.text_input('Administrative')
    Administrative_Duration = st.text_input('Administrative_Duration')
    Informational = st.text_input('Informational')
    Informational_Duration = st.text_input('Informational_Duration')
    ProductRelated = st.text_input('ProductRelated')
    ProductRelated_Duration = st.text_input('ProductRelated_Duration')
    BounceRates = st.text_input('BounceRates in %')
    ExitRates = st.text_input('ExitRates in %')
    PageValues = st.text_input('PageValues')
    SpecialDay = st.text_input('SpecialDay')
    Month = st.text_input('Month')
    OperatingSystems = st.text_input('OperatingSystems')
    Browser = st.text_input('Browser')
    Region = st.text_input('Region')
    TrafficType = st.text_input('TrafficType')
    VisitorType = st.selectbox('VisitorType', ['Returning visitor', 'New visitor'])
    if VisitorType == 'Returning visitor':
        VisitorType = 1
    else:
        VisitorType = 0

    Weekend = st.selectbox('Weekend', ['Urban', 'Rural'])
    if Weekend == 'Urban':
        Weekend = 0
    else:
        Weekend = 1



    Final_result = ''

    # creating a button for prediction
    if st.button('Prediction Result'):
        Final_result=prediction([Administrative, Administrative_Duration, Informational,
       Informational_Duration, ProductRelated, ProductRelated_Duration,
       BounceRates, ExitRates, PageValues,
       SpecialDay,Month, OperatingSystems, Browser,
       Region, TrafficType, VisitorType, Weekend])

    st.success(Final_result)

if __name__=='__main__':
    main()

