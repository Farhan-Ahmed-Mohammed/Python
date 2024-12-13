f=open(r"C:\Users\Jameel\Desktop\Python\demo.txt","r")
freq={}
data=f.read()
data1=data.lower()
for i in data1:
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i]=1
print(freq)            