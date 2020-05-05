# PCA
## Test Questions 
* Q1: Why the variances $\Sigma_{ij}$ also defines the signal-to-noise ratio?
  And the properties of SNR w.r.t. $\Sigma_{ij}$.

  &emsp;&emsp;$\displaystyle SNR=\frac{\sigma^2_{signal}}{\sigma^2_{noise}}$, is used to evaluate data quality. 

  &emsp;&emsp;In other words, a high $SNR$ (<<1) indicates high precision data, while a low SNR indicates noise contaminated data.

* Q2: Beside performing ED on $X^TX$, is there other way to obtain
  the principal components?

  &emsp;&emsp;Performing SVD on $X^TX$.

* Q3: Can PCA handle the data drawn from multiple subspace? 

  &emsp;&emsp;No, PCA can only handle the data drawn from singe subspace.

* Q4: PCA is a unsupervised dimension reduction method, which may suffer from what problem or limitations?  
  &emsp;&emsp; 1. We cannot get the precise information regaring data sorting.  
  &emsp;&emsp; 2. Because the input data is not known and not labeled by people in advance. That means the machine require to do this itself (clustering data). Hence the accuracy of the results would be less than supervised learning techniques.



  



























