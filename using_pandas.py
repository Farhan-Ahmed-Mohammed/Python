import pandas as pd

a=pd.Series([11,2,34,47],index=['a','b','c','d'])
print(a)
print(a.values)
print(a.index)
print(f"The value at b is :{a['b']}")

#using dictionary
grades_dict={'A':4,'B':3,'C':2,'D':1}
grades=pd.Series(grades_dict)
print(grades)
print(grades.values)
print(grades['A'])