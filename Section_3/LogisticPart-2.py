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
            
def accuracy_metrics(predicted, actual):
    count = 0
    for i in range(len(predicted)):
        if predicted[i] == actual[i]:
            count += 1
    return count / len(actual) * 100



def prediction(row,coef):
    ycap = coef[0]    
    for i in range(len(row) - 1):
        ycap += coef[i + 1] * row[i]    
    return 1 / (1 + math.exp(-ycap))


def evaluate_algorithm(dataset,algorithm, n_folds, learning_rate,nb_epoch):
    scores = []
    folds = cross_validation(dataset,n_folds)
    for fold in folds:
        train = list(folds)
        train.remove(fold)
        train = sum(train,[])
        test = list()
        for row in fold:
            row_copy = list(row)
            row_copy[-1] = None
            test.append(row_copy)
            
        predicted = algorithm(train,test,learning_rate,nb_epoch)
        actual = [row[-1] for row in fold]
        
        score = accuracy_metrics(predicted, actual)
        scores.append(score)
    
    return scores



def sgd_logistic(dataset,learning_rate,nb_epoch):
    coef = [0] * len(dataset[0])
    
    for epoch in range(nb_epoch):
        for row in dataset:
            ycap = prediction(row,coef)
            y = row[-1]
            coef[0] = coef[0] + learning_rate * (y - ycap) * ycap * (1 - ycap)
            
            for i in range(len(row)-1):
                coef[i+1] = coef[i+1] + learning_rate * (y - ycap) * ycap * (1 - ycap) * row[i]
                
    return coef


def logistic_regression(train,test,learning_rate,epoch):
    predicted_y = []
    coef = sgd_logistic(train,learning_rate,epoch)
    
    for row in test:
        ycap = prediction(row,coef)
        ycap = round(ycap)
        predicted_y.append(ycap)
    return predicted_y
    


filename = 'pima-indians-diabetes.data.csv'
dataset = load_csv(filename)
str_to_float(dataset)
minmax = minmax_dataset(dataset)
normalisation(dataset, minmax)

n_folds = 5
learning_rate = 0.01
nb_epoch = 1000
scores = evaluate_algorithm(dataset,logistic_regression, n_folds, learning_rate,nb_epoch)
print(scores)

avg_score = sum(scores) / len(scores)
print("Accuracy is",avg_score)