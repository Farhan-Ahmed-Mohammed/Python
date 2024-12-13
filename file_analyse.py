def analysefile(file1,file2):
    wfile1=set()
    wfile2=set()

    with open(file1,"r") as file:
        for line in file:
            words=line.split()
            wfile1.update(words)

    with open(file2,"r") as file:
        for line in file:
            words=line.split()
            wfile2.update(words)    

    common=wfile1.intersection(wfile2)
    uniquef1=wfile1.difference(wfile2)
    uniquef2=wfile2.difference(wfile1)
    

    print("Common words are :")
    print(common)    

    print("\nThe unique words in file1 are :")
    print(uniquef1)

    print("\nThe unique words in file2 are :")
    print(uniquef2)

file1=r"C:\Users\Jameel\Desktop\Python\demo.txt"      
file2=r"C:\Users\Jameel\Desktop\Python\demo2.txt"     
analysefile(file1,file2)      
