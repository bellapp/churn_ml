# from pycaret.cl import load_model, predict_model
from pycaret.classification import load_model, predict_model
#import pycaret 
import streamlit as st
import pandas as pd
import numpy as np

model = load_model('bellout_ml1')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():

    from PIL import Image
    image = Image.open('logo.png')
    image_hospital = Image.open('bank.jpg')

    # st.image(image,use_column_width=False)

    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict ?",
    ("Online", "Batch"))

    st.sidebar.info('This app is created to predict churn bank client ')
    # st.sidebar.success('https://www.pycaret.org')
    
    st.sidebar.image(image_hospital)

    st.title("Churn Bank Prediction App")

    if add_selectbox == 'Online':

        creditScore = st.slider('Credit Score', min_value=1, max_value=1000, value=1)
        
        geography  =st.selectbox('Geography', ['France', 'Germany', 'Spain'])
        gender = st.selectbox('Gender', ['Male', 'Female'])
        age = st.slider('Age', min_value=1, max_value=100, value=25)
        tenure = st.slider('Tenure', min_value=0, max_value=10, value=0)
        balance = st.slider('Balance', min_value=0, max_value=500000, value=0)
        numofproducts = st.number_input('Number Of Products', min_value=1, max_value=4, value=1)
        hascrcard= st.selectbox('Has Credit Card',  ['0', '1'])
        isactivemember =  st.selectbox('Is Active Member',  ['0', '1'])
        estimatedsalary  = st.number_input('Estimated Salary', min_value=1, max_value=200000, value=1)


        # sex = st.selectbox('Sex', ['male', 'female'])
        # bmi = st.number_input('BMI', min_value=10, max_value=50, value=10)
        # children = st.selectbox('Children', [0,1,2,3,4,5,6,7,8,9,10])
        # if st.checkbox('Smoker'):
        #     smoker = 'yes'
        # else:
        #     smoker = 'no'
        # region = st.selectbox('Region', ['southwest', 'northwest', 'northeast', 'southeast'])

        output=""
        output_result = ""
        output_message = ""

        # input_dict = {'creditScore' :CreditScore,'geography' :Geography,'gender' :Gender,'age' :Age,'tenure' :Tenure,'balance' 
        # :Balance,'numofproducts' :NumOfProducts,'hascrcard':HasCrCard,'isactivemember' :isActiveMember,'estimatedsalary'
        #   :EstimatedSalary}
        input_dict = {'CreditScore':creditScore,'Geography':geography,'Gender':gender,'Age':age,
          'Tenure':tenure,'Balance':balance,'NumOfProducts':numofproducts,'HasCrCard':hascrcard,'IsActiveMember':isactivemember,'EstimatedSalary':estimatedsalary}
        input_df = pd.DataFrame([input_dict])

        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            output_result = 'Churn' if output == 1 else 'Not Churn'
            output_message = 'The client will {}'.format(output_result)
            
        if output == 1 :
            st.warning('Result : {}' .format(output_message)   )
        else :
            st.success('Result : {}' .format(output_message) )
      

    if add_selectbox == 'Batch':

        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)

if __name__ == '__main__':
    run()