import math
import csv
import random

def load_data(path):
    dataset = []
    with open(path) as file:
        data = csv.reader(file)
        for row in data:
            if not row:
                continue
            dataset.append(row)
    return dataset

def str_to_float(dataset):
    for row in dataset:
        for col in range(len(row)):
            row[col] = float(row[col])

def cross_validation(dataset, n_folds):
    folds = []
    size = int(len(dataset) / n_folds)
    dataset_copy = list(dataset)
    
    for i in range(n_folds):
        fold = []
        while len(fold) < size:
            index = random.randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        folds.append(fold)
    
    return folds
    
def accuracy_metrics(actual,predicted):
    score = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            score += 1
    
    return score / len(actual) * 100

def evaluate_algorithm(dataset,n_folds,algorithm):
    scores = []
    folds = cross_validation(dataset,n_folds)
    
    for fold in folds:
        train = list(folds)
        train.remove(fold)
        train = sum(train,[])
        test = []
        for row in fold:
            row_copy = list(row)
            row_copy[-1] = None
            test.append(row_copy)
        
        predicted = predict(train, test)
        actual = [row[-1] for row in fold]
        score = accuracy_metrics(actual, predicted)
        scores.append(score)
    
    return scores

def  train_test():
    pass

def gini_index(class_values, group):
    gini = 0.0
    
    for class_value in class_values:
        p = count(class_value) / len(group)
        gini = sum(p * (1.0 - p))
    
    return gini
    

def get_split():
    pass

def decision_tree():
    pass


def predict():
    pass

filename = 'german_credit.csv'
dataset = load_data(filename)
str_to_float(dataset)