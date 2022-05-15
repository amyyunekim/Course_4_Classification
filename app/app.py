"""
To run this app:

1. cd into this directory
2. Run `streamlit run streamlit_app.py`
"""

import pandas as pd
import streamlit as st
import joblib
import pickle



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

    return pred[0] 

def descriptor (pred): 

    if pred =='Grade 5' :
        desc= "total or near collapse of the building"
    if pred =='Grade 4':
        desc= "walls collapse, partial structural failure of floor/roof"
    if pred =='Grade 3':
        desc ="large and extensive cracks in most walls, load capacity of structure is reduced"
    if pred =='Grade 2':
       desc= "cracks in many walls, damage to non structural parts"
    else:
        desc ="hairline to thin cracks in plaster on few walls" 
        
    return desc  

# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:#CBC3E3;padding:13px"> 
    <h1 style ="color:black; font-size: 32px;text-align:center;">Predicting building damage for Nepal</h1> 
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

        pred = prediction(height_ft_pre_eq,count_floors_pre_eq,age_building,plinth_area_sq_ft,has_superstructure_timber,
        has_superstructure_mud_mortar_stone) 
        desc = descriptor(pred)

        st.success('Your likely damage grade is {}: {}'.format(pred,desc))
        #st.success('Your likely damage grade is {}'.format(desc))

        print(pred)
        print(desc)
        
if __name__=='__main__': 
    main()
