# Predict_3ptContest_Participants
Since a Japanese NBA player, Yuta Watanabe, has ranked top in 3pt percentage in this season, I am interested in the participants in this year's 3 point contest. As of end of Janualy 2023, I would like to predict the candidates, extracting data by [nba_api](https://github.com/swar/nba_api) and using Machine Learning techniques for classification from traditional models like Logistic Regression and SVM to Boosting/Stacking methods.

I finally compared the results of the techniques below.

* Traditional Machine Learning Models
  * Logistic Regression
  * K-Nearest Neighbors 
  * Support Vector Machine
  * Gaussian Naive Bayes
* Boosting 
* Stacking

## Explanation for dataset and files I created
The dataset I used was very imbalanced since less than 10 playes can participate in the contest every year while hundreds of players are playing in NBA league, though I limited the data into only players whose FG3M_RANK in every season is less than or equal to 150.
Although I chose "precision score " as a metric because I'm interested in predicting participants accurately and avoiding False Positive, the precision score didn't exceed 0.4 meybe due to the imbalanced data.
