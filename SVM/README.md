# SVM
## Test Questions
* Q1: Who is Vladimir N. Vapnik?  
  &emsp;&emsp;Vladimir Naumovich Vapnik is one of the main developers of the Vapnik–Chervonenkis theory of statistical learning, and the co-inventor of the support-vector machine method, and support-vector clustering algorithm.
* Q2: Maximum Margin Principle and why support vector is important?  
  &emsp;&emsp;1. Maximum Margin Principle: Find the hyperplane with maximum separation marginon the training data.  
  &emsp;&emsp;2. Because they *support* the separating hyperplane. In other words, they determine the maximum margin. 
* Q3: How to compute the distance between a given data point to the boundary?  
  &emsp;&emsp;Geometric margin: $\displaystyle\gamma_i=\frac{y_i(w^Tx_i+b)}{||w||}$   
* Q4: What limitations the linear SVM suffered from?  
  &emsp;&emsp;The linear SVM can not separate the data that is not linearly separable.