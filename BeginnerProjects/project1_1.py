# -*- coding: utf-8 -*-
"""Project1.1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f8LuJUzCHZ_svTNplc1Mq-ebw8KFN2Uo
"""

import pandas as pd
import numpy as np

# read the text file into a list of strings, with each line being an element in the list
with open('/content/pinaindiansdiabetes.txt', 'r') as file:
    lines = file.readlines()

# create a dataframe from the list of strings
df = pd.DataFrame(lines, columns=['Column_name'])

# split the values in the column 'column_name' on commas
new_cols = df['Column_name'].str.split(',', expand=True)

# add the new columns to the original dataframe
df = pd.concat([df, new_cols], axis=1)

# remove the original column 'column_name'
df.drop('Column_name', axis=1, inplace=True)

# set the first row as column names
df.columns = df.iloc[0]

# drop the first row (now the column names)
df = df.drop(df.index[0])

# print the resulting dataframe
df.head()

# split into input (X) and output (Y) variables
X = df.iloc[:,0:8]
Y = df.iloc[:,8]

# create model
model = Sequential()
model.add(Dense(12, input_dim=8, init= uniform , activation= relu ))
model.add(Dense(8, init= uniform , activation= relu ))
model.add(Dense(1, init= uniform , activation= sigmoid ))
# Compile model
model.compile(loss= binary_crossentropy , optimizer= adam , metrics=[ accuracy ])
# Fit the model
model.fit(X, Y, nb_epoch=150, batch_size=10)
# evaluate the model
scores = model.evaluate(X, Y)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))