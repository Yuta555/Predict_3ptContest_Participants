# Predict_3ptContest_Participants
Since a Japanese NBA player, Yuta Watanabe, has ranked top in 3pt percentage in this season, I am interested in the participants in this year's 3 point contest. As of end of Janualy 2023, I would like to predict the participants, extracting players data by [nba_api](https://github.com/swar/nba_api) and former participants by [ReamGM](https://basketball.realgm.com/nba/allstar/three_point/players), and using Machine Learning techniques for classification from traditional models like Logistic Regression and SVM to Boosting/Stacking methods.

## Models/Methods I utilized
I finally compared the results of the techniques below.

* Traditional Machine Learning Models
  * Logistic Regression
  * K-Nearest Neighbors 
  * Support Vector Machine
  * Gaussian Naive Bayes
* Boosting 
* Stacking
* (Appendix)Neural Network

## Explanation for dataset and files I created
The dataset I used was very imbalanced since less than 10 playes can participate in the contest every year while hundreds of players are playing in NBA league. Hence, I limited the data into only players whose FG3M_RANK in every season are less than or equal to 150, and I applied RandomOverSampling to deal with the imbalance.
Although I chose "precision score" as a metric because I'm interested in predicting participants accurately and avoiding False Positive, the precision score didn't exceed 0.4 meybe due to the imbalanced data.

### DataExtract.py
This module is for extracting stats data by player and season, using [nba_api](https://github.com/swar/nba_api). I narrowed down the sample dataset to players who ranked within TOP 150 with respect to FG3M by season. Moreover, I added a constraint for the extraction such as start/end date gathering the data so that start data is Octorber 1 and end date is January 23 in every season.

### ContestParticipants.py
This module is for scraping and gathering data of former participants from [ReamGM](https://basketball.realgm.com/nba/allstar/three_point/players).

### Prediction.ipynb
In this notebook, I implemented various kinds of ML models and methods to compare the results and to find more accurate model.


## Output
I tried several models and I evaluated each player in the way that a player who is evaluated as a possible participant by more models is more likely to be participants, that is, the larger "sum" column is, the more likely to be a participant I consider the player is.

<img width="954" alt="image" src="https://user-images.githubusercontent.com/59324565/214356979-8b30ab55-8468-486c-89dc-f54ef507fc44.png">

