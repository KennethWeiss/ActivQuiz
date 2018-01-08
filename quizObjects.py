#Maybe I should convert runSheetMaker into a method of the object sheet this could be used to initialize the sheet
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


class Sheet:
    row = 0
    column = 0
    title = "Title"
    quiz = "Quiz"
    fileName = "Filename"

testSheet = Sheet()
testSheet.fileName = "convertLinear"
testSheet.title = "Title"
testSheet.quiz = "Quiz"

def getRandNotZero(first,last):
   numbers = range(first,-1) + range(1,last)
   return random.choice(numbers)



def add():
    firstInt = random.randint(1,12)
    secondInt = random.randint(1,12)
    Question.question = (str(firstInt)+" + "+str(secondInt))
    Question.answer = firstInt+secondInt
    print("The question is " + Question.question)
    Question.answerType = "Numeric"

def addMultipleChoice():
    firstInt = random.randint(1,12)
    secondInt = random.randint(1,12)
    Question.question = (str(firstInt)+" + "+str(secondInt))
    Question.answer = firstInt+secondInt
    print("The question is " + Question.question)
    Question.answerType = "MultipleChoice"
    Question.multipleChoices["A"] = firstInt - secondInt
    Question.multipleChoices["B"] = firstInt + secondInt
    Question.multipleChoices["C"] = firstInt * secondInt
    Question.multipleChoices["D"] = firstInt + firstInt



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

def addToSheetNumeric(function, Sheet):
    for num in range(1,10):  #to iterate between first to second-1 number of questions
        #function = add
        Sheet.spreadsheet.write(Sheet.row,Sheet.column, 'Q' + str(num))
        Sheet.spreadsheet.write(Sheet.row,Sheet.column+1,Question.question)
        Sheet.row+=1
        Sheet.spreadsheet.write(Sheet.row,Sheet.column,"Level")
        Sheet.spreadsheet.write(Sheet.row,Sheet.column+1,Question.level)
        Sheet.row+=1
        Sheet.spreadsheet.write(Sheet.row,Sheet.column,"Question Type")
        Sheet.spreadsheet.write(Sheet.row,Sheet.column+1,Question.answerType)
        Sheet.row+=1
        Sheet.spreadsheet.write(Sheet.row,Sheet.column,"Correct Answers")
        #write an answer to a cell from function
        Sheet.spreadsheet.write(Sheet.row,Sheet.column+1,Question.answer)
        Sheet.row+=3;
        print("Row in addToSheetNumeric = " +str(Sheet.row))

def addToSheetMultipleChoice(function, Sheet):
    for num in range(1,101):  #to iterate between first to second-1 number of questions
        Sheet.ws.write(Question.row,Question.col, 'Q' + str(num))
        #write a question from function
        Sheet.ws.write(Question.row,Question.col+1,Question.question)
        Question.row+=1
        Sheet.ws.write(Question.row,Question.col,"Level")
        Sheet.ws.write(Question.row,Question.col+1,Question.level)
        Question.row+=1
        Sheet.ws.write(Question.row,Question.col,"Question Type")
        Question.answerType = "Multiple Choice"
        Sheet.ws.write(Question.row,Question.col+1,Question.answerType)
        Question.row+=1
        Sheet.ws.write(Question.row,Question.col,"Correct Answers")
        Sheet.ws.write(Question.row,Question.col+1,Question.answer)
        #write an answer to a cell from function
        for letter, choice in Question.multipleChoices.items():
            Question.row+=1
            Sheet.ws.write(Question.row,Question.col,letter)
            Sheet.ws.write(Question.row,Question.col+1,choice)
        Sheet.row+=3


def runSheetMaker(functions):
   w = Workbook()
   ws = w.add_sheet('OK', cell_overwrite_ok=True)

   Sheet.spreadsheet = ws

   Sheet.row = 4
   Sheet.column = 1
   Question.level = 1
   Question.answerType = 'Numeric'
   ws.write(1,1,'Title')
   ws.write(2,1,'Quiz')
    #Determines if the answer type and sends the function to that for proper template
   for f in functions:
      f()
      if(Question.answerType == "Numeric") or (Question.answerType == "AlphaNumeric"):
          print("Adding Numeric")
          addToSheetNumeric(functions, Sheet)
          Question.level+=1
      elif(Question.answerType == "MultipleChoice"):
          addToSheetNumeric(functions, Sheet)
          print("Adding multiple Choice")
      else:
          print("QuestionType is " + Question.answerType)
   print(Sheet.row)
   w.save('addition.xls')

addition = [add, addMultipleChoice]

runSheetMaker(addition)


#questionType
#name of spreadsheet
#
'''
#working sheet creator
for num in range(1,101):  #to iterate between first to second-1 number of questions
   question, answer = modeOfNums()
   question = str(question)
   answer = str(answer)
   ws.write(row,col, 'Q' + str(num))
   #write a question from function
   ws.write(row,col+1,question)
   row+=1
   ws.write(row,col,"Level")
   ws.write(row,col+1,5)
   row+=1
   ws.write(row,col,"Question Type")
   ws.write(row,col+1,"Numeric")
   row+=1
   ws.write(row,col,"Correct Answers")
   #write an answer to a cell from function
   ws.write(row,col+1,answer)
   row+=3
   '''

'''

for num in range(1,101):  #to iterate between first to second-1 number of questions
   question, answer = percentageIntro()
   question = str(question)
   answer = str(answer)
   ws.write(row,col, 'Q' + str(num))
   #write a question from function
   ws.write(row,col+1,question)
   row+=1
   ws.write(row,col,"Level")
   ws.write(row,col+1,1)
   row+=1
   ws.write(row,col,"Question Type")
   Question.answerType = "Multiple Choice"
   ws.write(row,col+1,Question.answerType)
   row+=1
   ws.write(row,col,"Correct Answers")
   #write an answer to a cell from function
   if(answer == 'part'):
      ws.write(row,col+1,"1:A")
   elif(answer == 'whole'):
      ws.write(row,col+1,"1:B")
   elif(answer == 'percent'):
      ws.write(row,col+1,"1:C")
   row+=1
   ws.write(row,col,"A")
   ws.write(row,col+1,"Part")
   row+=1
   ws.write(row,col,"B")
   ws.write(row,col+1,"Whole")
   row+=1
   ws.write(row,col,"C")
   ws.write(row,col+1,"Percent")
   row+=3
'''
#lastRow = addToSheet(0)
#w.save('mode2.xls')
print("Awesome")
