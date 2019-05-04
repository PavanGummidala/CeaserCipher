ptext = 'A hello y how are you z'
enc= []
k=3
dec=[]


def eabc(s,k):
    if (ord(s)>=97) and (ord(s)<=122):        
        x=ord(s)-96
        abc=(x+k)%96
        chr(abc)
        y=chr(abc+96)
        enc.append(y)
    elif (ord(s)>=65) and (ord(s)<=90): 
        x=ord(s)-64
        abc=(x+k)%64
        chr(abc)
        y=chr(abc+64)
        enc.append(y)
    elif (ord(s)==32):
        y=chr(ord(s))
        enc.append(y)        

def dabc(s,k):
    if (ord(s)>96) and (ord(s)<=(122+k)):
        x=ord(s) +96
        abc=(x-k)%96
        chr(abc)
        y=chr(abc+96)
        dec.append(y)
    elif (ord(s)>=65) and (ord(s)<=90):
        x=ord(s) +64
        abc=(x-k)%64
        chr(abc)
        y=chr(abc+64)
        dec.append(y)
    elif(ord(s)==32):
        y=chr(ord(s))
        dec.append(y)
    
for i in range(len(ptext)):
    eabc(ptext[i],k)               
    i=+1
    
ctext = "".join(enc)
print('Encoded:',ctext) 


for i in range(len(enc)):
    dabc(enc[i],k)    
    i+=1

decoded= "".join(dec)
print("Decoded:",decoded)

