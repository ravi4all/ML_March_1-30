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

def test_split(index,value,dataset):
    left, right = list(), list()    
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)    
    return left, right

def gini_index(class_values, groups):
    gini = 0.0    
    for class_value in class_values:
        for group in groups:        
            size = len(group)
            
            if size == 0:
                continue
            
            p = [row[-1] for row in group].count(class_value) / float(size)
            gini += p * (1.0 - p)
    
    return gini    

def get_split(dataset):
    
    class_value = list(set([row[-1] for row in dataset]))
    b_score,b_value,b_index,b_group = 999,999,999,None
    
    for index in range(len(dataset[0]) - 1):
        for row in dataset:
            groups = test_split(index,row[index],dataset)
            gini = gini_index(class_value,groups)
            
        if gini < b_score:
            b_index, b_value, b_score, b_group = index, row[index], gini, groups
        
    return {'score':b_score, 'value':b_value, 'index':b_index, 'groups':b_group} 
    
    
def to_terminal(group):
    outcome = [row[-1] for row in group]
    return max(set(outcome),key=outcome.count)

def split(depth,node,max_depth,min_size):
    
    left, right = node['groups']
    del node['groups']
    
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        return
    
    if depth > max_depth:
        node['left'], node['right'] = to_terminal(left), to_terminal(right)
        return
    
    if len(left) <= min_size:
        node['left'] = to_terminal(left)
    else:
        node['left'] = get_split(left)
        split(depth+1,node['left'],max_depth,min_size)
    
    if len(right) <= min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_split(right)
        split(depth+1,node['right'],max_depth,min_size)
    

def build_tree(train,max_depth,min_size):
    root = get_split(train)
    split(1,root,max_depth,min_size)
    return root


def predict():
    pass

def random_forest():
    pass

def bagging_predict():
    pass



dataset = [
        [2.7810836,2.550537003,0],
    	[1.465489372,2.362125076,0],
    	[3.396561688,4.400293529,0],
    	[1.38807019,1.850220317,0],
    	[3.06407232,3.005305973,0],
    	[7.627531214,2.759262235,1],
    	[5.332441248,2.088626775,1],
    	[6.922596716,1.77106367,1],
    	[8.675418651,-0.242068655,1],
    	[7.673756466,3.508563011,1]
    ]

max_depth = 10
min_size = 1

root_node = build_tree(dataset,max_depth,min_size)

filename = 'german_credit.csv'
dataset = load_data(filename)
str_to_float(dataset)