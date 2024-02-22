#!/usr/bin/python3

from catboost.datasets import titanic

train, test = titanic()

train.to_csv("datasets/raw/train.csv", index=False)

test.to_csv("datasets/raw/test.csv", index=False)
