# disease_prediction
In the proposed system the diseases are predicted automatically by the system using our model which is trained on the medical dataset. This system also shows the confidence score of the prediction. After getting the anticipated disease, the system will suggest doctors associated with that disease and therefore the patient can consult to the doctor online. The proposed system acts as a decision support system and will prove to be an aid for the physicians with the diagnosis.

## Technology & tools: 
  ### Frontend : 
      HTML, CSS, Javascript, BOOTSTRAP 4.0
  
  ### Backend : 
      Django 
  
  ### Technology :
      Machine learning
  ### Database:
      PostgreSQL


# How To Use This
First make sure PostgreSQL and pgadmin is install in your system. 
then you have to manually create a DB instance on PostgreSQL named "predico", better use PgAdmin for that.
make a new environment(recommended) and run...

- Run pip install -r requirements.txt to install dependencies
- Run python manage.py makemigrations
- Run python manage.py migrate
- Run python manage.py runserver
- Navigate to http://127.0.0.1:8000/ in your browser
