### Small coding exercise 13

Download the `indeed_scraped_data.zip` file from Canvas under `Files/datasets`. Unzip it and use all the files under the folder "job_info_data" that are scraped on May 22, 2022 (having "5222022" in the filename) for the following assignments. 

 

**Task 1.** Create one pandas dataframe that combines all the data scraped from May 22, 2022 together. Drop rows with missing job titles and/or job descriptions. Use `spacy` to tokenize all the job titles included in the cleaned dataframe. For each job title, find all the nouns and all the adjectives in the title and get their lowercased lemmatized form. Use the reformatted nouns to construct a vocabulary set for this dataframe. How many unique nouns are there? Construct another vocabulary set using the reformatted adjectives. How many unique adjectives are there? What kind of different information do the nouns versus the adjectives reveal about the specific job? 


**Task 2.** Choose the first job title in your dataframe as the primary string. Use one-hot encoding as the word embedding method and find jobs in your cleaned dataframe that have similar nouns in the title as your primary string. 


**Task 3.** Use spacy's word vector to do Task 2. Compare the results. 


**Bonus task 1.** Do task 3 for both the nouns and the adjectives in the title. Combine the similarity values from comparing the nouns and from comparing the adjectives, and find jobs in your cleaned dataframe that are similar to your primary string in the combined setting. Compare the results with what you get from Task 3.  [0.5 extra point] 

 

**Bonus task 2.** Do task 3 for job descriptions. Compare the results with what you get from processing job titles. Which data source gives you better results in terms of finding actual similar jobs? Can you guess why? [0.5 extra point] 

You can also try doing Bonus task 2 using (1) verbs only; (2) noun-verb pairs, and compare their results with using nouns only. How are the results different from each other? 