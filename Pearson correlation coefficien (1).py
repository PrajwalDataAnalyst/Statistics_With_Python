#!/usr/bin/env python
# coding: utf-8

# In[43]:


import statistics as st
import matplotlib.pyplot as plt


# In[48]:


x=input("enter the integer numbers for X ").split()
x=list(map(int,x))
y=input("enter the integer numbers for Y ").split()
y=list(map(int,y))
#x=[1,2,3,4,5,6,7,8,9,10]
#y=[10,20,30,40,50,40,70,80,90,100]
xx=st.mean(x)
yy=st.mean(y)
s=0
xst=st.stdev(x)
yst=st.stdev(y)
print(xx,yy)
print("------------------------------------------------------")

print("xi - yi | (xi-mean) | (yi-mean) | (ximean -yimean) ")
print("------------------------------------------------------")
for i in range(len(x)):
    x1=x[i]-xx
    y1=y[i]-yy
    z1=x1*y1
    s=s+z1
    print(x[i],"|",y[i], "|  ",round(x1,2)," | ",y1,"   |  ",round(z1,2))
    if i+1==len(x):
        print(s)
        cov=s/(len(x)-1)
        print("correlation is = ",cov)
        pcc=cov/(xst*yst)
        print("Pearson correlation coefficient = ",round(pcc*100,2),"%")
plt.scatter(x, y,color="black")
plt.plot(x, y, linestyle=':', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Correlation Chart')
plt.grid(True)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




