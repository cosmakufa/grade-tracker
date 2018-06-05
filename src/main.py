from pymongo import MongoClient
from bson.objectid import ObjectId

#connect to database
client = MongoClient('mongodb://localhost:27017')

#get the collection
grades = client.tracker.grades

'''
for _ in range(3):
    name = input('student name: ')
    subject =input('student class: ')
    grade = float(input('grade: '))
    d = {'name': name, 'class': subject, 'grade': grade}
    print(name,subject,grade)

    #insert a grade into the database
    grades.insert_one(d)
'''
#
for g in grades.find():
    print('g is', g['grade'])
import numpy as np
print('sum', sum([g['grade'] for g in grades.find()]))
print('mean', np.mean([g['grade'] for g in grades.find()]))
