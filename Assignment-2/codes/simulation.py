from numpy import random
from scipy.stats import gamma
count=0
#no of experiments conducted.
n=100000
for i in  range (0,n):
  x=random.exponential(1,1)
  y=gamma.rvs(a=2,loc=0,scale=1,size=1)
  z=x-y
  if z<=0:
    count=count+1
theory_prob=0.75
exp_prob=count/n
print("Experimental probability of P(X_1<X_2) is:",exp_prob)
print("Theoritical probability of p(X_1<X_2) is :",theory_prob)
print("absolute difference in caluclating probability is :",abs(exp_prob-theory_prob))
