#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:10:58 2020

@author: parth
"""
import tkinter as tk
from tkinter import Menu,filedialog,Text




win=tk.Tk()

win.minsize(500,500)
win.resizable(0,0)
win.title('Key Management using PSO')

text0=Text(win,height=2)
text0.insert(tk.INSERT,'Open the file for encryption/decryption:\n')
text0.pack()


def openfile():
    file = filedialog.askopenfile()
    f=open(file.name,'r')
    text1=Text(win,height=1)
    text1.insert(tk.INSERT,'The text in the file is:\n')
    text1.pack()
    #file0 = open('plaintext.txt','w')
    #file0.write(str(input()))
    #file0.close()
    text2=Text(win,height=5)
    text2.insert(tk.INSERT,f.read())
    text2.pack()
    #return(f.read())
    #Label(win,text=f.read()).grid(row=0,column=0,sticky='nw')


def _quit():  
    win.quit()  
    win.destroy()  
    exit()  
       
    
def encryption():
        
#open the plain text document 
    file1 = filedialog.askopenfile()
    f2=open(file1.name,'r')
    if f2 is not None:
        contents=''
        contents=file1.read()
        
#index of spaces for later use
    l=[]
    for i in range(len(contents)):
        if(contents.find(' ',i,i+1 )!=-1):
            l.append(contents.find(' ',i,i+1 ))
    
        
#plain text into list without spacebar
    e=[]
    for i in contents:
        if(i!=' ' and i!='\n'):
            e.append(i)
#print(e)
    
    
    
#binary code of plain text(without spacebar) into list
    st=(str(''.join(format(ord(i),'b') for i in e)))
    c=list()
    for i in st:
        if(i!=' '):
            c.append(int(i))
    
#generation of crossover and mutation points
    import random
    key=[]
    while(len(key)<4):
        r1=random.randint(0,13)
        if(r1 not in key):
            key.append(r1)
    key.sort()
    
    for k in range(3):
        key.append(k)
        
    for i in range(4,7):
        r2=random.randint(0,13)
        key[i]=r2
    
    
#calculation of p_best and g_best
    p_best=[]
    _size = len(key) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if (key[i] == key[j] and key[i] not in repeated): 
                repeated.append(key[i])
    count=0
    
    for i in repeated:
        start_at = -1
        locs = []
        j=0
        k=j+1
        count=key.count(i)
        flag=0
        while (flag<count):
            loc = key.index(i,start_at+1,_size)
            locs.append(loc)
            start_at = loc
            flag=flag+1
    
            while(k<len(locs)):
                pos_diff=locs[j+1]-locs[j]
                p_best.append(pos_diff)
                j=j+1
                k=k+1
    if(len(p_best)==0):
        g_best=7
    elif(len(p_best)!=0):
        g_best=min(p_best)
    
#public key generation
    key1=[]
    for i in range(len(key)):
        key1.append(key[i])
    key1.append(g_best)
    
    public_key=[]
    for i in key1:
        public_key.append(i)
        public_key.append((i+g_best)%14)
    
    hexa_public_key=[]
    for i in range(len(public_key)):
        if(public_key[i]==10):
            hexa_public_key.insert(i,'A')
        elif(public_key[i]==11):
            hexa_public_key.insert(i,'B')
        elif(public_key[i]==12):
            hexa_public_key.insert(i,'C')
        elif(public_key[i]==13):
            hexa_public_key.insert(i,'D')        
        elif(public_key[i]==14):
            hexa_public_key.insert(i,'E')
        elif(public_key[i]==15):
            hexa_public_key.insert(i,'F')    
        else:
            hexa_public_key.append(public_key[i])

    s1 = [str(i) for i in hexa_public_key] 
    final_public_key= str("".join(s1))
    #print(final_public_key)
    text3=Text(win,height=1)
    text3.insert(tk.INSERT,'The public key is:\n')
    text3.pack()
    text4=Text(win,height=2)
    text4.insert(tk.INSERT,final_public_key)
    text4.pack()

    file2 = open('publickey.txt','w')
    file2.write(final_public_key)
    file2.close()
    

    
#distribution of binary coded plain text into matrix for encryption
    a=[0]*14
    b=[0]*14
    encrypt=[]
    q=int(len(c)//28)
    r=int(len(c)%28)
    q1=-1
    r1=-1
    if(r>0):
        q1=int(r//14)
        r1=int(r%14)
    flag=0
    i=0
    while True:
        a=[0]*14
        b=[0]*14
        if(flag<q):
            a=[0]*14
            b=[0]*14
    
            for j in range(14):
                a[j]=c[14*2*i+j]
                b[j]=c[14*(2*i+1)+j]
            i=i+1
            flag=flag+1
#crossover and mutation
            for x in range(4):
                a[key[x]],b[key[x]]=b[key[x]],a[key[x]]
            for y in range(3):
                a[key[y+4]]=1-a[key[y+4]]
                b[key[y+4]]=1-b[key[y+4]]
    
            for z in a:
                encrypt.append(z)
            for z in b:
                encrypt.append(z)
            
        elif(flag==q):
            if(q1==0):
                a=[0]*14
                b=[0]*14
                for k in range(r1):
                    a[k]=c[28*q+k]
                flag=flag+1

                for x in range(4):
                    a[key[x]],b[key[x]]=b[key[x]],a[key[x]]
                for y in range(3):
                    a[key[y+4]]=1-a[key[y+4]]
                    b[key[y+4]]=1-b[key[y+4]]
        
                for z in a:
                    encrypt.append(z)
                for z in b:
                    encrypt.append(z)                
                    
            elif(q1==1):
                a=[0]*14
                b=[0]*14
                for m in range(14):
                    a[m]=c[28*q+m]
                for t in range(r1):
                    b[t]=c[28*q+14+t]
                flag=flag+1
#crossover and mutation
                for x in range(4):
                    a[key[x]],b[key[x]]=b[key[x]],a[key[x]]
                for y in range(3):
                    a[key[y+4]]=1-a[key[y+4]]
                    b[key[y+4]]=1-b[key[y+4]]
        
                for z in a:
                    encrypt.append(z)
                for z in b:
                    encrypt.append(z)                    
            
            else:
                flag=flag+1

            
        elif(flag>q):
            break

    
#cipher text generation
    s = [str(i) for i in encrypt] 
    bin_data= str("".join(s))
    file5=open('cipherlist.txt','w')
    file5.write(bin_data)
    file5.close()
    str_data =''
    for i in range(0, len(bin_data), 7):
        temp_data = bin_data[i:i + 7]

        decimal_data= int(temp_data, 2)

        str_data = str_data + chr(decimal_data)

    
    lst=[]
    for i in str_data:
        lst.append(i)

    
    j=0
    for i in range(len(l)):
        lst.insert(l[i]+j,' ')
        j=j+1
    
    st= [str(i) for i in lst] 
    cipher_text= str("".join(st))
    file3=open('ciphertext.txt','w')
    file3.write(cipher_text)
    file3.close()    
    
#print(cipher_text)
    
    text5=Text(win,height=1)
    text5.insert(tk.INSERT,'The cipher text is:\n')
    text5.pack()
    text6=Text(win,height=5)
    text6.insert(tk.INSERT,cipher_text)
    text6.pack()


#private key generation
    contents1=final_public_key
    l=[]
    for i in contents1 :
        l.append(i)
    #print(l)
    hexa_private_key=[]
    for i in range(0,len(l)-2,2):
        hexa_private_key.append(l[i])
    hexa_private_key=hexa_private_key[::-1]
    #print(hexa_private_key)
    s1 = [str(i) for i in hexa_private_key] 
    final_private_key= str("".join(s1))
    #print(final_private_key)
    file4 = open('privatekey.txt','w')
    file4.write(final_private_key)
    file4.close()
    
def decryption():
    
    text7=Text(win,height=1)
    text7.insert(tk.INSERT,'The private key is:\n')
    text7.pack()
    file6=open('privatekey.txt','r')
    if file6 is not None:
        contents2=''
        contents2=file6.read() 
    text8=Text(win,height=1)
    text8.insert(tk.INSERT,contents2)
    text8.pack() 
    
    file7=open('cipherlist.txt','r')
    if file7 is not None:
        contents3=''
        contents3=file7.read()
    l=[]
    for i in contents3:
        l.append(i)
        
#open the plain text document 
    file8 = open('plaintext.txt','r')
    if file8 is not None:
        contents4=''
        contents4=file8.read()
        
#index of spaces for later use
    gap=[]
    for i in range(len(contents4)):
        if(contents4.find(' ',i,i+1 )!=-1):
            gap.append(contents4.find(' ',i,i+1 ))
    
    file9=open('privatekey.txt','r')
    if file9 is not None:
        contents5=''
        contents5=file9.read()
    hexa_private_key=[]
    for i in contents5:
        hexa_private_key.append(i)
        
    keyp=[]
    

    for i in range(len(hexa_private_key)):
 
        if(hexa_private_key[i]=='A'):
            keyp.insert(i,int(10))
        elif(hexa_private_key[i]=='B'):
            keyp.insert(i,int(11))
        elif(hexa_private_key[i]=='C'):
            keyp.insert(i,int(12))
        elif(hexa_private_key[i]=='D'):
            keyp.insert(i,int(13))
        elif(hexa_private_key[i]=='E'):
            keyp.insert(i,int(14))
        elif(hexa_private_key[i]=='F'):
            keyp.insert(i,int(15))
        else:
            keyp.insert(i,int(hexa_private_key[i]))


    decrypt=[]
    q1=int(len(l)//28)
    flag1=0
    i=0
    while True:
        if(flag1<q1):
            a=[0]*14
            b=[0]*14
    
            for j in range(14):
                a[j]=int(l[14*2*i+j])
                b[j]=int(l[14*(2*i+1)+j])
            i=i+1
            flag1=flag1+1  
            
    #re-mutation and re-crossover
            for y in range(3):
                a[keyp[y]]=1-a[keyp[y]]
                b[keyp[y]]=1-b[keyp[y]]
                
            for x in range(3,7):
                a[keyp[x]],b[keyp[x]]=b[keyp[x]],a[keyp[x]]
                
            
            for z in a:
                decrypt.append(z)
            for z in b:
                decrypt.append(z) 
        else:
            break
       
    #decrypt cipher text generation
    s = [str(i) for i in decrypt] 
    bin_data= str("".join(s))
    str_data=''
    for i in range(0, len(decrypt), 7):
        temp_data = bin_data[i:i + 7]
    
        decimal_data= int(temp_data, 2)
    
        str_data = str_data + chr(decimal_data)
    lst=[]
    for i in str_data:
        lst.append(i)
    
    for i in range(len(gap)):
        lst.insert(gap[i],' ')

        
    st= [str(i) for i in lst] 
    decrypt_text= str("".join(st)) 
    
    file4 = open('decryptext.txt','w')
    file4.write(decrypt_text)
    file4.close()
    
def show_decrypt_text():

    text1=Text(win,height=1)
    text1.insert(tk.INSERT,'The decrypted text is available in command shell:\n')
    text1.pack()
    #file0 = open('plaintext.txt','w')
    #file0.write(str(input()))
    #file0.close()
        
    file = filedialog.askopenfile()
    f=open(file.name,'r')
    print(f.read())

    
menuBar=Menu(win)  
win.config(menu=menuBar)  


fileMenu= Menu(menuBar, tearoff=0)  
fileMenu.add_command(label="New", command=openfile)  
fileMenu.add_separator()  
fileMenu.add_command(label="Exit", command=_quit)  
menuBar.add_cascade(label="File", menu=fileMenu)  

securityMenu= Menu(menuBar, tearoff=0)  
securityMenu.add_command(label="Encrypt",command=encryption) 
securityMenu.add_separator()  
securityMenu.add_command(label="Decrypt",command=decryption)
menuBar.add_cascade(label="Security", menu=securityMenu)  

showMenu= Menu(menuBar, tearoff=0)
showMenu.add_command(label="Decrypt Text",command=show_decrypt_text) 
menuBar.add_cascade(label="Show", menu=showMenu) 


win.mainloop()



