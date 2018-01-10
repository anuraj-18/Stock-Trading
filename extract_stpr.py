from urllib.request import urlopen
k=urlopen("file:///C:/Users/MAHE/Desktop/stpe.html")
t=k.read()
s=""
for i in range(len(t)):
    s=s+chr(t[i])
comp=s
ucomp=comp.upper()
urlgen="https://in.finance.yahoo.com/quote/"+comp+"?p="+ucomp 
k=urlopen("https://in.finance.yahoo.com/quote/"+comp+"?p="+ucomp)  
t=k.read() 

flag=0 
j=0 
count=0

for i in range(len(t)): 
    l="" 
    p="" 
    for j in range(i,i+18): 
        l=l+chr(t[j])
    if l=="data-reactid=\"36\">": 
        count=count+1
        if(count==2):
            while True: 
                if chr(t[j+1])=="<": 
                    flag=1 
                    break 
                
                p=p+chr(t[j+1])
                j=j+1 
    if flag==1: 
        break 

if(p==""):
    print("Invalid Symbol")    
else:
    print(p)


    
    