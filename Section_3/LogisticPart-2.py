import math
import csv
import random

def load_csv(filename):
    dataset = list()
    
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            dataset.append(row)
    
    return dataset

def str_to_float(dataset):
    for row in range(len(dataset)):
        for col in range(len(dataset[0])):
            dataset[row][col] = float(dataset[row][col])


def minmax_dataset(dataset):
    minmax = []
    for i in range(len(dataset[0])):
        col = [row[i] for row in dataset]
        min_value = min(col)
        max_value = max(col)
        minmax.append([min_value, max_value])
        
    return minmax

def normalisation(dataset,minmax):
    numer = 0
    denom = 0
    for row in dataset:
        for col in range(len(row)):
            numer = row[col] - minmax[col][0]
            denom = minmax[col][1] - minmax[col][0]
            row[col] = numer/denom


# K-Fold cross validation
def cross_validation(dataset, n_folds):
    dataset_copy = list(dataset)
    fold_size = int(len(dataset) / n_folds)
    folds = list()
    for i in range(n_folds):
        fold = list()
        while len(fold) < fold_size:
            index = random.randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        folds.append(fold)
        
    return folds
            

filename = 'pima-indians-diabetes.data.csv'
dataset = load_csv(filename)
str_to_float(dataset)
minmax = minmax_dataset(dataset)
normalisation(dataset, minmax)

f = cross_validation(dataset, 5)




