# -*- coding: utf-8 -*-
"""Project 1.4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IQT7axeYbABBjEVSLtR0XY1GNWCF5pGg
"""

# Regression Example With Boston Dataset: Baseline
import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
# load dataset
dataframe = pandas.read_csv("housing.csv", delim_whitespace=True, header=None)
dataset = dataframe.values
# split into input (X) and output (Y) variables
X = dataset[:,0:13]
Y = dataset[:,13]
# define base model
def baseline_model():
  # create model
  model = Sequential()
  model.add(Dense(13, input_dim=13, init= normal , activation= relu ))
  model.add(Dense(1, init= normal ))
  # Compile model
  model.compile(loss= mean_squared_error , optimizer= adam )
  return model
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# evaluate model with standardized dataset
estimator = KerasRegressor(build_fn=baseline_model, nb_epoch=100, batch_size=5, verbose=0)
kfold = KFold(n_splits=10, random_state=seed)
results = cross_val_score(estimator, X, Y, cv=kfold)
print("Baseline: %.2f (%.2f) MSE" % (results.mean(), results.std()))

# Regression Example With Boston Dataset: Standardized
import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
# load dataset
dataframe = pandas.read_csv("housing.csv", delim_whitespace=True, header=None)
dataset = dataframe.values
# split into input (X) and output (Y) variables
X = dataset[:,0:13]
Y = dataset[:,13]
# define base model
def baseline_model():
  # create model
  model = Sequential()
  model.add(Dense(13, input_dim=13, init= normal , activation= relu ))
  model.add(Dense(1, init= normal ))
  # Compile model
  model.compile(loss= mean_squared_error , optimizer= adam )
  return model    
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# evaluate model with standardized dataset
estimators = []
estimators.append(( standardize , StandardScaler()))
estimators.append(( mlp , KerasRegressor(build_fn=baseline_model, nb_epoch=50,
  batch_size=5, verbose=0)))
pipeline = Pipeline(estimators)
kfold = KFold(n_splits=10, random_state=seed)
results = cross_val_score(pipeline, X, Y, cv=kfold)
print("Standardized: %.2f (%.2f) MSE" % (results.mean(), results.std()))

# Regression Example With Boston Dataset: Standardized and Larger
import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
# load dataset
dataframe = pandas.read_csv("housing.csv", delim_whitespace=True, header=None)

dataset = dataframe.values
# split into input (X) and output (Y) variables
X = dataset[:,0:13]
Y = dataset[:,13]
# define the model
def larger_model():
  # create model
  model = Sequential()
  model.add(Dense(13, input_dim=13, init= normal , activation= relu ))
  model.add(Dense(6, init= normal , activation= relu ))
  model.add(Dense(1, init= normal ))
  # Compile model
  model.compile(loss= mean_squared_error , optimizer= adam )
  return model
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# evaluate model with standardized dataset
estimators = []
estimators.append(( standardize , StandardScaler()))
estimators.append(( mlp , KerasRegressor(build_fn=larger_model, nb_epoch=50, batch_size=5,
  verbose=0)))
pipeline = Pipeline(estimators)
kfold = KFold(n_splits=10, random_state=seed)
results = cross_val_score(pipeline, X, Y, cv=kfold)
print("Larger: %.2f (%.2f) MSE" % (results.mean(), results.std()))

# Regression Example With Boston Dataset: Standardized and Wider
import numpy
import pandas
from keras.models import Sequential

from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
# load dataset
dataframe = pandas.read_csv("housing.csv", delim_whitespace=True, header=None)
dataset = dataframe.values
# split into input (X) and output (Y) variables
X = dataset[:,0:13]
Y = dataset[:,13]
# define wider model
def wider_model():
  # create model
  model = Sequential()
  model.add(Dense(20, input_dim=13, init= normal , activation= relu ))
  model.add(Dense(1, init= normal ))
  # Compile model
  model.compile(loss= mean_squared_error , optimizer= adam )
  return model
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# evaluate model with standardized dataset
estimators = []
estimators.append(( standardize , StandardScaler()))
estimators.append(( mlp , KerasRegressor(build_fn=wider_model, nb_epoch=100, batch_size=5,
  verbose=0)))
pipeline = Pipeline(estimators)
kfold = KFold(n_splits=10, random_state=seed)
results = cross_val_score(pipeline, X, Y, cv=kfold)
print("Wider: %.2f (%.2f) MSE" % (results.mean(), results.std()))