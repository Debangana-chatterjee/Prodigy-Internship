# Data Science Internship(Prodigy Infotech) 


---

## Task-1

**Objective:**
- Analyze global population trends over the years.
- Identify the top 10 most populous countries based on total population across all years.
- Visualize Region and income based distributions.
  

**Key insights include:**

- A steady increase in global population over the years, with significant growth in certain regions.
- The top 10 most populous countries contributing a substantial share of the world's total population.
- The role of economic factors in population distribution, as observed through income-based analysis.


Through data cleaning, handling missing values, and exploratory visualizations, we provided a clearer understanding of how global demographics have evolved.


---
## Task-2 

**Objective**


The project aims to perform Exploratory Data Analysis (EDA) and data preprocessing on the Titanic dataset. The goal is to understand, clean, and transform the dataset for further analysis or predictive modeling.


**Key Insights:**

- First-class passengers had a significantly higher survival rate compared to second and third-class passengers.
- Females had a much higher survival rate than males.
- The age distribution is right-skewed, with most passengers in their 20s–30s.
- Higher fares were associated with a higher likelihood of survival.

---
## Task-3

**Objective**

The project focuses on analyzing customer demographic data and banking interactions to derive insights for customer segmentation and marketing strategies. It includes exploratory data analysis (EDA), feature engineering, and machine learning to predict customer responses.


**Key Insights:**

- Certain customer demographics (age, job type, education level) show higher engagement with the bank's marketing campaigns.
- The number of previous contacts plays a crucial role in predicting customer response.
- Duration of Call was the most influential factor in predicting customer response.
- Customers who had a positive outcome in the previous campaign were more likely to respond positively again
- The dataset was imbalanced, SMOTE was applied to balance the dataset, leading to improved model performance.
- The Decision Tree model provided reasonable accuracy of **79%**.
- The classification report highlighted that precision and recall scores varied significantly between classes.
- Further fine-tuning or alternative models could improve prediction accuracy.


---
## Task-4

**Objective**

The project aims to analyze sentiment from Twitter posts using Natural Language Processing (NLP) techniques. The dataset consists of 1.6 million tweets, extracted via the Twitter API, and annotated as either negative (0) or positive (4). The goal is to develop a model that can detect sentiment in social media posts.


**Key Insights:**

### Dataset Overview:

- The dataset includes tweet text along with metadata like user ID, timestamp, and sentiment labels (0 for negative, 4 for positive).
- A significant number of tweets require preprocessing to remove unnecessary elements such as URLs, special characters, and stopwords.

### Preprocessing Steps:

- Stopwords were removed using NLTK.
- Tokenization, stemming, and lemmatization techniques were applied to standardize text.
- Data cleaning included removing usernames, links, and punctuation.

### Modeling Approach:

- NLP techniques such as TF-IDF was used for feature extraction.
- The classification model likely involved machine learning algorithms such as Logistic Regression.
- Built with Streamlit for easy tweet sentiment prediction.

### Results and Performance:

- Sentiment classification model was evaluated using accuracy, precision, recall, and F1-score.
- The results indicate the effectiveness of the chosen approach in distinguishing positive and negative sentiments.


---
