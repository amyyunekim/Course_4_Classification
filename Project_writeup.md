

## Predicting Earthquake Damage		

### Abstract:
Following the 7.8 Mw Gorkha Earthquake on April 25, 2015, Nepal carried out a massive household survey for 11 severely affected districts which covered all buildings in these districts to assess building damage. This project uses building features to predict the level of building damage sustained from Grade 1 to 5. A number of machine learning models were trialled to solve this multiclass problem. The chosen model was a Random Forest Classification model with a F1 micro score of 0.4470. A proof of concept model was deployed in Streamlit.

### Design: 
A logistic regression model was created as a baseline. A binary model was also considered at the start however was discarded as the cost of missing a prediction was too high. 

Classification models were evaluated against each other using a log loss score. Regression models were evaluated against each other using a root mean squared error (RMSE) score. Finally, the 2 winning models were compared using a F1 score. F1 was chosen as we wanted to consider both recall and precision in this problem to minimize missing both high damage as well as low damage predictions. An ensemble model was also considered however it did not perform as well as the 2 final models. The Random Forest Classification model had the highest F1 score and was the final selected model.

### Data:
The dataset was sourced from a kaggle [site](https://www.kaggle.com/code/ar89dsl/predicting-building-damage-from-earthquakes/data). This project focused on building construction and occupancy data to predict damage. The relevant tables were taken and stored in a relational SQLite database. The final dataset included 762,106 rows of building data with 42 features, of which 7 were categorical features. 
The target was a building damage grade from Grade 1 to Grade 5 (the full description of the damage grading can be found [here](http://eq2015.npc.gov.np/docs/#/faqs/faqs)).


### Algorithms:


<i> <b>Pre modelling:</b></i>

Feature Engineering: 
- Kept "a priori" features only i.e. dropped height post earthquake, floors post earthquake, location data
- Converted categorical features to binary dummy variables with the resulting dataframe shape: (758,949 , 69)

Class imbalance: Treated class imbalance toward higher damage grades with SMOTE oversampling.

<i> <b>Model Evaluation</b> </i>
<br>

The entire dataset was split into a 80/20 train vs holdout and all scores reported were calculated with 3-fold cross validation on the training portion only.


<table><tr><td>

| Classification Model| Log Loss Score|
| ------------------- | ---------------|
|Logistic Regression (Multinomial)| 1.3056|  
|Logistic Regression (One v Rest)  |1.3067| 
|Random Forest Classifier| 1.2974| 
|<b>Random Forest Classifer (SMOTE) |<b>1.2410| 
|XGBoost Classifier (SMOTE)| 1.2740 | 

</td><td>

| Regression Model| RMSE Score|
| --------------- | ---------------|
|Linear Regression| 1.2641|  
|Random Forest Regressor | 1.0427| 
|<b>Random Forest Regressor (SMOTE) |<b>0.9977| 
|XGBoost Regressor (SMOTE)| 1.0210 |  |

</td></tr> </table>

Random Forest Classifier (SMOTE) and Random Forest Regressor (SMOTE) performed best in their respective categories. An ensemble model was also considered however it fell short of the final two models scores. Finally when comparing the two, Random Forest Classifier (SMOTE) performed better than the Random Forest Regressor (SMOTE) (F1 micro score of 0.5427 vs 0.4267). 

### Final results:

Random Forest Classifier (SMOTE) was selected.

Training scores

- F1 0.5427 micro, 0.5366 macro
- Precision 0.5427 micro, 0.5427 macro
- Recall 0.5427 micro, 0.5639 macro

Holdout scores

- F1: 0.4470 micro, 0.4023 macro
- Precision: 0.4470 micro, 0.4187 macro
- Recall: 0.4470 micro, 0.4039 macro


### Tools:
- SQLite database for storage
- SQL alchemy for ingestion into Python
- Pandas, numpy & geopandas for EDA and data manipulation
- Sklearn and XgBoost for modelling
- Seaborn and Matplotlib for vizualisations
- Streamlit for model deployment

### Model Deployment: 
- Top 6 features were chosen as input features using Sklearn permutation_importance to deploy a proof-of-concept prediction app on Streamlit:  
https://share.streamlit.io/amyyunekim/course_4_classification/main/app/app.py