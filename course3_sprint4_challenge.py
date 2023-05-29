#!/usr/bin/env python
# coding: utf-8

# ## MCQ QUIZ

# In[ ]:


print ("\033[1mMCQ QUIZ ON SQL\033[0m")
print("\n")
Q = {"Q.1 what is the full form of RDBMS ?" : "1.relational database management system  2.retrieval database management system  3.both 1 and 2  3. none of them",
    "Q.2 Which of the following commands does not belongs to the DDL?" : "1.drop  2.update  3.create  4.alter", 
    "Q.3 what is the function of the drop command ?" : "1.create a new table  2.rename a table  3.modify the structure of the table  4.drop a table",
    "Q.4 which of the foloowing is not the logical operator used in SQL ?" : "1.OR  2.UP  3.AND  4.NOT",
    "Q.5 which clause allows the user to limit the query ?" : "1.limit  2.where  3.none of them  4.both of them",
    "Q.6 which of the following mathematical function in SQL gives the integer value ?" : "1.floor  2.cot  3.pi  4.pow",
    "Q.7 In which of the following join user dosen't need to specify a join condition ?" : "1.left outer join  2.right outer join  3.natural join  4.inner join",
    "Q.8 which of the following is true about correlated queries ?" : "1.correlated queries doesn't exist  2.can stand alone  3.does not reference outer query  4.cannot stand alone",
    "Q.9 which of the following is the type of normaliztion in SQL ?" : "1.AD  2.BCNF  3.NOF  4.NIF",
    "Q.10 which of the following is not a quantifier in SQL ?" : "1.MORE  2.ALL  3.SOME  4.ANY"}
options = list(Q.values())
correct_options = ["1", "3", "4", "2", "1", "1", "3", "4", "2", "1"]
myit2 = iter(correct_options)
myit = iter(options)
start = input("Are u ready for quiz? (yes or no) : ")
print("\n")
score = 0
negative_m = 0
question_skipped = 0
correct_answers = 0
wrong_answers = 0


if start == 'yes':
    print("\033[1mINSTRUCTIONS\033[0m")
    print("following are the instructions :")
    print("1. the quiz contains 10 questions and every question has four options and exactly one option will be correct.")
    print("2. To answer a question student needs to enter the number corresponding to the chosen option")
    print("3. each question carry 2 marks")
    print("4. there is also negative marking, for every wrong answer student gets -1 marks. ")
    print("5. student can also skip the question if they want to.")
    print("\n")
    for q in Q:
        print (q)
        options = next(myit)
        print(options)
        correct_options = next(myit2)
        ans = (input("enter the option between 1 and 4 or type 's' to skip : "))
        if ans == correct_options :
            print("your answer is correct")
            score = score + 2
            correct_answers = correct_answers + 1
        elif ans == "s":
            print ('you skip the question')
            question_skipped = question_skipped + 1
        else :
            print("your answer is incorrect")
            negative_m = negative_m + 1
            wrong_answers = wrong_answers + 1
        print("\n")
    print("your total score = {}/20".format(score - negative_m))
    percentage = (score-negative_m)/20*100
    print("you got %d%%" %(percentage))
    print('total questions skipped :', question_skipped)
    print("total questions answered correctly : ", correct_answers)
    print("total questions answered incorrectly : ", wrong_answers)
else :
    print("you leave the quiz")
    


# 
# 
