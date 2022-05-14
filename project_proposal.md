
## Question/Need:

What is the question behind your analysis or model and what practical impact will your work have?

- Which buildings are most prone to damage in an earthquake?
- Build more resilient communities to withstand natural catastrophes

Who is your client and how will that client benefits from exploring this question or building this model/system?

- Construction companies - build stronger EQ proof structures
- Government - policy to implement building codes
- Insurance companies - understand the riskiness of underwriting certain buildings

## Data Description:

What dataset(s) do you plan to use, and how will you obtain the data? Please include a link!
- 2015 Gorkha, Nepal 7.8 magnitude earthquake data from Kaggle:
https://www.kaggle.com/code/ar89dsl/predicting-building-damage-from-earthquakes/data

What is an individual sample/unit of analysis in this project? In other words, what does one row or observation of the data represent?
-  One building impacted by the earthquake

What characteristics/features do you expect to work with? In other words, what are your columns of interest?
- Construction information e.g. number of floors, square feet, construction material, land surface etc. 

If modeling, what will you predict as your target?
- The level of damage sustained (1 - 5)


## Tools:

How do you intend to meet the tools requirement of the project?
- SQLite database for storage
- SQL alchemy for ingestion into Python
- Pandas, numpy for EDA
- Sklearn for modelling
- XGBoost
- Seaborn and Matplotlib for vizualisations
- Stretch goal: deploy in streamlit?

## MVP Goal:

Have a baseline model complete