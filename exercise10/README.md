### Small coding exercise 10

Download the `MA_cbg_human_mobility_2019.zip` file. Unzip it and use the `MA_cbg2cbg_2019_01.csv` file to finish the following tasks. 

**Task 10.1** Create a human mobility network for MA using the provided csv file.
* network node: individual census block group (neighborhood) in MA
* network edge: residents from one neighborhood visiting another
* weight of network tie: percentage of residents from one neighborhood visiting another    

How many nodes and edges are there in your network? 

 

**Task 10.2** Calculate weighted node degree and unweighted node degree for each census block group in the mobility network and use the results to create a pandas dataframe. The dataframe should have three columns. One column stores the census block group id, and the other two the two calculated node degrees. 

 

**Task 10.3** Create a plot that visualizes the distribution of the weighted node degrees. Is the human mobility network a scale-free network? In other words, does the degree distribution follow a power law? 

**Bonus task ** Does this network follow the “six degrees of separation” principle? Find out ways to analyze the network to answer this question. [1 extra point]