# -*- coding: utf-8 -*-
"""Untitled16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_0Z5i1F3k93xnLGlJk_kV_Efkujc5qzV
"""

from scipy.stats import bernoulli
# no of times the experiment is conducting.
n=600
sim_expectation=0
#caluclating probability of (X=i):
def prob(i):
  count=0
  j=0
  while(j<n):
    a=bernoulli.rvs(size=i,p=2/3)
    j=j+1
    k=0
    while(k<i):
      if (a[i-1]==0):
        break
      elif (a[k]==1 and k!=i-1):
        break
      elif (k==i-1):
        count=count+1
      
      k=k+1
  return count/n

for b in range(1,1001):
  sim_expectation=sim_expectation+prob(b)*(b)

theory_expectation=3/2

print("simulated value is ",sim_expectation)
print("theoritical value is ",theory_expectation)
print("absolute differnece between the values is ",abs(sim_expectation-theory_expectation))
