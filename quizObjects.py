#I'm working on the runSheetMaker methods - Kenny
#I have objects working for
#creating a sheet
#insert numeric
#insert multiple
#THE CHECKTYPE SEEMS A BIT SLOPPY BUT IT WORKS :(
#SOMETHING IS WRONG WITH GETRANDNOTZERO
#!/usr/bin/python2.7
# -*- coding: cp1252 -*-
from xlwt import *
from fractions import Fraction
from fractions import gcd
from decimal import *
import random
import string
import re
import numpy as np

#why do I have a question and answer type?
class Question:
    question=""
    answer=" "
    questionType="NotChanged"
    answerType=" " #Numeric,AlphaNumeric,MultipleChoice
    level=0
    numberOfQuestions=10
    multipleChoices = {}
    num = 0

class Sheet:
    row = 0
    column = 0
    title = "Title"
    quiz = "Quiz"
    fileName = "Filename"

    w = Workbook()
    ws = w.add_sheet('OK', cell_overwrite_ok=True)

#create a Spreadsheet with Title and Quiz
    def initialSheet():
       #Sheet.fileName = functions
       print("Creating initial template")
       Sheet.row = 4
       Sheet.column = 1
       Question.level = 1
       Question.answerType = 'Numeric'
       Sheet.ws.write(1,1,'Title')
       Sheet.ws.write(2,1,'Quiz')

#insert a question and numerical answer to the spreadsheet
    def insertNumeric(function):
        print("adding numeric question")
        Sheet.ws.write(Sheet.row,Sheet.column, 'Q' + str(Question.num))
        Question.num+=1
        Sheet.ws.write(Sheet.row,Sheet.column+1,Question.question)
        Sheet.row+=1
        Sheet.ws.write(Sheet.row,Sheet.column,"Level")
        Sheet.ws.write(Sheet.row,Sheet.column+1,Question.level)
        Sheet.row+=1
        Sheet.ws.write(Sheet.row,Sheet.column,"Question Type")
        Sheet.ws.write(Sheet.row,Sheet.column+1,Question.answerType)
        Sheet.row+=1
        Sheet.ws.write(Sheet.row,Sheet.column,"Correct Answers")
        #write an answer to a cell from function
        Sheet.ws.write(Sheet.row,Sheet.column+1,Question.answer)
        Sheet.row+=3;

#insert a multiple choice question and answer into the spreadsheet
    def insertMultipleChoice(function):
        Sheet.ws.write(Sheet.row,Sheet.column, 'Q' + str(Question.num))
        Question.num += 1
        #write a question from function
        Sheet.ws.write(Sheet.row,Sheet.column+1,Question.question)
        Sheet.row+=1
        Sheet.ws.write(Sheet.row,Sheet.column,"Level")
        Sheet.ws.write(Sheet.row,Sheet.column+1,Question.level)
        Sheet.row+=1
        Sheet.ws.write(Sheet.row,Sheet.column,"Question Type")
        Question.answerType = "Multiple Choice"
        Sheet.ws.write(Sheet.row,Sheet.column+1,Question.answerType)
        Sheet.row+=1
        Sheet.ws.write(Sheet.row,Sheet.column,"Correct Answers")
        Sheet.ws.write(Sheet.row,Sheet.column+1,Question.answer)
        #write an answer to a cell from function
        for letter, choice in Question.multipleChoices.items():
            Sheet.row+=1
            Sheet.ws.write(Sheet.row,Sheet.column,letter)
            Sheet.ws.write(Sheet.row,Sheet.column+1,choice)
            print(letter, choice)
        Sheet.row+=3

#insert any function that has a question and answer
#send question and answer to proper sheetInsert
    def insertProblem(function):
        function()
        if(Question.answerType == "numeric"):
            Sheet.insertNumeric(function)
        elif(Question.answerType == "multipleChoice"):
            Sheet.insertMultipleChoice(function)
        else:
            print("Problem with type")



#def getRandNotZero(first,last):
#   numbers = range(first,-1) + range(1,last)
#   return random.choice(numbers)

#def add():
#def addMultipleChoice():
#def subtract():
#def addSubtract():
#def multiply():
#def divide():
#def multiplyDivide():
#def allOperations():
#def divideSingleDigitQuotient():
#def divideSingleDigitQuotientMultiple10():
#def divideDoubleDigitQuotient():
#def divideDoubleDigitQuotientMultiple10():
#def divideDoubleDigitDivisor():
#def divideDecimalEasy():
#def divideDecimalMedium():
#def divideDecimalHard():


def add():
    Question.answerType = "numeric"
    firstInt = random.randint(1,12)
    secondInt = random.randint(1,12)
    Question.question = (str(firstInt)+" + "+str(secondInt))
    Question.answer = firstInt+secondInt
    print("The question is " + Question.question)


def addMultipleChoice():
    Question.answerType = "multipleChoice"
    firstInt = random.randint(1,12)
    secondInt = random.randint(1,12)
    Question.question = (str(firstInt)+" + "+str(secondInt))
    Question.answer = firstInt+secondInt
    print("The question is " + Question.question)
    Question.multipleChoices["A"] = firstInt - secondInt
    Question.multipleChoices["B"] = firstInt + secondInt
    Question.multipleChoices["C"] = firstInt * secondInt
    Question.multipleChoices["D"] = firstInt + firstInt

def subtract():
    Question.type = "numerical"
    firstInt = random.randint(1,30);
    secondInt = random.randint(1,30);
    if(secondInt>firstInt):
      Question.question, Question.answer = (str(secondInt)+" - "+str(firstInt),secondInt-firstInt)
    else:
      Question.question, Question.answer = (str(firstInt)+" - "+str(secondInt),firstInt-secondInt)

def addSubtract():
    Question.type = "numerical"
    choice = random.choice('as')
    if(choice == "a"):
       add()
    else:
       subtract()

def multiply():
    Question.type = "numerical"
    firstInt = random.randint(1,12)
    secondInt = random.randint(1,12)
    if(secondInt<0):
      Question.question,Question.answer = (str(firstInt)+ " x" + " ("+str(secondInt)+")",firstInt*secondInt)
    else:
      Question.question,Question.answer = (str(firstInt)+" x "+str(secondInt),firstInt*secondInt)

def divide():
   Question.type = "numerical"
   divisor = random.randint(3,12)
   quotient = random.randint(3,12)
   dividend = divisor * quotient
   Question.question,Question.answer = (str(dividend)+" / "+str(divisor),quotient)

def multiplyDivide():
   Question.type = "numerical"
   choice = random.choice('md')
   if(choice=="m"):
      multiply()
   else:
      divide()

def allOperations():
   Question.type = "numerical"
   choice = random.choice('am')
   if(choice == 'a'):
      addSubtract()
   else:
      multiplyDivide()

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#division problem
#quotient is single digit no remainder
#####
#I can probably make all this division one function
#####
def divideSingleDigitQuotient():
   qtype = "numerical"
   divisor = random.randint(2,10)
   quotient = random.randint(2,10)
   dividend = divisor*quotient
   Question.question = str(dividend)+"/"+str(divisor)
   Question.answer = str(quotient)

def divideSingleDigitQuotientMultiple10():
   qtype = "numerical"
   divisor = random.randint(2,10)
   divisor *= 10
   quotient = random.randint(2,10)
   dividend = divisor*quotient
   Question.question = str(dividend)+"/"+str(divisor)
   Question.answer = str(quotient)

def divideDoubleDigitQuotient():
   qtype = "numerical"
   divisor = random.randint(2,10)
   quotient = random.randint(10,99)
   dividend = divisor*quotient
   Question.question = str(dividend)+"/"+str(divisor)
   Question.answer = str(quotient)

def divideDoubleDigitQuotientMultiple10():
   qtype = "numerical"
   divisor = random.randint(2,10)
   divisor *= 10
   quotient = random.randint(10,99)
   dividend = divisor*quotient
   Question.question = str(dividend)+"/"+str(divisor)
   Question.answer = str(quotient)

def divideDoubleDigitDivisor():
   qtype = "numerical"
   divisor = random.randint(11,50)
   quotient = random.randint(10,99)
   dividend = divisor*quotient
   Question.question = str(dividend)+"/"+str(divisor)
   Question.answer = str(quotient)

def divideDecimalEasy():
   qtype = "numerical"
   divisor = random.randint(1,10)
   divisor = divisor/10.0
   quotient = random.randint(10,100)
   dividend = divisor*quotient
   Question.question = str(dividend)+"/"+str(divisor)
   Question.answer = str(quotient)

def divideDecimalMedium():
   qtype = "numerical"
   divisor = random.randint(1,10)
   divisor = divisor/10.0
   quotient = random.randint(100,1000)
   dividend = divisor*quotient
   Question.question = str(dividend)+"/"+str(divisor)
   Question.answer = str(quotient)

def divideDecimalHard():
   qtype = "numerical"
   divisor = random.randint(10,100)
   divisor = divisor/10.0
   quotient = random.randint(10,100)
   dividend = divisor*quotient
   Question.question = str(dividend)+"/"+str(divisor)
   Question.answer = str(quotient)


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

addition = [add, addMultipleChoice, subtract, addSubtract, multiply, divide, multiplyDivide, allOperations, divideSingleDigitQuotient]


#def divideSingleDigitQuotientMultiple10():
#def divideDoubleDigitQuotient():
#def divideDoubleDigitQuotientMultiple10():
#def divideDoubleDigitDivisor():
#def divideDecimalEasy():
#def divideDecimalMedium():
#def divideDecimalHard():


Sheet.initialSheet()
Sheet.insertProblem(add)
Sheet.insertProblem(subtract)
Sheet.insertProblem(addMultipleChoice)
Sheet.insertProblem(addSubtract)
Sheet.insertProblem(multiply)
Sheet.insertProblem(divide)
Sheet.insertProblem(multiplyDivide)
Sheet.insertProblem(allOperations)
Sheet.insertProblem(divideSingleDigitQuotient)


Sheet.w.save("addition.xls")

print("Awesome")
