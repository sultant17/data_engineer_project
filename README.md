# data_engineer_project
Airflow ETL using a docker. Download the 'final_diploma' folder. In the command line, navigate to the folder and run the 'docker-compose up' command. 
You will have all the necessary services up and running (including the Postgres database, airflow webserver etc.). 
You will also have the necessary directories for creating dags and applications, as well as directories with logs.


Project Summary:
SberAutosubscription is a long-term car rental service for individuals. The client pays a fixed monthly payment and receives to use the car for a period of six months to three years. SberAutosubscription offers a new way for the Russian market to own a car and acts as an alternative to a car loan.

EDA Tasks:
- Read the provided dataset.
- Review the descriptions of the attributes presented.
- Evaluate the completeness and purity of the data. Try to understand what is behind this data in the real world. Bring the data into a convenient / normal form for further work.
- Do some basic cleanup (duplicates, nulls, data typing, unnecessary attributes).
- Look at the distribution of key attributes, their relationship.

Data Engineering Tasks:
- Set up and run a local database suitable for storing and executing queries against data in the provided dataset.
- Create objects in the database to store the source file data.
- Process and put into the database the data from the provided main dataset.
- Set up a pipeline for collecting, processing and writing new .json files to the database.

