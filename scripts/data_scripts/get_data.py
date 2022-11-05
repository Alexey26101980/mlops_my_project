#!/usr/bin/python3

# Комментарий из VS Code

from catboost.datasets import titanic

train, test = titanic()

train.to_csv("/home/alexey/projects/mlops_my_project/data/raw/train.csv", index=False)

test.to_csv("/home/alexey/projects/mlops_my_project/data/raw/test.csv", index=False)
