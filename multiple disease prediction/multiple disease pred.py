# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 11:59:54 2024

@author: venka
"""
import os

import pickle
import streamlit as st
from streamlit_option_menu import option_menu   


# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")


# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))



#loading the saved models

diabetes_model=pickle.load(open('C:/Users/venka/multiple disease prediction/models/trained_model.sav','rb'))
heart_disease_model=pickle.load(open('C:/Users/venka/multiple disease prediction/models/Heart_model.sav','rb'))
#parkinsons_disease_model=pickle.load(open('C:/Users/venka/multiple disease prediction\models/parkinsons_model.sav','rb'))
#breastCancer_model=pickle.load(open('C:/Users/venka/multiple disease prediction/models/breastCancer_model.sav','rb'))
#Migraine_model=pickle.load(open('C:/Users/venka/multiple disease prediction/models/migraine.sav','rb'))
#sidebar for navigate
with st.sidebar:
    selected=option_menu('Multiple Disease prediction System using ML',['HomePage','Diabetes prediction','Heart disease prediction'
                                                               ,'Breast_Cancer_Prediction'],
                         menu_icon='hospital-fill',
                         icons=['person','person','activity', 'heart'],default_index=0)
    

      
     # Set the background image
if (selected == 'HomePage'):
    st.title('Welcome EVERYONE ')
    
   
    
    st.image('C:/Users/venka/multiple disease prediction/wallpaper.jpg', caption='ML Doctor',width=650)

    st.info('MACHINE LEARNING Doctor is a advance as well as most accurate predictor for most of the diseases in  just few seconds where presence of doctor is not necessary.')
     
    st.info('EveryOne and at Anytime and not to wait for all queue for checkup result is needed just result output  and YOUR PREDICTION can be Calculated in few minutes')
   
    st.success('your are welcomed')



    # Diabetes Prediction Page
if (selected == 'Diabetes prediction'):

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

        st.success(diab_diagnosis)

# Heart Disease Prediction Page
if (selected == 'Heart disease prediction'):

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)



           


           
if (selected == 'Breast_Cancer_Prediction'):

        # page title
        st.title('BreastCancer Prediction using ML')
        col1, col2, col3 = st.columns(3)

        with col1:
            meanradius = st.text_input('mean radius')

        with col2:
            meantexture = st.text_input('mean texture')

        with col3:
            meanperimeter = st.text_input('mean perimeter')

        with col1:
            meanarea = st.text_input('mean area')

        with col2:
            meansmoothness = st.text_input('mean smoothness')

        with col3:
            meancompactness = st.text_input('mean compactness')

        with col1:
            meanconcavity = st.text_input('mean cocavity')

        with col2:
            meanconcavepoints = st.text_input('mean concave points')

        with col3:
            meansymmetry = st.text_input('mean symmetry')
        
        with col1:
            meanfractaldimension = st.text_input('mean fractal dimension')
            
        with col2:
            radiuserror = st.text_input('radius error') 
            
        with col3:
            textureerror = st.text_input('texture error')
               
        with col3:
            perimetererror= st.text_input('perimeter error')

 
        with col1:
            areaerror = st.text_input('area error')
            
        with col2:
            smoothnesserror= st.text_input('smoothness error') 
            
        with col3:
            compactnesserror= st.text_input('compactness error')
    
        with col1:
            concavityerror = st.text_input('concavity error')
            
        with col2:
            concavepointserror = st.text_input('concave points erro') 
            
        with col3:
            symmetryerror= st.text_input('symmetry error')
              
        with col1:
            fractaldimensionerror = st.text_input('fractual dimension error')
                
        with col2:
            worstradius= st.text_input('worst radius') 
                
        with col3:
             worsttexture= st.text_input('worst texture')
        with col1:
             worstperimeter = st.text_input('worst perimeter')
                         
        with col2:
             worstarea = st.text_input('worst area') 
                 
        with col3:
             worstsmoothness= st.text_input('worst smoothness')
        with col1:
             worstcompactness = st.text_input('worst compactness')
                 
        with col2:
             worstconcavity= st.text_input('worst concavity') 
                 
        with col3:
              worstconcavepoints= st.text_input('worst concave points')
        with col1:
            worstsymmetry = st.text_input('worst symmetry')
                      
        with col2:
          worstfractaldimension= st.text_input('worst fractal dimension') 
                       
        with col1:
          label= st.text_input('label')
              
        breastcancer_diagnosis = ''

         # creating a button for Prediction
        if st.button('Breast Cancer Test Result'):

           user_input = [meanradius,meantexture,meanperimeter,meanarea,meansmoothness,meancompactness,meanconcavity,meanconcavepoints,meansymmetry,meanfractaldimension,radiuserror,textureerror,perimetererror,areaerror,smoothnesserror,compactnesserror,concavityerror,concavepointserror,symmetryerror,fractaldimensionerror,worstradius,worsttexture,worstperimeter,worstarea,worstsmoothness,worstcompactness,worstconcavity,worstconcavepoints,worstsymmetry,worstfractaldimension,label]

           user_input = [float(x) for x in user_input]

           breastCancer_prediction = breastCancer_model.predict([user_input])

           if breastCancer_prediction[0] == 1:
                 breastcancer_diagnosis = 'The person is having heart disease'
           else:
                 breastcancer_diagnosis = 'The person does not have any heart disease'

        st.success(breastcancer_diagnosis)                   
               
