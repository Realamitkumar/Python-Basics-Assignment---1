#!/usr/bin/env python
# coding: utf-8

# In[9]:


range(10)


# In[16]:


list(range(1,11))


# In[18]:


list(range(10,3,-1))


# In[44]:


l=[1, 2, 3, 4, 5, 6]

#l[::-1] #if want to reverse

m = []

for i in l:
    i+=2
    m.append(i)


# In[45]:


m


# In[65]:


#range() with For Loop

l=[5, 2, 3, 4, 5, 6]
m = []

for i in range(len(l)):
    n=l[i]
    m.append(n)


# In[66]:


m


# In[85]:


#if condition

l=[5, 2, 3, 4, 5, 6]
m = []

for i in range(len(l)):
    if i >= 4: 
        m.append(l[i]+2)


# In[84]:


m


# In[96]:


l=[5, 2, 3, 4, 5, 6,"sudh"]
m=[]

for i in l:
    if type(i)==str: 
        m.append(i)


# 

# In[97]:


m


# In[105]:


#WHile loop
d=10
s=0
i=1
while i<=d:
    s = s + i
    i = i + 1
print(s)    


# In[120]:


#for-else Condition
for x in "sudh":
    if x == "d":
        break # stop at that moment
    print(x)
else:
    print("I am unable to complete iteration") 
print("out of the loop")    


# In[121]:


for x in "sudh":
    if x == "d":
        continue #skip & contnue with others
    print(x)  


# In[154]:


# Input Operation
a = int(input("Insert integer only "))
l = [1,2,3,4,5,6,7,5,5,5,6,7,8,9,9]
m = []

for i in l :
    if i == a:
        m.append(i)    
m


# In[161]:


"sudh" + str(1)


# In[165]:


[1,2,3]+"sudh"


# In[168]:


str("1,2,3") +"sudh"


# In[169]:


[1,2,3]+["sudh"]


# # Q1
# ``Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.``

# In[59]:


c=[]
for i in range(2000,3201):
    if (i%7==0) and (i%5!=0):
            c.append(str(i))
print(",".join(c))            


# # Q2:
# ``Write a Python program which accepts the 
# user’s first and last name and print them in reverse order``

# In[81]:


#1
first = input("Enter First Name Here/n")
last = input("Enter Last Name Here/n")
#2 Spacing 
r = first + " "+ last
#3
s=r[::-1]
#Result
r


# # Q3:
# ``Write a Python program to 
# find the volume of a sphere
# with diameter 12 cm 
# Formula : V=4/3 * π * r 3``

# In[91]:


pi = 3.14
r = 12
V=4/3 * pi * (r*r*r)


# In[93]:


V


# In[ ]:




