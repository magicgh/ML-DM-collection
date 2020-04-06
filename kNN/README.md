# kNN
## Test Questions
* Q1: What is the classification? How to perform classification by human? And what is the simplest way?  
  1. Classification is the problem of identifying to which of a set of categories a new observation belongs based on a training set of data containing observations whose category membership is known.
  2. By Comparing the similarity between a new observation and records in our memory.
  3. Vectorize the new observation and sample data, compute their distances.
* Q2: What problem of 1NN is addressed by kNN? 
  1. The training data are sufficiently distinct with each other.
  2. Insufficient robustness to noises.

* Q3: How to (why) incorporate the distance into classical kNN? And what will be benefited from it?  
  1. How: Weighting by the distance.     
     Why: When the class distribution is skewed, classical kNN performs badly.
  2. Enhance the accurary of results.
  
* Q4: How to solve the scaling issue faced by KNN?  
  &emsp;&emsp;Normalize the data by some specific functions.

* Q5: How to evaluate the performance of a classifier?  
  &emsp;&emsp;By Caculating accuracy (accuracy may be fine when dealing with balanced datasets), or confusion matrix (commonly used).
  
* Q6: What is model selection? How to solve this issue?  
  1. Model selection is the task of selecting a statistical model from a set of candidate models, given data. In kNN, that is choosing the value of k.
  2. Using different validating methods (various validation subsets) to determine the values of parameters. In kNN, that is tuning the value of k.