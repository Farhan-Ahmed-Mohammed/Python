text=input("Enter text :")
def words(text):
    vowels=0
    consonents=0
    for i in text:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
        else:
            consonents=consonents+1
    print(f"The no of vowels are :{vowels}")
    print(f"The no of consonents are :{consonents}") 
words(text)       
