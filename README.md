# Privacy-Preserving Machine Learning

<a href="https://www.packtpub.com/product/privacy-preserving-machine-learning/9781800564671"><img src="(https://m.media-amazon.com/images/I/711kNKHPZ1L._SL1500_.jpg)" alt="no-image" height="256px" align="right"></a>

This is the code repository for [Privacy-Preserving Machine Learning](https://github.com/PacktPublishing/Privacy-Preserving-Machine-Learning), published by Packt.

**A use-case-driven approach to building and protecting ML pipelines from privacy and security threats**

## What is this book about?
Privacy regulations are evolving each year and compliance with privacy regulations is mandatory for every enterprise. Machine learning engineers are required to not only analyze large amounts of data to gain crucial insights, but also comply with privacy regulations to protect sensitive data. This may seem quite challenging considering the large volume of data involved and lack of in-depth expertise in privacy-preserving machine learning.

This book covers the following exciting features:
* Study data privacy, threats, and attacks across different machine learning phases
* Explore Uber and Apple cases for applying differential privacy and enhancing data security
* Discover IID and non-IID data sets as well as data categories
* Use open-source tools for federated learning (FL) and explore FL algorithms and benchmarks
* Understand secure multiparty computation with PSI for large data
* Get up to speed with confidential computation and find out how it helps data in memory attacks

If you feel this book is for you, get your [copy](https://www.amazon.com/Privacy-Preserving-Machine-Learning-approach-pipelines/dp/1800564678/ref=sr_1_4?crid=2A8M75FNMIZR7&dib=eyJ2IjoiMSJ9.zzun7F66YOxB9glIwxMIPK8FYp69fnR0s1KD5vnUy4x-FcAtzDW-_aPUIbNw5uhYSpuvgkv-haKt39vTBSZ1jSDzVM4xEwjI8CBUU42mzfnAbDICuAjDALg0MGARsTvd_dPxXKthr2oZvifBTGQDQrKa5UmFGeztAUDQYFqet72LiYnJ5X3re4hQtWerorspHQuACi-fALYTAeG1488y0ByjHh1vXgH43ovaxkH6rx0.uqVAl48etQfjfPxq6x8_48e18QCwJP6ItUaInRzs7Es&dib_tag=se&keywords=Privacy-Preserving+Machine+Learning&qid=1715837639&sprefix=privacy-preserving+machine+learning%2Caps%2C464&sr=8-4) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, Chapter02.

The code will look like the following:
```
import numpy as np 
from sklearn.linear_model import LinearRegression 
# Prepare sample input data with two features (feature 1, feature 2 
X = np.array([[10, 10], [10, 20], [20, 20], [20, 30]]) 
# Assume that target feature has some relationship with the input 
features with the formula y = 3 * x_1 + 5 * x_2 + 50 
y = np.dot(X, np.array([3, 5])) + 50

```

**Following is what you need for this book:**
This book is for data scientists, machine learning engineers, and privacy engineers who have working knowledge of mathematics as well as basic knowledge in any one of the ML frameworks (TensorFlow, PyTorch, or scikit-learn).

With the following software and hardware list you can run all code files present in the book (Chapter 2-10).
### Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| 2-10 | Python 3.7 or higher | Windows, macOS, or Linux |
| 2-10 | Jupyter Notebook |  Windows, macOS, or Linux |


### Related products
* Federated Learning with Python [[Packt]](https://www.packtpub.com/product/federated-learning-with-python/9781803247106) [[Amazon]](https://www.amazon.com/dp/180324710X)

* Machine Learning with PyTorch and Scikit-Learn [[Packt]](https://www.packtpub.com/product/machine-learning-with-pytorch-and-scikit-learn/9781801819312) [[Amazon]](https://www.amazon.com/dp/1801819319)

## Get to Know the Author
**Srinivas Rao Aravilli**
boasts 27 years of extensive experience in technology and leadership roles, 
spearheading innovation in various domains such as information retrieval, search, ML/AI, Generative 
AI, distributed computing, network analytics, privacy, and security. Currently serving as a senior 
director of machine learning engineering at Capital One, Bangalore, he has a proven track record of 
driving new products from conception to outstanding customer success. Prior to his tenure at Capital 
One, Srinivasa held prominent leadership positions at Visa, Cisco, and Hewlett Packard, where he led 
product groups focused on large-scale data, privacy, machine learning, and Generative AI. He holds 
a master’s degree in computer applications from Andhra University, Visakhapatnam, India.
I would like to thank the people who have been close to me and supported me, especially my family, 
parents, and my colleagues and team members.
