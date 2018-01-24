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
       Question.answerType = 'numerical'
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
        if(Question.answerType == "numerical"):
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
#def addDecimal():
#def subtractDecimal():
#def perfectSquaresto13():
#def perfectSquares14to16():
#def perfectSquares17to20
#def perfectSquaresFractions
#def perfectCubes2to5()
#getFraction() numerator 1-10 denom 2-12
#getFractionSmall() numer: 1-4 denom 2-5
#def addFractionCommonDenominator():
#def EquivalentFractions():
#def multiplyFraction():
#def divideFraction():
#def GCF():
#def LCM():
#def convertImproperMixed(fract):
#def convertDecimalPercent():
#def convertDecimalFractionSimple():
#def convertDecimalFractionReduce():
#def EquivalentRatios():
#def EquivalentRatiosOneStep():
#def proportions():
#def percentagesTenFifty():
#def percentagesTenFiftyFindWhole():
#def percentagesFiveTwenty():
#def percentagesFiveTwentyFindWhole():
#def percentagesUptoTwenty():
#def percentagesUptoTwentyFindWhole():
#def percentagesUptoTen():
#def percentagesUptoTwenty():
#def percentages():
#def hardPercentages():






















def add():
    Question.answerType = "numerical"
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
    Question.answerType = "numerical"
    firstInt = random.randint(1,30);
    secondInt = random.randint(1,30);
    if(secondInt>firstInt):
      Question.question, Question.answer = (str(secondInt)+" - "+str(firstInt),secondInt-firstInt)
    else:
      Question.question, Question.answer = (str(firstInt)+" - "+str(secondInt),firstInt-secondInt)

def addSubtract():
    Question.answerType = "numerical"
    choice = random.choice('as')
    if(choice == "a"):
       add()
    else:
       subtract()

def multiply():
    Question.answerType = "numerical"
    firstInt = random.randint(1,12)
    secondInt = random.randint(1,12)
    if(secondInt<0):
      Question.question,Question.answer = (str(firstInt)+ " x" + " ("+str(secondInt)+")",firstInt*secondInt)
    else:
      Question.question,Question.answer = (str(firstInt)+" x "+str(secondInt),firstInt*secondInt)

def divide():
   Question.answerType = "numerical"
   divisor = random.randint(3,12)
   quotient = random.randint(3,12)
   dividend = divisor * quotient
   Question.question,Question.answer = (str(dividend)+" / "+str(divisor),quotient)

def multiplyDivide():
   Question.answerType = "numerical"
   choice = random.choice('md')
   if(choice=="m"):
      multiply()
   else:
      divide()

def allOperations():
   Question.answerType = "numerical"
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
   Question.answerType = "numerical"
   divisor = random.randint(2,10)
   quotient = random.randint(2,10)
   dividend = divisor*quotient
   Question.question = str(dividend)+"/"+str(divisor)
   Question.answer = str(quotient)

def divideSingleDigitQuotientMultiple10():
   Question.answerType = "numerical"
   divisor = random.randint(2,10)
   divisor *= 10
   quotient = random.randint(2,10)
   dividend = divisor*quotient
   Question.question = str(dividend)+"/"+str(divisor)
   Question.answer = str(quotient)

def divideDoubleDigitQuotient():
   Question.answerType = "numerical"
   divisor = random.randint(2,10)
   quotient = random.randint(10,99)
   dividend = divisor*quotient
   Question.question = str(dividend)+"/"+str(divisor)
   Question.answer = str(quotient)

def divideDoubleDigitQuotientMultiple10():
   Question.answerType = "numerical"
   divisor = random.randint(2,10)
   divisor *= 10
   quotient = random.randint(10,99)
   dividend = divisor*quotient
   Question.question = str(dividend)+"/"+str(divisor)
   Question.answer = str(quotient)

def divideDoubleDigitDivisor():
   Question.answerType = "numerical"
   divisor = random.randint(11,50)
   quotient = random.randint(10,99)
   dividend = divisor*quotient
   Question.question = str(dividend)+"/"+str(divisor)
   Question.answer = str(quotient)

def divideDecimalEasy():
   Question.answerType = "numerical"
   divisor = random.randint(1,10)
   divisor = divisor/10.0
   quotient = random.randint(10,100)
   dividend = divisor*quotient
   Question.question = str(dividend)+"/"+str(divisor)
   Question.answer = str(quotient)

def divideDecimalMedium():
   Question.answerType = "numerical"
   divisor = random.randint(1,10)
   divisor = divisor/10.0
   quotient = random.randint(100,1000)
   dividend = divisor*quotient
   Question.question = str(dividend)+"/"+str(divisor)
   Question.answer = str(quotient)

def divideDecimalHard():
   Question.answerType = "numerical"
   divisor = random.randint(10,100)
   divisor = divisor/10.0
   quotient = random.randint(10,100)
   dividend = divisor*quotient
   Question.question = str(dividend)+"/"+str(divisor)
   Question.answer = str(quotient)

def getOneDecimal():
   decimal = random.uniform(1,100)
   decimal *= 10
   decimal = int(decimal)
   decimal = decimal/10.0
   return decimal

def getTwoDecimal():
   decimal = random.uniform(1,100)
   decimal *= 100
   decimal = int(decimal)
   decimal = decimal/100.00
   return decimal

def addDecimal():
   Question.answerType = "numerical"
   firstnum = getOneDecimal()
   secondnum = getTwoDecimal()
   Question.question = str(firstnum)+" + "+str(secondnum)
   Question.answer = firstnum + secondnum

def subtractDecimal():
   Question.answerType = "numerical"
   firstnum = getOneDecimal()
   secondnum = getTwoDecimal()
   if(firstnum < secondnum):
      temp = firstnum
      firstnum = secondnum
      secondnum = temp
   Question.question = str(firstnum)+" - "+str(secondnum)
   Question.answer = firstnum - secondnum

def perfectSquaresto13():
    Question.answerType = "numerical"
    base = random.randint(1,13)
    exponent = 2
    Question.question = "Square root of " + str(pow(base,exponent))
    Question.answer = base

def perfectSquares14to16():
    Question.answerType = "numerical"
    base = random.randint(14,16)
    exponent = 2
    Question.question = "Square root of " + str(pow(base,exponent))
    Question.answer = base

def perfectSquares17to20():
    Question.answerType = "numerical"
    base = random.randint(17,20)
    exponent = 2
    Question.question = "Square root of " + str(pow(base,exponent))
    Question.answer = base

def perfectSquaresFractions():
    Question.answerType = "alphanumerical"
    base = getFraction()
    exponent = 2
    Question.question = "Square root of " + str(pow(base,exponent))
    Question.answer = str(base)

def perfectCubes2to5():
    Question.answerType = "numerical"
    base = random.randint(2,5)
    exponent = 3
    Question.question = "Cube root of " + str(pow(base,exponent))
    Question.answer = base

def getFraction():
   numerator = random.randint(1,10);
   denominator = random.randint(2,12);
   while (numerator >= denominator):
      numerator = random.randint(1,10);
      denominator = random.randint(2,12);
   return (Fraction(numerator,denominator))

def getFractionSmall():
   numerator = random.randint(1,4);
   denominator = random.randint(2,5);
   while (numerator >= denominator):
      numerator = random.randint(1,4);
      denominator = random.randint(2,5);
   return (Fraction(numerator,denominator))

def addFractionEasy():
   Question.answerType = "alphanumerical"
   first = getFractionSmall()
   denominator = first.denominator
   second = getFractionSmall()
   answer = first + second
   Question.question,Question,answer = (str(first)+" + "+str(second)),str(answer)

def addFractionHard():
   Question.answerType = "alphanumerical"
   first = getFraction()
   denominator = first.denominator
   second = getFraction()
   answer = first + second
   Question.question, Question.answer = (str(first)+" + "+str(second)),str(answer)

def addFractionCommonDenominator():
   Question.answerType = "alphanumerical"
   first = getFraction()
   denominator = first.denominator
   second = getFraction()
   numerator = random.randint(1,10);
   second = (Fraction(numerator,denominator))
   answer = first + second
   Question.question, Question.answer = (str(first)+" + "+str(second)),str(answer)

def EquivalentFractions():
   Question.answerType = "alphanumerical"
   first = random.randint(1,100)
   second = random.randint(1,100)
   while(gcd(first, second) == 1):
      first = random.randint(1,100)
   gcf = gcd(first, second)
   question = str(first) +"/" + str(second) + " = "
   answer = str(Fraction(first, second))
   Question.question, Question.answer = question, answer

def multiplyFraction():
   Question.answerType = "alphanumerical"
   first = getFraction()
   second = getFraction()
   answer = first * second
   Question.question, Question.answer = (str(first)+u" divided by " +str(second)),str(answer)

def divideFraction():
   Question.answerType = "alphanumerical"
   first = getFraction()
   second = getFraction()
   answer = first / second
   Question.question, Question.answer = (str(first)+" divided by "+str(second)),str(answer)

def GCF():
   Question.answerType = "numerical"
   first = random.randint(1,100)
   second = random.randint(1,100)
   while(gcd(first, second) == 1):
      first = random.randint(1,100)
   gcf = gcd(first, second)
   Question.question = "GCF of " + str(first) +" and " + str(second) + " : "
   Question.answer = gcf

def LCM():
   Question.answerType = "numerical"
   first = random.randint(1,10)
   second = random.randint(1,10)
   gcf = gcd(first, second)
   Question.question = "LCM of " + str(first) +" and " + str(second) + " : "
   Question.answer = (first*second)//gcf

###########################################################
def convertImproperMixed(fract):
   Question.answerType = "numerical"
   whole, rational = divmod(fract.numerator, fract.denominator)
   if(whole == 0):
      mixed = str(rational)+"/"+str(fract.denominator)
   elif(rational == 0):
      mixed = str(whole)
   else:
      mixed = str(whole)+" "+str(rational)+"/"+str(fract.denominator)
   return mixed
###############################################

def convertDecimalPercent():
   Question.answerType = "numerical"
   number = random.randint(1,100)
   if(number>9):
      Question.question = "What is ."+str(number)+" as a percent?"
   else:
      Question.question = "What is .0"+str(number)+" as a percent?"
   Question.answer = str(number)

#Students are required to know that
#Number goes over 10,100,1000,10000
#No reducing
def convertDecimalFractionSimple():
   Question.answerType = "alphanumerical"
   number = random.randint(1,100)
   if(number < 10):
      question = ".0"+str(number)
      answer = str(number)+"/"+str(100)
   elif(number % 10 == 0):
      question = "."+str(number/10)
      answer = str(number/10)+"/"+str(10)
   else:
      question = "."+str(number)
      answer = str(number)+"/"+str(100)
   Question.question, Question.answer = question, answer

def convertDecimalFractionReduce():
   Question.answerType = "alphaNumerical"
   number = random.randint(1,99)
   if(number < 10):
      question = ".0"+str(number)
   elif(number % 10 == 0):
      question = "."+str(number/10)
   else:
      question = "."+str(number)
   answer = Fraction(number,100)
   Question.question, Question.answer = question, answer

def EquivalentRatios():
   Question.answerType = "numerical"
   first = [random.randint(1,10), random.randint(1,10)]
   multiplier = random.randint(2,11)
  # a = multiplier*first(0)
  # b = multiplier*second
   second = [x*multiplier for x in first]

   chooser = random.randint(1,4)
   if(chooser == 1):
      #percent
      question = "%d:%d = %d:x" % (first[0], first[1], second[0])
      answer = second[1]
   if(chooser == 2):
      #percent
      question = "x:%d = %d:%d" % (first[1], second[0], second[1])
      answer = first[0]
   if(chooser == 3):
      #percent
      question = "%d:x = %d:%d" % (first[0], second[0], second[1])
      answer = first[1]
   if(chooser == 4):
      #percent
      question = "%d:%d = x:%d" % (first[0], first[1], second[1])
      answer = second[0]
   Question.question, Question.answer = question, answer

def EquivalentRatiosOneStep():
   Question.answerType = "numerical"
   first = [random.randint(1,10), random.randint(1,10)]
   multiplier = random.randint(2,11)
  # a = multiplier*first(0)
  # b = multiplier*second
   second = [x*multiplier for x in first]

   chooser = random.randint(1,4)
   if(chooser == 1):
      #percent
      question = "%d:%d = %d:x" % (first[0], first[1], second[0])
      answer = second[1]
   if(chooser == 2):
      #percent
      question = "x:%d = %d:%d" % (first[1], second[0], second[1])
      answer = first[0]
   if(chooser == 3):
      #percent
      question = "%d:x = %d:%d" % (first[0], second[0], second[1])
      answer = first[1]
   if(chooser == 4):
      #percent
      question = "%d:%d = x:%d" % (first[0], first[1], second[1])
      answer = second[0]


   Question.question, Question.answer = question, answer

def proportions():
   Question.answerType = "numerical"
   numerator = random.randint(1,10)
   denominator = random.randint(1,10)
   scale = random.randint(1,10)
   scaledNumerator = scale*numerator
   scaledDenominator = scale*denominator
   chooseVariable = random.randint(1,4)
   if(chooseVariable == 1):
      question = "x:"+str(denominator)+"="+str(scaledNumerator)+":"+str(scaledDenominator)
      answer = numerator
   elif(chooseVariable == 2):
      question = str(numerator)+":x"+"="+str(scaledNumerator)+":"+str(scaledDenominator)
      answer = denominator
   elif(chooseVariable == 3):
      question = str(numerator)+":"+str(denominator)+"=x:"+str(scaledDenominator)
      answer = scaledNumerator
   elif(chooseVariable == 4):
      question = str(numerator)+":"+str(denominator)+"="+str(scaledNumerator)+":x"
      answer = scaledDenominator
   else:
      question = "error"
      answer = "error"
   Question.question, Question.answer = question,answer


#remove trailing zeros
def format_float(f):
    Question.answerType = "numerical"
    d = Decimal(str(f));
    return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()

def percentagesTenFifty():
   Question.answerType = "numerical"
   percentages = [10,50,100]
   percent = random.choice(percentages)*1.0
   whole = random.randint(50,100)*1.0
   part = whole*(percent/100.0)
   chooser = 3
   #chooser = random.randint(1,4)
   if(chooser == 1):
      #percent
      question = "%.2f is what percent of %d?" % (part, whole)
      answer = percent
   if(chooser == 2):
      #whole
      question = "%d percent of what is %.2f?" % (percent, part)
      answer = whole
   if(chooser == 3):
      #part
      question = "%d percent  of %d is what?" % (percent, whole)
      answer = '%.2f'%part
   if(chooser == 4):
      question = "What percent of %d is %.2f?" % (whole, part)
      answer = percent
   answer = format_float(answer)
   Question.question, Question.answer = question, answer

def percentagesTenFiftyFindWhole():
   Question.answerType = "numerical"
   percentages = [10,50,100]
   percent = random.choice(percentages)*1.0
   whole = random.randint(50,100)*1.0
   part = whole*(percent/100.0)
   chooser = 2
   #chooser = random.randint(1,4)
   if(chooser == 1):
      #percent
      question = "%.2f is what percent of %d?" % (part, whole)
      answer = percent
   if(chooser == 2):
      #whole
      question = "%d percent of what is %.2f?" % (percent, part)
      answer = whole
   if(chooser == 3):
      #part
      question = "%d percent  of %d is what?" % (percent, whole)
      answer = '%.2f'%part
   if(chooser == 4):
      question = "What percent of %d is %.2f?" % (whole, part)
      answer = percent
   answer = format_float(answer)
   Question.question, Question.answer = question, answer

def percentagesFiveTwenty():
   Question.answerType = "numerical"
   percentages = [5,10,20,50,100]
   percent = random.choice(percentages)*1.0
   whole = random.randint(50,100)*1.0
   part = whole*(percent/100.0)
   chooser = 3
   #chooser = random.randint(1,4)
   if(chooser == 1):
      #percent
      question = "%.2f is what percent of %d?" % (part, whole)
      answer = percent
   if(chooser == 2):
      #whole
      question = "%d percent of what is %.2f?" % (percent, part)
      answer = whole
   if(chooser == 3):
      #part
      question = "%d percent  of %d is what?" % (percent, whole)
      answer = '%.2f'%part
   if(chooser == 4):
      question = "What percent of %d is %.2f?" % (whole, part)
      answer = percent
   answer = format_float(answer)
   Question.question, Question.answer = question, answer

def percentagesFiveTwentyFindWhole():
   Question.answerType = "numerical"
   percentages = [5,10,20,50,100]
   percent = random.choice(percentages)*1.0
   whole = random.randint(50,100)*1.0
   part = whole*(percent/100.0)
   chooser = 2
   #chooser = random.randint(1,4)
   if(chooser == 1):
      #percent
      question = "%.2f is what percent of %d?" % (part, whole)
      answer = percent
   if(chooser == 2):
      #whole
      question = "%d percent of what is %.2f?" % (percent, part)
      answer = whole
   if(chooser == 3):
      #part
      question = "%d percent  of %d is what?" % (percent, whole)
      answer = '%.2f'%part
   if(chooser == 4):
      question = "What percent of %d is %.2f?" % (whole, part)
      answer = percent
   answer = format_float(answer)
   Question.question, Question.answer = question, answer

def percentagesUptoTwenty():
   Question.answerType = "numerical"
   percentages = [5,10,20,25,50,75,100]
   percent = random.choice(percentages)*1.0
   whole = random.randint(50,100)*1.0
   part = whole*(percent/100.0)
   chooser = 3
   #chooser = random.randint(1,4)
   if(chooser == 1):
      #percent
      question = "%.2f is what percent of %d?" % (part, whole)
      answer = percent
   if(chooser == 2):
      #whole
      question = "%d percent of what is %.2f?" % (percent, part)
      answer = whole
   if(chooser == 3):
      #part
      question = "%d percent  of %d is what?" % (percent, whole)
      answer = '%.2f'%part
   if(chooser == 4):
      question = "What percent of %d is %.2f?" % (whole, part)
      answer = percent
   answer = format_float(answer)
   Question.question, Question.answer = question, answer

def percentagesUptoTwentyFindWhole():
   Question.answerType = "numerical"
   percentages = [5,10,20,25,50,75,100]
   percent = random.choice(percentages)*1.0
   whole = random.randint(50,100)*1.0
   part = whole*(percent/100.0)
   chooser = 2
   #chooser = random.randint(1,4)
   if(chooser == 1):
      #percent
      question = "%.2f is what percent of %d?" % (part, whole)
      answer = percent
   if(chooser == 2):
      #whole
      question = "%d percent of what is %.2f?" % (percent, part)
      answer = whole
   if(chooser == 3):
      #part
      question = "%d percent  of %d is what?" % (percent, whole)
      answer = '%.2f'%part
   if(chooser == 4):
      question = "What percent of %d is %.2f?" % (whole, part)
      answer = percent
   answer = format_float(answer)
   Question.question, Question.answer = question, answer

def percentagesUptoTen():
   Question.answerType = "numerical"
   percent = random.randint(1,10)*1.0
   whole = random.randint(50,100)*1.0
   part = whole*(percent/100.0)
   chooser = 3
   #chooser = random.randint(1,4)
   if(chooser == 1):
      #percent
      question = "%.2f is what percent of %d?" % (part, whole)
      answer = percent
   if(chooser == 2):
      #whole
      question = "%d percent of what is %.2f?" % (percent, part)
      answer = whole
   if(chooser == 3):
      #part
      question = "%d percent  of %d is what?" % (percent, whole)
      answer = '%.2f'%part
   if(chooser == 4):
      question = "What percent of %d is %.2f?" % (whole, part)
      answer = percent
   answer = format_float(answer)
   Question.question, Question.answer = question, answer

def percentagesUptoTenFindWhole():
   Question.answerType = "numerical"
   percent = random.randint(1,10)*1.0
   whole = random.randint(50,100)*1.0
   part = whole*(percent/100.0)
   chooser = 2
   #chooser = random.randint(1,4)
   if(chooser == 1):
      #percent
      question = "%.2f is what percent of %d?" % (part, whole)
      answer = percent
   if(chooser == 2):
      #whole
      question = "%d percent of what is %.2f?" % (percent, part)
      answer = whole
   if(chooser == 3):
      #part
      question = "%d percent  of %d is what?" % (percent, whole)
      answer = '%.2f'%part
   if(chooser == 4):
      question = "What percent of %d is %.2f?" % (whole, part)
      answer = percent
   answer = format_float(answer)
   Question.question, Question.answer = question, answer

def percentagesUptoTwenty():
   Question.answerType = "numerical"
   percent = random.randint(1,25)*1.0
   whole = random.randint(50,100)*1.0
   part = whole*(percent/100.0)
   chooser = 3
   #chooser = random.randint(1,4)
   if(chooser == 1):
      #percent
      question = "%.2f is what percent of %d?" % (part, whole)
      answer = percent
   if(chooser == 2):
      #whole
      question = "%d percent of what is %.2f?" % (percent, part)
      answer = whole
   if(chooser == 3):
      #part
      question = "%d percent  of %d is what?" % (percent, whole)
      answer = '%.2f'%part
   if(chooser == 4):
      question = "What percent of %d is %.2f?" % (whole, part)
      answer = percent
   answer = format_float(answer)
   Question.question, Question.answer = question, answer

def percentages():
   Question.answerType = "numerical"
   percent = random.randint(1,100)*1.0
   whole = random.randint(50,100)*1.0
   part = whole*(percent/100.0)
   chooser = 3
   #chooser = random.randint(1,4)
   if(chooser == 1):
      #percent
      question = "%.2f is what percent of %d?" % (part, whole)
      answer = percent
   if(chooser == 2):
      #whole
      question = "%d percent of what is %.2f?" % (percent, part)
      answer = whole
   if(chooser == 3):
      #part
      question = "%d percent  of %d is what?" % (percent, whole)
      answer = '%.2f'%part
   if(chooser == 4):
      question = "What percent of %d is %.2f?" % (whole, part)
      answer = percent
   answer = format_float(answer)
   Question.question, Question.answer = question, answer

def hardPercentages():
   Question.answerType = "numerical"
   percent = random.randint(50,100)*1.0
   whole = random.randint(50,100)*1.0
   part = whole*(percent/100.0)
   chooser = 3
   #chooser = random.randint(1,4)
   if(chooser == 1):
      #percent
      question = "%.2f is what percent of %d?" % (part, whole)
      answer = percent
   if(chooser == 2):
      #whole
      question = "%d percent of what is %.2f?" % (percent, part)
      answer = whole
   if(chooser == 3):
      #part
      question = "%d percent  of %d is what?" % (percent, whole)
      answer = '%.2f'%part
   if(chooser == 4):
      question = "What percent of %d is %.2f?" % (whole, part)
      answer = percent
   answer = format_float(answer)
   Question.question, Question.answer = question, answer

def sysEqZeroPair():
    Question.answerType = "numerical"
    x = random.randint(1,9)
    yCoefficient = random.randint(1,9)
    x1Coefficient = random.randint(1,9)
    x2Coefficient = random.randint(1,9)
    solution = (x1Coefficient+x2Coefficient)*random.randint(1,5)
    solution1 = solution - random.randint(1,solution)
    solution2 = solution - solution1
    Question.question = "%dy + %dx = %d and -%dy + %dx = %d Solve for x: " % (yCoefficient,x1Coefficient,solution1,yCoefficient,x2Coefficient,solution2)
    Question.answer = solution

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

addition = [
            add,
            addMultipleChoice,
            subtract,
            addSubtract,
            multiply,
            divide,
            multiplyDivide,
            allOperations,
            divideSingleDigitQuotient,
            divideSingleDigitQuotientMultiple10,
            divideDoubleDigitQuotient,
            divideDoubleDigitDivisor,
            divideDecimalEasy,
            divideDecimalMedium,
            divideDecimalHard,
            addDecimal,
            subtractDecimal,
            perfectSquaresto13,
            perfectSquares14to16,
            perfectSquaresFractions,
            perfectCubes2to5,
            addFractionCommonDenominator,
            #EquivalentFractions,
            multiplyFraction,
            divideFraction,
            GCF,
            LCM,
            convertDecimalPercent,
            convertDecimalFractionSimple,
            convertDecimalFractionReduce,
            EquivalentRatios,
            EquivalentRatiosOneStep,
            proportions,
            percentagesTenFifty,
            percentagesTenFiftyFindWhole,
            percentagesFiveTwenty,
            percentagesFiveTwentyFindWhole,
            percentagesUptoTwenty,
            percentagesUptoTwentyFindWhole,
            percentagesUptoTen,
            percentagesUptoTwenty,
            percentages,
            hardPercentages,
            sysEqZeroPair,
            sysEqZeroPair,
            sysEqZeroPair,
            sysEqZeroPair,
            sysEqZeroPair,
            sysEqZeroPair,
            sysEqZeroPair,
            sysEqZeroPair,
            sysEqZeroPair,
            sysEqZeroPair,
            sysEqZeroPair]

multiply = [ multiply]

Sheet.initialSheet()
for i in multiply:
    print(i)
    for i in range(100):
        Sheet.insertProblem(i)
Sheet.w.save("multiply.xls")

print("Awesome")
