### Small coding exercise 5

**Task 5.1** Download "MA_cbg_human_mobility_2019.zip" from Canvas under "Files/datasets". 
Write a program that loops through all the files in this zip file and prints the name of all the "csv" files. 
Use `zipfile` package. 


**Task 5.2** Unzip the above zipped file in your laptop’s File System and you will get a folder named "MA_cbg_human_mobility_2019". 
Write a program that loops through all the files stored in this folder and counts the number of lines contained in each of the "csv" files. 
Print a sum of the line counts. Use with statement when reading files. 


**Task 5.3** Use the same program from Task 5.2 that counts lines of all the csv files in "MA_cbg_human_mobility_2019". 
Store the output in a dictionary with keys being filenames and values being the corresponding line counts. 
Write the output to a json file. 