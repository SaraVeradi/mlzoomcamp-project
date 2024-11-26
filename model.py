# -*- coding: utf-8 -*-
"""model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xTfl4faRJWQbcAaBdRVdri4eQlGGG6HX
"""

# ==============================================================================
# # importing libraries functions for data preparation and training
# ==============================================================================

import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection    import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing      import StandardScaler
from sklearn.metrics            import root_mean_squared_error
from sklearn.preprocessing      import PolynomialFeatures
from sklearn.linear_model       import LinearRegression


# loading data, the target data here is calories.csv and features are
#  exercise
calories = pd.read_csv('calories.csv')
exercise = pd.read_csv('exercise.csv')


# ==============================================================================
# Preparing data for Trining
# ==============================================================================
print("preparing data")
# making a feature matrix and final target matrix
features = exercise.drop(['User_ID'], axis=1)
target = calories.drop(['User_ID'], axis=1)

# making features's and target's  titles lower case
features.columns = features.columns.str.lower()
target.columns = target.columns.str.lower()

# height accoriding to SI unit
features['height'] = features['height']/100

# defining BMI
features['bmi'] = features['weight']/(features['height']**2)


# split features and target in training, test and validation sets
features_full_train, features_test, target_full_train, target_test = train_test_split(
                                                           features,
                                                           target,
                                                           test_size=0.2,
                                                           random_state=42)
features_train, features_val, target_train, target_val = train_test_split(
                                                           features_full_train,
                                                           target_full_train,
                                                           test_size=0.25,
                                                           random_state=42)
# ==============================================================================
# One-Hot encoding
# ==============================================================================

dv = DictVectorizer(sparse=False)
## one-hot endocding for training data
train_dicts  = features_train.to_dict(orient='records')
X_train      = dv.fit_transform(train_dicts)

## one-hot encoding for validation data
val_dicts  = features_val.to_dict(orient='records')
X_val      = dv.transform(val_dicts)

## one-hot encoding for test data
test_dicts  = features_test.to_dict(orient='records')
X_test      = dv.transform(val_dicts)

# ==============================================================================
# Scaling
# ==============================================================================

scaler = StandardScaler(copy=False, with_mean=True, with_std=True)
scaled_X_train  = scaler.fit_transform(X_train)
scaled_X_test   = scaler.transform(     X_test)
scaled_X_val    = scaler.transform(      X_val)


# ==============================================================================
# Training
# ==============================================================================
print("training")
lin_reg = LinearRegression()

for model_degree in [4]:
    print('model degree %d'% model_degree)
    poly_features = PolynomialFeatures(degree=model_degree, include_bias=False)
    X_poly = poly_features.fit_transform(scaled_X_train)

    lin_reg.fit(X_poly, target_train)
    lin_reg.intercept_, lin_reg.coef_

    X_poly_val = poly_features.fit_transform(scaled_X_val)

    y_pred = lin_reg.predict(X_poly_val)
    print(root_mean_squared_error(target_val, y_pred))
    y_pred = lin_reg.predict(X_poly)
    print(root_mean_squared_error(target_train, y_pred))
    print("\n")


# ==============================================================================
# Saving The Output
# ==============================================================================
output_file = "calories.bin"
f_out = open(output_file, 'wb')
pickle.dump((dv, lin_reg), f_out)
f_out.close()