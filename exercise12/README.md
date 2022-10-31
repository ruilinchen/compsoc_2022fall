### Small coding exercise 12

Download the `indeed_scraped_data.zip` file. Unzip it and use all the files under the folder "job_info_data" that are scraped on May 22, 2022 (having "5222022" in the filename) for the following assignments. 



**Task 1**. Create one pandas dataframe that combines all the data scraped from May 22, 2022 together. Drop rows with missing job titles and/or job descriptions. Use `spacy` to tokenize all the job descriptions included in the cleaned dataframe. Count how many unique tokens are there in total, and describe the distribution of token tags among them.

 

**Task 2**. Construct a token/term frequency dictionary from the cleaned dataframe. The keys of the dictionary should be unique tokens, and the values being the frequency of the tokens in the entire corpus. Save that dictionary to a json file. What are the top 10 most common tokens according to your frequency dictionary? 

 

**Bonus task**. Use the cleaned dataframe from the previous task. Separate jobs with the keywords {"compliance", "regulation", "regulatory"} in the job title from those without such keywords in the job title. Treat their job descriptions as two separate corpuses and do Task 2 for each of them. Compare their term frequency dictionaries. Is there a significant difference between them? How can you tell? [one extra point] 