### Small coding exercise 14
Download the `yelp_academic_dataset_review_Nov2022_small.jsonl` file from Canvas under `Files/datasets`. Use this dataset to finish the following tasks.

**Task 1.** For each review included in the dataset, use `spacytextblob` and its inherent document-level scores to get the polarity score of the text. Create a violinplot with the x-axis being individual reviews' star rating, and the y-axis being the calculated polarity scores. Interpret the results. 


**Task 2.** For each review included in the dataset, extract the subjective phrases in the text using  `spacytextblob` and its `sentiment_assessments.assessments` feature. Then, for each review whose review_id is in the following `target_review_ids` list, find the top 3 reviews that are most similar to it in terms of their subjective phrases. 

> target_review_ids = ["40thYphUgIfvJq17QCfTwA", "E9AB7V4z8xrt2uPF7T55FQ", "4PHFo_GRG4FEk1q4X7xQVQ", "4KpIldEM-tdnrJLqYzRfZQ", "PDHRlnEdkEcwATry4w71PQ", "meGaFP7yxQdjyABrYDVeoQ", "pgESDcC7eDx4z_epqon4_Q", "qeSxL-POvGLZD6aQ5O9kvw"]

Answer the following questions:

* For each of the target reviews, what are the top 3 reviews that are most similar to it in terms of their subjective phrases?

* What is the rating of each of the target reviews? What about the rating of their top 3 most similar reviews? Are they correlated? Interpret the results. 

Requirement:
* Use either spacy's word vector or the one-hot encoding method to get document-level word embeddings for the review text, which should be based only on the subjective phrases. 
* Use these word embeddings and the cosine similarity metric to find similar texts. 
 