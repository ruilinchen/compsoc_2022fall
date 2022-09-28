### Small coding exercise 8

**Task 8.1** Create a bubble map for property crimes in Boston, 2019. 
Each bubble represents one property crime incident. 
Your map should look something like [this example](https://hermionewy.github.io/crime/) online.


**Task 8.2** Create another bubble map for violent crimes in Boston, 2019. 
Use a different map design (marker color, tile style, etc). 


**Task 8.3** Calculate district-level violent vs. property crime counts. 
Use boston's zoning map from [here](https://data.boston.gov/dataset/boston-zoning-subdistricts) to map individual crime incidents to zoning district. 
Create a bubble map for these two sets of counts. 
There should be two sets of bubbles in your map. 
One set represents **zoning subdistrict-level** violent crime counts, and the other set zoning subdistrict-level property crime counts. 
These two bubble sets should be colored differently, but the size of the bubble for both sets should indicate the relative size of the crime count. 
Use each zoning subdistrict’s centroid location to place their bubbles on the map. 

Hint: in geopandas,  `gdf["geometry"].centroid` returns the centroid point of the corresponding geometry.]
