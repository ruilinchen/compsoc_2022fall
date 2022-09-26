### Small coding exercise 7

Download Boston’s crime incident reports for the year 2019, and 2020 [here](https://data.boston.gov/dataset/crime-incident-reports-august-2015-to-date-source-new-system).

According to National Institute of Justice, violent crimes and property crimes include the following offense types respectively:
- Violent crimes: robbery, assault, rape
- Property crimes: burglary, larceny, auto theft, arson

**Task 7.1** Combine year 2019 and year 2020’s crime records into one pandas dataframe. 
Drop duplicates as well as any record that has missing values in the following columns: “INCIDENT_NUMBER”, “OFFENSE_CODE”, “DISTRICT”, “Long”, “Lat”, “SHOOTING”, “OCCURRED_ON_DATE”. Save the “cleaned” pandas dataframe to a separate csv file. 
Use the "OFFENSE_DESCRIPTION" column to identify violent vs. property crime incidents, and based on the cleaned dataframe, count the total number of violent vs. property crime incidents in Boston in year 2019 and year 2020 respectively. 
Print the results. Do you see any trend? 


**Task 7.2** Create a scatter plot of annual violent crimes vs. annual property crimes by district in Boston from 2019 to 2020. 
X axis: annual property crimes. Y axis: annual violent crimes. Use different colors to color data from different years. 


**Task 7.3** Create a bar plot of the sum of annual violent and property crimes by district in Boston from 2019 to 2020. 
X axis: districts. Y axis: annual sums. Use different bars to represent data from different years. 


**Task 7.4** Create a violin plot of district-level shooting incidents by quarter in Boston from 2019 to 2020. 
X axis: quarters. Y axis: district-level shooting incidents (counts).