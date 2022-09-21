### Small coding exercise 6

Before you start: Download Boston’s crime incident reports for the year 2019, and 2020 [here](https://data.boston.gov/dataset/crime-incident-reports-august-2015-to-date-source-new-system).

**Task 6.1** Combine year 2019 and year 2020’s crime records into one pandas dataframe. 
Drop duplicates as well as any record that has missing values in the following columns: "INCIDENT_NUMBER", 
"OFFENSE_CODE", "DISTRICT", "Long", "Lat", "SHOOTING", "OCCURRED_ON_DATE". Save the "cleaned" pandas dataframe to a separate csv file. 


**Task 6.2** Read the csv file generated from Task 6.1 as a pandas dataframe. 
Use functions inside pandas to create a frequency table that counts the total number of crime incidents in Boston in each month from 2019 to 2020. 
Print this table.

**Task 6.3** Count the total number of crime incidents in each year by district (column "DISTRICT" in the data). 
Ignore DISTRACT with null value as well as value  "External". Discuss the spatial distribution of crime. 
Do you see any significant difference between districts in terms of their crime counts?  
