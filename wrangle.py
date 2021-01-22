import pandas as pd
import numpy as np
import scipy as sp 
import os

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
import acquire
import prepare

import sklearn



####### Split dataframe ########
def split(df, target_var):
    '''
    This splits the dataframe for train, validate, and test, and creates X and y dataframes for each
    '''
    # split df into train_validate (80%) and test (20%)
    train_validate, test = train_test_split(df, test_size=.20, random_state = 123, stratify=df.language)
    # split train_validate into train(70% of 80% = 56%) and validate (30% of 80% = 24%)
    train, validate = train_test_split(train_validate, test_size=.25, random_state = 123, stratify=train_validate.language)
    
    # create X_train by dropping the target variable 
    X_train = train.drop(columns=[target_var])
    # create y_train by keeping only the target variable.
    y_train = train[[target_var]]

    # create X_validate by dropping the target variable 
    X_validate = validate.drop(columns=[target_var])
    # create y_validate by keeping only the target variable.
    y_validate = validate[[target_var]]

    # create X_test by dropping the target variable 
    X_test = test.drop(columns=[target_var])
    # create y_test by keeping only the target variable.
    y_test = test[[target_var]]
    
    # for explore create copy of train without x/y split
    train_exp = train.copy()
    return train_exp, X_train, y_train, X_validate, y_validate, X_test, y_test



##### for GitHub project
def wrangle_github(cached=True):
    print('acquiring data')
    df = acquire.get_github2(cached)
    print('preparing data')
    df = prepare.prep_data(df, 'content', extra_words=['file', 'environmental', 'data'], exclude_words=[])
    print('splitting data')
    train_exp, X_train, y_train, X_validate, y_validate, X_test, y_test = split(df, 'language')
    print('complete')
    print('X-train shape', X_train.shape, 'X_validate shape', X_validate.shape, 'X_test shape', X_test.shape)
    return  train_exp, X_train, y_train, X_validate, y_validate, X_test, y_test