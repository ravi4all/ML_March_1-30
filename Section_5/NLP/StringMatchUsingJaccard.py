Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> text_1 = "Hello this is python programming and python is mainly used for machine learning and data science"
>>> text_2 = "Python is a very popular language among data scientist and used in machine learning heavily"
>>> token_1 = text_1.split()
>>> token_2 = text_2.split()
>>> token_1
['Hello', 'this', 'is', 'python', 'programming', 'and', 'python', 'is', 'mainly', 'used', 'for', 'machine', 'learning', 'and', 'data', 'science']
>>> token_2
['Python', 'is', 'a', 'very', 'popular', 'language', 'among', 'data', 'scientist', 'and', 'used', 'in', 'machine', 'learning', 'heavily']
>>> for i in range(len(token_1)):
	token_1[i] = token_1[i].lower()

	
>>> token_1
['hello', 'this', 'is', 'python', 'programming', 'and', 'python', 'is', 'mainly', 'used', 'for', 'machine', 'learning', 'and', 'data', 'science']
>>> for i in range(len(token_1_2)):
	token_2[i] = token_2[i].lower()

	
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    for i in range(len(token_1_2)):
NameError: name 'token_1_2' is not defined
>>> for i in range(len(token_2)):
	token_2[i] = token_2[i].lower()

	
>>> token_2
['python', 'is', 'a', 'very', 'popular', 'language', 'among', 'data', 'scientist', 'and', 'used', 'in', 'machine', 'learning', 'heavily']
>>> stopwords = ['is','am','are','the','and','or','in','this','that','for','a','used']
>>> list_1 = []
>>> list_2 = []
>>> for word in token_1:
	if word not in stopwords:
		list_1.append(word)

		
>>> for word in token_2:
	if word not in stopwords:
		list_2.append(word)

		
>>> list_1
['hello', 'python', 'programming', 'python', 'mainly', 'machine', 'learning', 'data', 'science']
>>> list_2
['python', 'very', 'popular', 'language', 'among', 'data', 'scientist', 'machine', 'learning', 'heavily']
>>> set_1 = set(list_1)
>>> set_1
{'python', 'hello', 'machine', 'mainly', 'data', 'learning', 'programming', 'science'}
>>> set_2 = set(list_2)
>>> set_2
{'python', 'popular', 'language', 'among', 'machine', 'data', 'scientist', 'heavily', 'learning', 'very'}
>>> set_1.intersection(set_2)
{'python', 'data', 'learning', 'machine'}
>>> s1 = set_1.intersection(set_2)
>>> s2 = set_2.union(set_2)
>>> s2
{'python', 'popular', 'language', 'among', 'machine', 'data', 'scientist', 'heavily', 'learning', 'very'}
>>> s2 = set_1.union(set_2)
>>> s2
{'python', 'hello', 'machine', 'popular', 'language', 'among', 'mainly', 'data', 'scientist', 'learning', 'heavily', 'very', 'programming', 'science'}
>>> len(s1) / len(s2)
0.2857142857142857
>>> 
