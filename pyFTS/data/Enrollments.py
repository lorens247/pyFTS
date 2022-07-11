"""
Yearly 
"""

from pyFTS.data import common
import pandas as pd
import numpy as np


def get_data():
    """
    Get a simple univariate time series data.

    :return: numpy array
    """
    dat = get_dataframe()
    dat = np.array(dat["Enrollments"])
    return dat


def get_dataframe():
    dat = common.get_dataframe('Enrollments.csv',
                               'https://raw.githubusercontent.com/lorens247/pyFTS/master/pyFTS/data/Enrollments.csv',
                               sep=";")
    return dat
