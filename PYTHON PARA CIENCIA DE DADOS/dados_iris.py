# -*- coding: utf-8 -*-
"""Dados Iris.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gAZOrQCj6nmJ1UBYgyj0xsb8q1-sfDyU
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", names = ["Sepal Length","Sepal Width", "Petal Length", "Petal Width", "Class"])
df.head()

df.shape

df.dtypes

df.groupby("Class").mean()

df.groupby("Class")["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"].sum().plot.bar(title="Características por Classe");