import os
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM, Dense
# from tensorflow.keras.models import load_model
# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# # Loading the saved models
# diabetes_model = load_model(os.path.join(working_dir, 'saved_models', 'diabetes.h5'))
# heart_disease_model = load_model(os.path.join(working_dir, 'saved_models', 'heart.h5'))
# parkinsons_model = load_model(os.path.join(working_dir, 'saved_models', 'park_2.h5'))

diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))


# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # Page title
    st.title('Diabetes Prediction using ML')

    # Getting the input data from the user
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

    # # Code for Prediction
    diab_diagnosis = ''

    # Creating a button for Prediction
    # if st.button('Diabetes Test Result'):
    #     user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
    #                   BMI, DiabetesPedigreeFunction, Age]

    #     user_input = [float(x) for x in user_input]

    #     diab_prediction = diabetes_model.predict([user_input])

    #     if diab_prediction[0] == 1:
    #         diab_diagnosis = 'The person is diabetic'
    #     else:
    #         diab_diagnosis = 'The person is not diabetic'

    # st.success(diab_diagnosis)

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
if selected == 'Heart Disease Prediction':

    # Page title
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

    # Code for Prediction
    heart_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        #user_input = [float(x) for x in user_input]
         # Convert input to NumPy array
        user_input_np = np.array([float(x) for x in user_input])
        user_input_np = user_input_np.reshape(1, -1)
        heart_prediction = heart_disease_model.predict(user_input_np)



       # heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] [0]== 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
       col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', format="%.3f")
        fhi = st.number_input('MDVP:Fhi(Hz)', format="%.3f")
        flo = st.number_input('MDVP:Flo(Hz)', format="%.3f")
        Jitter_percent = st.number_input('MDVP:Jitter(%)', format="%.5f")
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', format="%.4f")

    with col2:
        RAP = st.number_input('MDVP:RAP', format="%.4f")
        PPQ = st.number_input('MDVP:PPQ', format="%.4f")
        DDP = st.number_input('Jitter:DDP', format="%.5f")
        Shimmer = st.number_input('MDVP:Shimmer', format="%.5f")
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', format="%.3f")

    with col3:
        APQ3 = st.number_input('Shimmer:APQ3', format="%.5f")
        APQ5 = st.number_input('Shimmer:APQ5', format="%.4f")
        APQ = st.number_input('MDVP:APQ', format="%.5f")
        DDA = st.number_input('Shimmer:DDA', format="%.5f")
        NHR = st.number_input('NHR', format="%.5f")

    with col4:
        HNR = st.number_input('HNR', format="%.3f")
        RPDE = st.number_input('RPDE', format="%.6f")
        DFA = st.number_input('DFA', format="%.6f")
        spread1 = st.number_input('spread1', format="%.5f")
        spread2 = st.number_input('spread2', format="%.6f")

    with col5:
        D2 = st.number_input('D2', format="%.6f")
        PPE = st.number_input('PPE', format="%.6f")

    user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP]
    # Convert the list to a NumPy array
    user_input_np = np.array([user_input])
    user_input_reshaped = np.reshape(user_input_np, (1, 8))
    parkinsons_prediction = parkinsons_model.predict([user_input_reshaped])

    if parkinsons_prediction[0][0] == 1:
        parkinsons_diagnosis = "The person has Parkinson's disease"
    else:
        parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)