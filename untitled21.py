# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 00:39:15 2024

@author: Avinash T
"""

from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
import seaborn as sns
from pyspark.ml.feature import StringIndexer
from pyspark.sql.functions import col, isnan, when, count
from pyspark.ml import Pipeline

spark = SparkSession.builder \
    .appName("collab").getOrCreate()
spark

dementiaData = spark.read.csv('mentalhealth.csv',header=True,inferSchema=True)
dementiaData.show()

import pandas as pd
dataframe = dementiaData.toPandas()
dataframe.head()
