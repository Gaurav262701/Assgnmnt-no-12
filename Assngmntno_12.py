#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Answer no 1
#Write a Python program to Extract Unique values dictionary values
test_dict ={'abc' : [1,2,3,4],
             'is' : [5,6,7,8],
             'best':[9,10,11,12],
             'for': [13,14,15]}

print("The original dictionary is :"+str(test_dict))

res = list(sorted({ele for val in test_dict.values() for ele in val}))
print("The unique values is :" +str(res))


# In[3]:


#Answer no 2
#Write a Python program to find the sum of all items in a dictionary
def returnSum(myDict):
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)
    return final
dict = {'a' : 100 , 'b' : 200, 'c':300}
print("sum :" , returnSum(dict))


# In[5]:


#Answer no 3
#Write a Python program to Merging two Dictionaries
def Merge(A,B):
    return(B.update(A))
A = {'a':10,'b': 8}
B = {'d':6,'c':4}
print(Merge(A,B))
print(B)


# In[11]:


#Answer no 4
#Write a Python program to convert key-values list to flat dictionary
from itertools import product
test_dict = {'month':[1,2,3],
             'name':['jan','feb','march']}
print("The original dictionary is :"+str(test_dict))
x = list(test_dict.values())
a = x[0]
b = x[1]
d = Dict()
for i in range(0,len(a)):
    d[a[i]]=b[i]
print("flattened dictionar :"+ str(d))


# In[13]:


from collections import OrderedDict


# In[15]:


#Answer no 5
#Write a Python program to insertion at the beginning in OrderedDict
iniordered_dict = OrderedDict([('Akshat','1'),('nikhil','2')])

iniordered_dict.update({'manjeet':'3'})

iniordered_dict.move_to_end('manjeet',last = False)

print("result dictionary:"+str(iniordered_dict))


# In[17]:


#Answer no 6
#Write a Python program to check order of character in string using OrderedDict().
def checkOrder(input,pattern):
    dict = OrderedDict.fromkeys(input)
    
    ptrlen = 0
    
    for key,value in dict.items():
        if(key == pattern[ptrlen]):
            ptrlen = ptrlen+1
            
        if (ptrlen == (len(pattern))):
            return 'true'
        
    return 'false'

if __name__ == '__main__':
    input = 'engineer rock'
    pattern = 'er'
    print(checkOrder(input,pattern))
            


# In[18]:


#Answer no 7
#Write a Python program to sort Python Dictionaries by Key or Value
def dictionary():
    key_value = {}
    key_value[2]=56
    key_value[5]=12
    key_value[1]=2
    key_value[4]=24
    key_value[6]=18
    key_value[3]=323
    
    print("Task 1:-\n")
    print("key_value",key_value)
    
    for i in sorted(key_value.keys()):
        print(i,end = " ")
        
def main():
    dictionary()
    
if __name__ == '__main__':
    main()
    


# In[ ]:




