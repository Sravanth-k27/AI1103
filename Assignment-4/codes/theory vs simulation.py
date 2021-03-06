# -*- coding: utf-8 -*-
"""Untitled18.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s9FPy-XRtVhl43h2OCoZJQe_ziI5STa0
"""

from scipy.stats import bernoulli
import numpy as np
import random
# no of times the experiment is conducting:
n=100000
count1=count2=count3=count4=count5=count6=0
#caluclating probability of getting heads on first and second thows.
for i in range (n):
  a=random.randint(0,2)
  #selecting coin1 on first trail
  if (a==0):
    random_rand_coin=bernoulli.rvs(size=1,p=1/2)
    if (random_rand_coin==1):
      b=random.randint(1,2)
      #selecting coin2 on second trail
      if (b==1):
        c=bernoulli.rvs(size=1,p=1)
        if c==1:
          count1=count1+1
      #selecting coin3 on second trail
      if (b==2):
        d=bernoulli.rvs(size=1,p=0)
        if(d==1):
          count2=count2+1


for i in range(n):
  a=random.randint(0,2)
  #selecting coin2 on first trail
  if(a==1):
    random_rand_coin=bernoulli.rvs(size=1,p=1)
    if (random_rand_coin==1):
      b=random.randint(1,2)
      #selecting coin1 on second trail
      if (b==1):
        c=bernoulli.rvs(size=1,p=1/2)
        if (c==1):
          count3=count3+1
      #selecting coin3 on second trail
      if (b==2):
        d=bernoulli.rvs(size=1,p=0)
        if (d==1):
              count4=count4+1

for i in range (n):
  a=random.randint(0,2)
  #selecting coin3 on first trail
  if(a==2):
    random_rand_coin=bernoulli.rvs(size=1,p=0)
    if (random_rand_coin==1):
      b=random.randint(1,2)
      #selecting coin1 on second trail
      if (b==1):
        c=bernoulli.rvs(size=1,p=1/2)
        if (c==1):
          count5=count5+1
      #selecting coin2 on second trail
      if (b==2):
        d=bernoulli.rvs(size=1,p=1)
        if (d==1):
              count6=count6+1

prob1=(count1+count2+count3+count4+count5+count6)/n
#caluclating probability of getting head on first throw
c1=c2=c3=0
for i in range(n):
  a=random.randint(0,2)
  #selecting coin1 on first trail
  if (a==0):
    random_rand_coin1=bernoulli.rvs(size=1,p=1/2)
    if (random_rand_coin1==1):
      c1=c1+1
  #selecting coin2 on first trail
  if (a==1):
    random_rand_coin2=bernoulli.rvs(size=1,p=1)
    if (random_rand_coin2==1):
      c2=c2+1
  #selecting coin3 on first trail
  if (a==2):
    random_rand_coin3=bernoulli.rvs(size=1,p=0)
    if (random_rand_coin3==1):
      c3=c3+1

prob2=(c1+c2+c3)/n
simul_prob=prob1/prob2
theory_prob=1/3
print("Simulated probability of getting head on second throw given that first throw results head is :",simul_prob)
print("theoritical probability of getting head on second throw given that first throw results head is :",theory_prob)
print("absolute differnce between the probabilities is :",abs(simul_prob-theory_prob))
