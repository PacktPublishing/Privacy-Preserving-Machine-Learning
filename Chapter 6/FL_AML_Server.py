# -*- coding: utf-8 -*-
"""FL_AML_Server.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wz6qzzwEeadZYdWoniAqaODWBMFtIzrc
"""

import pandas as pd
import torch
url ="PS_20174392719_1491204439457_log.csv"
df_actual = pd.read_csv(url, sep=",")
df_actual

df_transactions=df_actual.head(25000)

from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit

print("No of Fraud Transactions:", df_transactions["isFraud"].value_counts()[0])
print("No of Non Fraud Transactions:", df_transactions["isFraud"].value_counts()[1])

print('No Frauds', round(df_transactions['isFraud'].value_counts()[0]/len(df_transactions) * 100,2), '% of the dataset')
print('Frauds', round(df_transactions['isFraud'].value_counts()[1]/len(df_transactions) * 100,2), '% of the dataset')

df_transactions.dtypes

from sklearn.preprocessing import LabelEncoder
encoder = {}
for i in df_transactions.select_dtypes('object').columns:
    encoder[i] = LabelEncoder()
    df_transactions[i] = encoder[i].fit_transform(df_transactions[i])

X = df_transactions.drop('isFraud', axis=1)
y = df_transactions['isFraud']

# Commented out IPython magic to ensure Python compatibility.

import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from imblearn.over_sampling import SMOTE
# %matplotlib inline

over_sample = SMOTE(random_state=0)
X,y = over_sample.fit_resample(X,y)

y.value_counts()

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

X = df_transactions[['step', 'type', 'amount', 'nameOrig','oldbalanceOrg', 'newbalanceOrig','nameDest', 'oldbalanceDest', 'isFlaggedFraud']]
y= df_transactions['isFraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Turn the values into an array for feeding the classification algorithms.
X_train = X_train.values
X_test = X_test.values
y_train = y_train.values
y_test = y_test.values

#from sklearn.linear_model import LogisticRegression
#log_reg = LogisticRegression()
#log_reg.fit(X_train,y_train)

#log_reg.score(X_test,y_test)

#### FLOWER SERVER PART ######.

from typing import Tuple, Union, List
import numpy as np
from sklearn.linear_model import LogisticRegression
import openml

XY = Tuple[np.ndarray, np.ndarray]
Dataset = Tuple[XY, XY]
LogRegParams = Union[XY, Tuple[np.ndarray]]
XYList = List[XY]

def get_model_parameters(model: LogisticRegression) -> LogRegParams:

    if model.fit_intercept:
        params = [
            model.coef_,
            model.intercept_,
        ]
    else:
        params = [
            model.coef_,
        ]
    return params


def set_model_params(
    model: LogisticRegression, params: LogRegParams
) -> LogisticRegression:

    model.coef_ = params[0]
    if model.fit_intercept:
        model.intercept_ = params[1]
    return model

def shuffle(X: np.ndarray, y: np.ndarray) -> XY:

    rng = np.random.default_rng()
    idx = rng.permutation(len(X))
    return X[idx], y[idx]


def partition(X: np.ndarray, y: np.ndarray, num_partitions: int) -> XYList:

    return list(
        zip(np.array_split(X, num_partitions), np.array_split(y, num_partitions))
    )

def set_initial_params(model: LogisticRegression):

    n_classes = 2  # Fraud Detection has only  classes
    n_features = 9  # Number of features in dataset
    model.classes_ = np.array([i for i in range(n_classes)])

    model.coef_ = np.zeros((n_classes, n_features))
    if model.fit_intercept:
        model.intercept_ = np.zeros((n_classes,))

import flwr as fl
#import utils
from sklearn.metrics import log_loss
from sklearn.linear_model import LogisticRegression
from typing import Dict


def fit_round(server_round: int) -> Dict:
    """Send round number to client."""
    return {"server_round": server_round}


def get_evaluate_fn(model: LogisticRegression,X_test,y_test):
    """Return an evaluation function for server-side evaluation."""

    # The `evaluate` function will be called after every round
    def evaluate(server_round, parameters: fl.common.NDArrays, config):
        # Update model with the latest parameters
        set_model_params(model, parameters)
        loss = log_loss(y_test, model.predict_proba(X_test))
        accuracy = model.score(X_test, y_test)
        return loss, {"accuracy": accuracy}

    return evaluate


# Start Flower server for five rounds of federated learning
def Server():
    model = LogisticRegression(max_iter=10000)
    set_initial_params(model)
    strategy = fl.server.strategy.FedAvg(
        min_available_clients=2,
        evaluate_fn=get_evaluate_fn(model,X_test,y_test),
        on_fit_config_fn=fit_round,
    )
    fl.server.start_server(
        server_address="0.0.0.0:8080",
        strategy=strategy,
        config=fl.server.ServerConfig(num_rounds=5),
    )

Server()






