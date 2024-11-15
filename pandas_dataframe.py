import pandas as pd

grades_dict={'A':4.0,'B':3.5,'C':3.0,'D':2.5}
grades=pd.Series(grades_dict)
print(grades)

marks_dict={'A':44,'B':35,'C':78,'D':85}
marks=pd.Series(marks_dict)
print(marks)
print("\nCreating a data frame :\n")
d=pd.DataFrame({'Marks':marks,'Grades':grades}) 
print(d)
print("\nInserting a new column :\n")

d['ScaledMarks']=100*(d['Marks']/90)            #adding one more column 
print(d)
print("\nAfter deleting the added column :\n")
del d['ScaledMarks']                            #deleting the added column 
print(d)

A=pd.DataFrame([{'a':1,'b':4},{'b':-3,'c':9}])
print(A)
print("\n Replacing NaN with 0 :\n")
B=A.fillna(0)
print(B)

print("\nPanda indexing :\n")

data=pd.Series(['a','b','c'],index=[1,3,5])
print(data[1])
print(data[1:3])
print(data.loc[1:3])