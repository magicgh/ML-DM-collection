# Introduction to Machine Learning Final Assignment

## Description

Simple implementation of kNN & SVM on MNIST dataset.

## Results

* **kNN Classifier** (k=3, PCA, n_components=0.8)
mean=95.8550%, std=0.00227706
total time: 649.5709s

* **kNN Classifier based on KD-Tree** (k=3, PCA, n_components=0.8)
mean=95.8550%, std=0.00227706  
total time: 1616.3644s  

* **Weighted kNN Classifier based on Sklearn KD-Tree** (PCA, n_components=0.8)
  * Gaussian Function
  
    |     k      |     1      |     2      |     3      |     4      |     5      |
    | :--------: | :--------: | :--------: | :--------: | :--------: | :--------: |
    |    Mean    |  95.5400%  |  95.5400%  |  95.8550%  |  96.0050%  |  95.6950%  |
    |     SD     | 0.00073485 | 0.00073485 | 0.00227706 | 0.00231517 | 0.00310000 |
    | Total Time |  6.7580s   |  7.5520s   |  7.9370s   |  8.2820s   |  8.6380s   |

  * Inverse Proportional Function  
  
    |     k      |     1      |     2      |     3      |     4      |     5      |
    | :--------: | :--------: | :--------: | :--------: | :--------: | :--------: |
    |    Mean    |  95.5400%  |  95.5400%  |  95.8550%  |  96.0000%  |  95.7250%  |
    |     SD     | 0.00073485 | 0.00073485 | 0.00227706 | 0.00224165 | 0.00316623 |
    | Total Time |  7.0120s   |  7.2941s   |  7.9420s   |  8.0890s   |  8.5873s   |

* **Weighted kNN Classifier based on Sklearn Ball Tree** (PCA, n_components=0.8)
  * Gaussian Function

    |     k      |     1      |     2      |     3      |     4      |     5      |
    | :--------: | :--------: | :--------: | :--------: | :--------: | :--------: |
    |    Mean    |  95.5400%  |  95.5400%  |  95.8550%  |  96.0050%  |  95.6950%  |
    |     SD     | 0.00073485 | 0.00073485 | 0.00227706 | 0.00231517 | 0.00310000 |
    | Total Time |  7.2410s   |  8.1700s   |  7.5830s   |  7.7931s   |  7.9130s   |
  
  * Inverse Proportional Function  
  
    |     k      |     1      |     2      |     3      |     4      |     5      |
    | :--------: | :--------: | :--------: | :--------: | :--------: | :--------: |
    |    Mean    |  95.5400%  |  95.5400%  |  95.8550%  |  96.0000%  |  95.7250%  |
    |     SD     | 0.00073485 | 0.00073485 | 0.00227706 | 0.00224165 | 0.00316623 |
    | Total Time |  7.5410s   |  7.4490s   |  7.6050s   |  7.6700s   |  7.8181s   |

* **Sklearn LinearSVC** (dual=False, max_iter=1000)  

    |     k      |  PCA(0.9)  |    LDA     |
    | :--------: | :--------: | :--------: |
    |    Mean    |  90.6400%  |  90.3600%  |
    |     SD     | 0.00369662 | 0.00355528 |
    | Total Time |  2.6780s   |  1.8880s   |

* **Sklearn SVC** (kernel='rbf', gamma='scale', dfs='ovr')

    |     k      | PCA(0.85)  |  PCA(0.9)  |    LDA     |
    | :--------: | :--------: | :--------: | :--------: |
    |    Mean    |  96.7700%  |  96.7850%  |  92.6350%  |
    |     SD     | 0.00160779 | 0.00192743 | 0.00070000 |
    | Total Time |  8.5266s   |  12.5595s  |  3.4560s   |

* **Linear SVM Classifier** (ovr)
Overall Accuracy:
mean=96.7700%, std=0.00137555
Average Accuracy:
mean=95.9090%, std=0.00137555
total time: 769.3448s
