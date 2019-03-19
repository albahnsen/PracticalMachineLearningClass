# Practical Machine Learning

*Instructor: Alejandro Correa Bahnsen*

- email: <al.bahnsen@gmail.com>
- twitter: [@albahnsen](https://twitter.com/albahnsen)
- github: [albahnsen](http://github.com/albahnsen)


The use of statistical models in computer algorithms allows computers to make decisions and predictions, and to perform tasks that traditionally require human cognitive abilities. Machine learning is the interdisciplinary field at the intersection of statistics and computer science which develops such algorithnms and interweaves them with computer systems. It underpins many modern technologies, such as speech recognition, internet search, bioinformatics, computer vision, Amazon’s recommender system, Google’s driverless car and the most recent imaging systems for cancer diagnosis are all based on Machine Learning technology.

This course on Machine Learning will explain how to build systems that learn and adapt using real-world applications. Some of the topics to be covered include machine learning, python data analysis, deep learning frameworks, natural language processing models and recurrent models. The course will be project-oriented, with emphasis placed on writing software implementations of learning algorithms applied to real-world problems, in particular, image analysis, image captioning, natural language pocessing, sentiment detection, among others.

## Requiriments 
* [Python](http://www.python.org) version 3.5;
* [Numpy](http://www.numpy.org), the core numerical extensions for linear algebra and multidimensional arrays;
* [Scipy](http://www.scipy.org), additional libraries for scientific programming;
* [Matplotlib](http://matplotlib.sf.net), excellent plotting and graphing libraries;
* [IPython](http://ipython.org), with the additional libraries required for the notebook interface.
* [Pandas](http://pandas.pydata.org/), Python version of R dataframe
* [Seaborn](stanford.edu/~mwaskom/software/seaborn/), used mainly for plot styling
* [scikit-learn](http://scikit-learn.org), Machine learning library!

A good, easy to install option that supports Mac, Windows, and Linux, and that has all of these packages (and much more) is the [Anaconda](https://www.continuum.io/).

GIT!! Unfortunatelly out of the scope of this class, but please take a look at these [tutorials](https://help.github.com/articles/good-resources-for-learning-git-and-github/)

## Evaluation

* 30% Exercises
* 50% Projects
* 20% Final Project

## Schedule

### Supervised Machine Learning
| Date | Session         | Notebooks/Presentations          | Exercises |
| :----| :----| :------------- | :------------- | 
| January 21st | Introduction to python and ML | <ul><li>[1 - Intro to ML](https://nbviewer.jupyter.org/github/albahnsen/PracticalMachineLearningClass/blob/master/notebooks/01-IntroMachineLearning.ipynb) </li> <li>[2 - Intro to Python for data analysis](https://nbviewer.jupyter.org/github/albahnsen/PracticalMachineLearningClass/blob/master/notebooks/02-IntroPython_Numpy_Scypy_Pandas.ipynb) </li></ul> | <ul><li>[E1 - Data Science Overview](https://github.com/albahnsen/PracticalMachineLearningClass/blob/master/exercises/E1-DataScienceOverview) </li><li>[E2 - Python Text Analysis](https://nbviewer.jupyter.org/github/albahnsen/PracticalMachineLearningClass/blob/master/exercises/E2-%20Python%20Text%20Analysis.ipynb) </li>  </ul> | 
| January 28th | Linear Models | <ul><li>[3 - Linear Regression](https://nbviewer.jupyter.org/github/albahnsen/PracticalMachineLearningClass/blob/master/notebooks/03-linear_regression.ipynb) </li> <li>[4 - Logistic Regression](https://nbviewer.jupyter.org/github/albahnsen/PracticalMachineLearningClass/blob/master/notebooks/04-logistic_regression.ipynb) </li>  </ul> | <ul><li>[E3 - Supervised vs Unsupervised Overview]() </li> <li>[E4 - Linear Models]() </li> </ul> | 
| February 4th | SVM & Decision Trees  | <ul><li>[5 - SVM](https://nbviewer.jupyter.org/github/albahnsen/PracticalMachineLearningClass/blob/master/notebooks/05-SVM.ipynb) </li><li>[6 - Decision Tress](https://nbviewer.jupyter.org/github/albahnsen/PracticalMachineLearningClass/blob/master/notebooks/06-decision_trees.ipynb) </li><li>[7 - Regularization](https://nbviewer.jupyter.org/github/albahnsen/PracticalMachineLearningClass/blob/master/notebooks/07-regularization.ipynb) </li></ul> | <ul><li>[E5 - Decision Trees Overview](https://github.com/albahnsen/PracticalMachineLearningClass/blob/master/exercises/E5-DecisionTreesOverview.md) </li> <li>[E6 - SVM - Regularization](https://nbviewer.jupyter.org/github/albahnsen/PracticalMachineLearningClass/blob/master/exercises/E6-SVM%26Regularization.ipynb) </li> <li>[E7 - Decision Trees](https://nbviewer.jupyter.org/github/albahnsen/PracticalMachineLearningClass/blob/master/exercises/E7-DecisionTrees.ipynb) </li></ul> | 
| February 11th | Machine Learning as a Service | <ul>  <li>[8 - Introduction to APIs](https://nbviewer.jupyter.org/format/slides/github/albahnsen/PracticalMachineLearningClass/blob/master/notebooks/08-IntroductionToAPIs.ipynb#/) </li> <li>[9 - Model Deployment](https://nbviewer.jupyter.org/github/albahnsen/PracticalMachineLearningClass/blob/master/notebooks/09-Model_Deployment.ipynb) </li><li>[10 - Creating APIs in AWS](https://nbviewer.jupyter.org/format/slides/github/albahnsen/PracticalMachineLearningClass/blob/master/notebooks/10-CreatingAPIinAWS.ipynb#/) </li></ul> | <ul><li>[P1 - Survival Prediction API](https://nbviewer.jupyter.org/github/albahnsen/PracticalMachineLearningClass/blob/master/exercises/P1-UsedVehiclePricePrediction.ipynb) </li> </ul> | 
| February 18th |  Ensembles | <ul><li>[11 - Bagging](https://nbviewer.jupyter.org/github/albahnsen/PracticalMachineLearningClass/blob/master/notebooks/11-Ensembles_Bagging.ipynb) </li><li>[12 - Boosting](https://nbviewer.jupyter.org/github/albahnsen/PracticalMachineLearningClass/blob/master/notebooks/12-Ensembles_Boosting.ipynb) </li></ul> | <ul><li>[E8 - Best Ensemble Overview](https://github.com/albahnsen/PracticalMachineLearningClass/blob/master/exercises/E8-EnsembleTreesOverview.md) </li><li>[E9 - Bagging](https://nbviewer.jupyter.org/github/albahnsen/PracticalMachineLearningClass/blob/master/exercises/E9-Bagging.ipynb) </li> </ul> | 
| February 25th |  Random Forest | <ul><li>[13 - Random Forest](https://nbviewer.jupyter.org/github/albahnsen/PracticalMachineLearningClass/blob/master/notebooks/13-Ensembles_RandomForest.ipynb) </li></ul> | <ul><li>[E10 - Random Forest Performance Review](https://github.com/albahnsen/PracticalMachineLearningClass/blob/master/exercises/E10-RandomForestPerformanceReview.md) </li><li>[E11 - Random Forest](https://nbviewer.jupyter.org/github/albahnsen/PracticalMachineLearningClass/blob/master/exercises/E11-RandomForest.ipynb) </li> </ul> | 
| March 4th |  Feature Engineering | <ul><li>[14 - Feature Engineering](https://nbviewer.jupyter.org/github/albahnsen/PracticalMachineLearningClass/blob/master/notebooks/14-data_preparation.ipynb) </li> </ul> | <ul><li>[E12 - Gradient Boosting Review](https://github.com/albahnsen/PracticalMachineLearningClass/blob/master/exercises/E12-GradientBoostingRewiew.md) </li> <li>[E13 - Categorical Encoding ](https://nbviewer.jupyter.org/github/albahnsen/PracticalMachineLearningClass/blob/master/exercises/E13-CategoricalEncoding.ipynb) </li> </ul> | 
| March 11th | Project Presentations  |  | | 
| March 18th |  Unbalanced Learning | <ul><li>[15 - Unbalanced Learning](https://nbviewer.jupyter.org/github/albahnsen/PracticalMachineLearningClass/blob/master/notebooks/15-Unbalanced_Datasets.ipynb) </li></ul> | <ul><li>[E14 - Unbalanced Learning Overview](https://github.com/albahnsen/PracticalMachineLearningClass/blob/master/exercises/E14-UnbalancedLearningOverview.md) </li> <li>[E15 - Fraud Detection](https://nbviewer.jupyter.org/github/albahnsen/PracticalMachineLearningClass/blob/master/exercises/E15-fraud_detection.ipynb) </li>  </ul>  | 


 ### Natural Language Processing
| Date | Session         | Notebooks/Presentations          | Exercises |
| :----| :----| :------------- | :------------- | 
| April 1st | Natural Language Processing  | <ul><li>[16 - Natural Language Processing]() </li></ul> | <ul><li>[P2 - NLP Movies Analysis API]() </li> </ul> | 
| April 8th |  Sentiment Analysis | <ul><li>[17 - Sentiment Analysis]() </li></ul> | <ul><li>[]() </li>  </ul> |
| April 22nd | Project Presentations  |  | | 
 ### Advanced Topics in Machine Learning
| Date | Session         | Notebooks/Presentations          | Exercises |
| :----| :----| :------------- | :------------- | 
| April 29th |  Introduction to Deep Learning | <ul><li>[18 - MLP and Backpropagation]() </li></ul> <ul><li>[19 - Introduction to Deep Learning]() </li></ul> | <ul><li>[]() </li> </ul> | 
| May 6th |  Recurrent Neural Networks| <ul><li>[20 - LSTM]() </li></ul>  <ul><li>[21 - CNN]() </li></ul> | <ul><li>[]() </li> </ul> | 


### Final Project Presentation 

* [P3 - Kaggle Competition]() 


