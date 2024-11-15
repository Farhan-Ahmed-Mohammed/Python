f=open(r"C:\Users\Jameel\Desktop\Python\demo.txt","r")
data1=f.read()      #reads the complete data of file
print(data1)
print(type(data1))
#data2=f.read(5)  if we write like this it dont read first 5 chatecters here  becoz the file pointer 
# already read everything and pointer is now at the end of the file
f.close()

f=open(r"C:\Users\Jameel\Desktop\Python\demo.txt","w") # if we open a file which dont exist in w 
# a mode then pyhhon automatically creates a file
f.write("The data of file is replaced with this line now bcoz we used f.write and file is opened in append mode, check by opening demo file in nodepad \n")
f.close()

f=open(r"C:\Users\Jameel\Desktop\Python\demo.txt","a")
f.write("Now that old data is not replaced becoz we opened file in append mode")
f.close()

f=open(r"C:\Users\Jameel\Desktop\Python\demo.txt","r+")#r+ mode brings pointer to starting of file
f.write("abc") # now the starting three letters of file T h e is replced by abc
print(f.read()) # now pointer is after abc so it prints every thing after abc
f.close()

f=open(r"C:\Users\Jameel\Desktop\Python\demo.txt","w+")# whole file becomes empty if we open in this mode
print(f.read()) 
f.write("The old data is removed bcoz we opened file in w+ mode\n")
f.close()

f=open(r"C:\Users\Jameel\Desktop\Python\demo.txt","a+") # it puts pointer to the end of file 
print(f.read()) # it dont print anything bcoz the pointer is at the end 
f.write("Now it is not over writing bcoz we open in append mode")
f.close()