# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 19:41:25 2026

@author: MSI-1
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models
diabetes_model = pickle.load(open('trained_diabetes_prediction_model.sav','rb'))
heart_disease_model = pickle.load(open('trained_heart_disease_prediction_model.sav','rb'))
breast_cancer_model = pickle.load(open('trained_breast_cancer_prediction_model.sav','rb'))
parkinsons_model = pickle.load(open('trained_parkinson_disease_prediction_model.sav','rb'))

#sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System (Developer : DHRUV R. CHANDEL)',
                           ['Diabetes Prediction System',
                            'Heart Disease Prediction System',
                            'Breast Cancer Prediction System',
                            "Parkinson's Disease Prediction System"],
                           icons=['activity','heart','gender-female','person'],
                           default_index = 0)
#Prediction Page
if (selected == 'Diabetes Prediction System'):
    #page title
    st.title('Diabetes Prediction using ML')
    #columns with input fields
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:    
        Glucose = st.text_input('Glucose Level')
    with col3:    
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:    
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:    
        Insulin = st.text_input('Insulin Level')
    with col3:    
        BMI = st.text_input('BMI Value')
    with col1:    
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:    
        Age = st.text_input('Age of the Person')
    
    #code for prediction
    diab_diagnosis = ''
    #creating a button
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0]==1):
            diab_diagnosis = 'The person is Diabetic'
            
        else:
            diab_diagnosis = 'The person is Not Diabetic'
        
    st.success(diab_diagnosis)
    
    
    
if (selected == 'Heart Disease Prediction System'):
    #page title
    st.title('Heart Disease Prediction using ML')
    #columns with input fields
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        age = st.text_input('Age of the Person')
    with col2:    
        sex = st.text_input('Sex of the Person')
    with col3:    
        cp = st.text_input('Chest Pain Types')
    with col4:    
        trestbps = st.text_input('Resting Blood Pressure Value')
    with col1:    
        chol = st.text_input('Serum Cholestrol in mg/dL')
    with col2:    
        fbs = st.text_input('Fasting Blood Pressure > 120 mg/dl')
    with col3:    
        restecg = st.text_input('Resting Electrocardiographic Result')
    with col4:    
        thalach = st.text_input('Maximum Heart Rate Received')
    with col1:    
        exang = st.text_input('Exercise Induced Angina')
    with col2:    
        oldpeak = st.text_input('ST Depression Induced by Exercise')
    with col3:    
        slope = st.text_input('Slope of the peak Exercise ST Segment')
    with col4:    
        ca = st.text_input('Major vessels coloured by Fluoroscopy')
    with col1:    
        thal = st.text_input('thal: 0=Normal; 1=Fixed Defect; 2=Reversible Defect')
        
    
    #code for prediction
    heart_diagnosis = ''
    #creating a button
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, thal]])
        
        if (heart_prediction[0]==1):
            heart_diagnosis = 'The person does have a Heart Disease'
            
        else:
            heart_diagnosis = 'The person does Not have a Heart Disease'
        
    st.success(heart_diagnosis)



if (selected == 'Breast Cancer Prediction System'):
    #page title
    st.title('Breast Cancer Prediction using ML')
    #columns with input fields
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        mean_radius = st.text_input('Radius of Lobes')
    with col2:    
        mean_texture = st.text_input('Mean of Texture Surface')
    with col3:    
        mean_perimeter = st.text_input('Outer Perimeter of Lobes')
    with col4:    
        mean_area = st.text_input('Mean Area of Lobes')
    with col5:    
        mean_smoothness = st.text_input('Mean of Smoothness Levels')
    with col1:    
        mean_compactness = st.text_input('Mean of Compactness')
    with col2:    
        mean_concavity = st.text_input('Mean of Concavity')
    with col3:    
        mean_concave_points = st.text_input('Mean of Concave Points')
    with col4:    
        mean_symmetry = st.text_input('Mean of Symmetry')
    with col5:    
        mean_fractal_dimension = st.text_input('Mean of Fractal Dimension')
    with col1:    
        radius_error = st.text_input('Error in Radius')
    with col2:    
        texture_error = st.text_input('Error in Texture')
    with col3:    
        perimeter_error = st.text_input('Error in Perimeter')
    with col4:
        area_error = st.text_input('Error in Area')
    with col5:    
        smoothness_error = st.text_input('Error in Smoothness')
    with col1:    
        compactness_error = st.text_input('Error in Compactness')
    with col2:    
        concavity_error = st.text_input('Error in Concavity')
    with col3:    
        concave_points_error = st.text_input('Error in Concave Points')
    with col4:    
        symmetry_error = st.text_input('Error in Symmetry')
    with col5:    
        fractal_dimension_error = st.text_input('Fractal Dimension Error')
    with col1:    
        worst_radius = st.text_input('Worst Radius')
    with col2:    
        worst_texture = st.text_input('Worst Texture')
    with col3:    
        worst_perimeter = st.text_input('Worst Perimeter')
    with col4:    
        worst_area = st.text_input('Worst Area')
    with col5:    
        worst_smoothness = st.text_input('Worst Smoothness')
    with col1:    
        worst_compactness = st.text_input('Worst Compactness')
    with col2:    
        worst_concavity = st.text_input('Worst Concavity')
    with col3:    
        worst_concave_points = st.text_input('Worst Concave Points')
    with col4:    
        worst_symmetry = st.text_input('Worst Symmetry')
    with col5:    
        worst_fractal_dimension = st.text_input('Worst Fractal Dimension')
        
    
    #code for prediction
    breast_diagnosis = ''
    #creating a button
    if st.button('Breast Cancer Test Result'):
        breast_prediction = breast_cancer_model.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,symmetry_error,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,worst_fractal_dimension]])
        
        if (breast_prediction[0]==1):
            breast_diagnosis = 'The person does have Breast Cancer'
            
        else:
            breast_diagnosis = 'The person does Not have Breat Cancer'
        
    st.success(breast_diagnosis)

    
    
if (selected == "Parkinson's Disease Prediction System"):
    #page title
    st.title("Parkinson's Disease Prediction using ML")
    #columns with input fields
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        fo = st.text_input('MDVP : Fo(Hz)')
    with col2:    
        fhi = st.text_input('MDVP : Fhi(Hz)')
    with col3:    
        flo = st.text_input('MDVP : Flo(Hz)')
    with col4:    
        Jitter_percent = st.text_input('MDVP : Jitter(%)')
    with col1:    
        Jitter_abs = st.text_input('MDVP : Jitter(Abs)')
    with col2:    
        RAP = st.text_input('MDVP : RAP')
    with col3:    
        PPQ = st.text_input('MDVP : PPQ')
    with col4:    
        DDP = st.text_input('Jitter : DDP')
    with col1:    
        Shimmer = st.text_input('MDVP : Shimmer')
    with col2:    
        Shimmer_dB = st.text_input('MDVP : Shimmer(dB)')
    with col3:    
        APQ3 = st.text_input('Shimmer : APQ3')
    with col4:    
        APQ5 = st.text_input('Shimmer : APQ5')
    with col1:    
        APQ = st.text_input('MDVP : APQ')
    with col2:    
        DDA = st.text_input('Shimmer : DDA')
    with col3:    
        NHR = st.text_input('NHR')
    with col4:    
        HNR = st.text_input('HNR')
    with col1:    
        RPDE = st.text_input('RPDE')
    with col2:    
        DFA = st.text_input('DFA')
    with col3:    
        spread_1 = st.text_input('Spread 1')
    with col4:    
        spread_2 = st.text_input('Spread 2')
    with col1:    
        D2 = st.text_input('D2')
    with col2:    
        PPE = st.text_input('PPE')
    
    #code for prediction
    park_diagnosis = ''
    #creating a button
    if st.button("Parkinson's Test Result"):
        park_prediction = parkinsons_model.predict([[fo,fhi,flo,Jitter_percent,Jitter_abs,RAP,PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread_1,spread_2,D2,PPE]])
        
        if (park_prediction[0]==1):
            park_diagnosis = 'The person is Diabetic'
            
        else:
            park_diagnosis = 'The person is Not Diabetic'
        
    st.success(park_diagnosis)
    