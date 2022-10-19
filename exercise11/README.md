### Small coding exercise 11

Download the `MA_cbg_human_mobility_2020.zip` file. Unzip it and use the `MA_cbg2cbg_2020_02.csv` and `MA_cbg2cbg_2020_04.csv` file to finish the following tasks.
 

**Task 11.1** On March 11, 2020, the World Health Organization (WHO) declared COVID-19, the disease caused by the SARS-CoV-2, a pandemic. Two days later, the Trump Administration declares a nationwide emergency and issues an additional travel ban on non-U.S. citizens traveling from 26 European countries due to COVID-19. 

The two provided csv files described the human mobility pattern of MA residents right before and after the outbreak of the COVID-19 pandemic in the US. Read them into pandas and calculate at least three metrics that we can use to understand the change in people’s mobility patterns due to COVID. 

Interpret your results.  

 

**Task 11.2** Use these two data sources to create two human mobility networks as directed graphs for MA with          

network node: individual census block group (neighborhood) in MA
network edge: residents from one neighborhood visiting another with the direction of the edge implying the direction of the visit 
weight of network tie: percentage of residents from one neighborhood (origin) visiting another (destination)
Calculate at least three network-based metrics that we can use to understand the change in people’s mobility due to COVID. 

Interpret your results.  

 

**Bonus task** Run the Louvain algorithm on these two networks using the networkx function `louvain_communities()` to detect sub-communities among census block groups (CBG) in MA. Discuss the racial and income profile of different “communities” identified by Louvain using ACS’s CBG-based demographic estimates. What changed during COVID? Any other pattern you have noticed? Another interesting thing to see about these communities is to plot them on the map and see how they are distributed in space. Do they tend to cluster with each other geographically? Speculate on why or why not. [one extra point] 