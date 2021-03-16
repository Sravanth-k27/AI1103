import random as rd

# Defining a function for rolling  a die three times.
def rolling_a_die(Event_happening):
    count1=0
    count2=0
    count3=0
    n_experiment=1000000
    #repeating the experiment 1000000 times 
    for i in range(n_experiment):
    #throw1,throw2,throw2,throw3 be the outcomes of throwing a die three times.
       
        throw1=rd.randint(1,6)
        throw2=rd.randint(1,6)
        throw3=rd.randint(1,6)


        #defining event A as  getting 4 on third throw of die
        #defining event B as getting 6 and 5 on first and second throws of die resp
        if Event_happening=='A':
            if throw3==4:
                count1=count1+1

              
        if Event_happening=='B':
            if throw1==6 and throw2==5 :
                count2=count2+1
        
        #Event AB(A and B) i.e occuring 6,5,4 as outomes on throwing a die three times.
        if Event_happening=='AB':
            if throw1==6 and throw2==5 and throw3==4:
                count3=count3+1

    return (count1+count2+count3)/n_experiment

a=rolling_a_die('AB')/rolling_a_die('B')

print("The following  probabilities are the summilation results")
print("")
print("1.Probability of occuring 4 on third throw, P(A) = ",rolling_a_die('A'))
print("")
print("2.Probability of occuring 6 and 5 on first and second throws , P(B) = ",rolling_a_die('B'))
print("")
print("3.Probability of AB(A and B) i.e occuring 6,5,4 as outcomes of throwing a die 3 times, Pr(AB) = ",rolling_a_die('AB'))
print("")
print("4.conditional probability of P(A|B) = ",a)
print("")
print("The following probabilities are the theoritical results:")
print("")
print("1.Probability of occuring 4 on third throw, P(A) = ",0.166667)
print("")
print("2.Probability of occuring 6 and 5 on first and second throws , P(B) = ",0.027778)
print("")
print("3.Probability of AB(A and B) i.e occuring 6,5,4 as outcomes  of throwing a die 3 times,P(AB)=",0.004630)
print("")
print("4.Conditional probability of P(A|B)=",0.166667)
print("")
print("The following are the errors in probabilities caluclated via simulation and theoritical methods")
print("")
print("1.error in caluclating P(A)=",rolling_a_die('A')-0.16667)
print("")
print("2.error in caluclating P(B)=",rolling_a_die('B')-0.027778)
print("")
print("3.error in caluclating P(AB)=",rolling_a_die('AB')-0.004630)
print("")
print("4.error in caluclationg P(A|B)=",a-0.166667)