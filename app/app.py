"""
To run this app:

1. cd into this directory
2. Run `streamlit run streamlit_app.py`
"""

import pandas as pd
import streamlit as st
import joblib
import pickle
import sklearn


# loading the trained model
classifier = joblib.load('app/mini_model')
# load the model from disk
#classifier = pickle.load(open('minimodel.sav', 'rb'))

@st.cache()
  
## defining the function which will make the prediction using the data which the user inputs 
def prediction(height_ft_pre_eq,count_floors_pre_eq,age_building,plinth_area_sq_ft,has_superstructure_timber,
        has_superstructure_mud_mortar_stone):   
 
    # Pre-processing user input    
    if has_superstructure_timber == 0:
        has_superstructure_timberTimber = 0
    else:
        has_superstructure_timber = 1
 
    if has_superstructure_mud_mortar_stone ==0 :
        has_superstructure_mud_mortar_stone = 0
    else:
        has_superstructure_mud_mortar_stone = 1  
 
    # Making predictions 
    prediction = classifier.predict( 
        [[height_ft_pre_eq,count_floors_pre_eq,age_building,plinth_area_sq_ft,has_superstructure_timber,
        has_superstructure_mud_mortar_stone]]
        )            

    pred = prediction
    return pred 
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:#CBC3E3;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Predicting building damage for Nepal</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    height_ft_pre_eq = st.number_input('Building Height in ft')
    count_floors_pre_eq = st.number_input('Number of floors') 
    age_building = st.number_input("Building Age") 
    plinth_area_sq_ft = st.number_input("Area in square feet")
    has_superstructure_timber = st.selectbox('Has timber superstructure?',("No","Yes"))
    has_superstructure_mud_mortar_stone = st.selectbox('Has mud/mortar/stone superstructure?',('No','Yes'))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(height_ft_pre_eq,count_floors_pre_eq,age_building,plinth_area_sq_ft,has_superstructure_timber,
        has_superstructure_mud_mortar_stone) 
        st.success('Your likely damage grade is {}'.format(result))
        print(result)
     
if __name__=='__main__': 
    main()
