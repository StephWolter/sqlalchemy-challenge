# sqlalchemy-challenge
# Use SQL Alchemy and Flask through Pandas to analyze given data.

## SetUp

* Create Repository in GitHub.
[sqlalchemy-challenge repository](https://github.com/StephWolter/sqlalchemy-challenge.git)

* Clone sqlalchemy-challenge repository to personal computer, then create the folder structure:

        * SurfsUp                           # Folder for all files
            * Resources                     # Given files
                * hawaii.sqlite             # sqlite file for the second half of the challenge
                * hawaii_measurements.csv   # daily measurements taken by research stations 
                * hawaii_stations.csv       # Hawaii research station info  
            * climate.ipynb                 # main code for first half of the challenge
            * app.py                        # main code for the second half of the challenge
            * README.md

* Examined the brief given on the bootcampspot module challenge #10 page, checked csv files in Visual Studio Code and Pandas. 
* Pushed regularly to git repository.


## DataGathering

* Created new Database sqlalchemy-challenge
* In Pandas created a new notebook "climate.ipynb".  
    * Imported necessary libraries
    * ### Reflect Tables into SQLAlchemy ORM
        * Imported python SQL toolkit and Object Relational Mapper
        * Created engine to hawaii.sqlite.
        * Reflected an existing database into a new model and reflected the tables.
        * Viewed all of the classes that automap found in the given csv files and saved the references.
            * **Measurements**
            * **Stations**
    * Opened our session (link) from Python to the DB.
        * Checked Measurement data for reference.

## DataAnalysis

    * ### Exploratory Precipitation Analysis
        * Found the most recent date in the **Measurement** data set using a session query.
        * Designed a query to retrieve the last 12 months of precipitation data and plotted the results. 
            * Hard coded the most recent date and converted it to a datetime format.
            * Calculated the prior year. 
                * NOTE: I had to use 366 days prior to the 'most recent date' in order to replicate the info 
                    in the climate_starter file we were given.  I'm not sure why, honestly.
            * Performed a query to retrieve the date and precipitation scores for the full prior year.
            * Saved the query results as a Pandas DataFrame, explicitly setting the column names to:
                * date
                * precipitation
            * Sorted the results by date and then used that to plot the inches of precipitation vs date.
                * Set title and labels
                * Rotated the labels on the x-axis for ease of visibility.
        * Useed Pandas to calculate the summary statistics for the precipitation data.
    * ### Exploratory Station Analysis
        * Checked Station data for reference using the inspector.
        * Designed a query to calculate the total number of stations in the dataset.
            * Set columns as station ids, and the count of those stations.
            * Grouped the data by the station ids.
            * Ordered by them in descending order of the counts.
        * Defined the most active station id from the previous query.
            * Calculated the lowest, highest, and average temperature using min, max, avg functions respectively.
        * Used the most active station id to query the last 12 months worth of temperature observation data (tobs)
        * Plotted that information as a histogram of the temperature and frequency of that temperature.
    * Closed the session.

## FLASK
    * Import all necessasry tools and libraries.
    * 













## Wrote out README
* Voila
