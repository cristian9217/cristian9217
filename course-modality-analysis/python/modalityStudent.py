##############################################################
# File: modalityStudent.py                                   #
# Author: Cristian M. Pagan 841-17-0264                      #
# Course: SICI 4997 - Special Topics and New Technologies    #
# Date: September 11, 2021                                   #
##############################################################

## Import libraries
import pandas as pd ## For used to analyze data from dataframe.
import matplotlib.pyplot as plt ## For working with graphs
import numpy as np ## For used for working with arrays.
from pathlib import Path ## for working directories and files.

## The name of the filename of the dataset.
file = "uprb_database.csv"
# file = "C:\\Users\\crist\\Documents\\R\\C22_Python.csv"

## Throw an exception if file exists or not exists.
if Path(file).is_file():
    print(f"\nThe file {file:s} exist.")
else:
    raise FileNotFoundError(f"\nThe file {file:s} does not exist.")

## Reading csv to a dataframe
df = pd.read_csv(file)

## Returns the tuple of shape (rows, columns) of DataFrame.
row, col = df.shape

## Throw an excpetion if dataframe is empty or not empty.
if df.size > 0:
    print(f"{row:d} obs. of {col:d} variables\n")
else:
    raise Exception("Empty Dataset\n")    

def modalityTerm(term: str, modality: str):
    """ This function returns the amount of data for each semester and its modality. """
    return df[(df['Term'] == term) & (df['Modality'] == modality)]

def modalityTermCourse(term: str, modality: str, courseCode: str):
    """ This function returns the amount of data for each semester and its modality
        by the course code. """ 
    return df[(df['Term'] == term) & (df['Modality'] == modality) & 
              (df['Course'] == courseCode)]

def modalityCourse(term: str, courseCode: str):
    """ This function returns the amount of data for each semester
        by the course code. """
    return df[(df['Term'] == term) & (df['Course'] == courseCode)]

def modalityProfesor(term: str, nameProfesor: str):
    """ This function returns the amount of data for each semester
        by the full name of the profesor given the course. """
    return df[(df['Term'] == term) & (df['Professor'] == nameProfesor)]

def modalityTermDays(term: str, days: str):
    """ This function returns the amount of data for each semester
        by the days given the course. """
    return df[(df['Term'] == term) & (df['Days'].str.contains(days))]

def showCourseTerm(term: str):
    """ This function returns the amount of data for each semester.  """
    return df[(df['Term'] == term)]

def pieChart(term: str):
    """ Generates a pie chart of the each semester. """
    totalModality = []
    
    totalModality.insert(0, len(modalityTerm(term, "(H) - Hybrid")))
    totalModality.insert(1, len(modalityTerm(term, "(P) - Presencial")))
    totalModality.insert(2, len(modalityTerm(term, "(D) - Distance")))

    labelModality = ["Hybrid", "Presencial", "Distance"]

    if(sum(totalModality) < 1):
        print(f"No data found for the term {term:s}.")
    else:
        plt.pie(totalModality, labels = labelModality, autopct='%.1f%%')
        plt.legend()
        plt.title('Modality for the semester')
        plt.show()

## Show the amount of data for each semester and its hybrid modality.
hybridC22 = len(modalityTerm("C22", "(H) - Hybrid"))
print(f"Semester C22 has {hybridC22:d} in hybrid mode. ")

hybridC12 = len(modalityTerm("C12", "(H) - Hybrid"))
print(f"Semester C12 has {hybridC12:d} in hybrid mode. ")

hybridC11 = len(modalityTerm("C11", "(H) - Hybrid"))
print(f"Semester C11 has {hybridC11:d} in hybrid mode. ")

hybridC03 = len(modalityTerm("C03", "(H) - Hybrid"))
print(f"Semester C03 has {hybridC03:d} in hybrid mode. ")

hybridC02 = len(modalityTerm("C02", "(H) - Hybrid"))
print(f"Semester C02 has {hybridC02:d} in hybrid mode.\n")

## Show the amount of data for each semester and its face-to-face modality.
presencialC22 =  len(modalityTerm("C22", "(P) - Presencial"))
print(f"Semester C22 has {presencialC22:d} in face-to-face mode.")

presencialC12 =  len(modalityTerm("C12", "(P) - Presencial"))
print(f"Semester C12 has {presencialC12:d} in face-to-face mode.")

presencialC11 = len(modalityTerm("C11", "(P) - Presencial"))
print(f"Semester C11 has {presencialC11:d} in face-to-face mode.")

presencialC03 = len(modalityTerm("C03", "(P) - Presencial"))
print(f"Semester C03 has {presencialC03:d} in face-to-face mode.")

presencialC02 = len(modalityTerm("C02", "(P) - Presencial"))
print(f"Semester C02 has {presencialC02:d} in face-to-face mode.\n")

## Show the amount of data for each semester and its distance modality.
distanceC22 = len(modalityTerm("C22", "(D) - Distance"))
print(f"Semester C22 has {distanceC22:d} in distance mode.")

distanceC12 = len(modalityTerm("C12", "(D) - Distance"))
print(f"Semester C12 has {distanceC12:d} in distance mode.")

distanceC11 = len(modalityTerm("C11", "(D) - Distance"))
print(f"Semester C11 has {distanceC11:d} in distance mode.")

distanceC03 = len(modalityTerm("C03", "(D) - Distance"))
print(f"Semester C03 has {distanceC03:d} in distance mode.")

distanceC02 = len(modalityTerm("C02", "(D) - Distance"))
print(f"Semester C02 has {distanceC02:d} in distance mode.\n")

## Show the amount of data for each semester, its face-to-face modality and
## the course code is COTI3101 - Algorithms & Prog Dev I
cotiPresC11 = len(modalityTermCourse("C11", "(P) - Presencial", "COTI3101"))
print(f"Semester C11 in COTI3101 has {cotiPresC11:d} in presencial mode.\n")

## Show the amount of data which been created from COTI 3101 for semester C11
coti3101C11 = len(modalityCourse("C11", "COTI3101"))
print(f"Semester C11 in COTI3101 has the amount of {coti3101C11:d} courses.\n")

## Show the amount of data which has been teach by a professor for semester C11
profSolaC11 = len(modalityProfesor("C11", "JUAN M. SOLA SLOAN"))
print(f"Semester C11 has the professor Juan M. Sola is given {profSolaC11:d} courses.\n")            

## Show the amount of data which been created are 
## offered on Tuesdays and Thursdays in semester C11
TwoDaysC11 = len(modalityTermDays("C11", "TuTh"))
print(f"On Tuesdays and Thursdays at {TwoDaysC11:d} courses are offered in term C11.\n")

## Show the amount of data which been created are 
## offered on Wednesday in semester C11
OneDayC11 = len(modalityTermDays("C11", "W"))
print(f"On Wednesday at {OneDayC11:d} courses are offered in term C11.\n")

## Mostrar la cantidad de datos de cada semestre.
totalC22 = len(showCourseTerm("C22"))
print(f"There are {totalC22:d} courses created in semester C22.")

totalC12 = len(showCourseTerm("C12"))
print(f"There are {totalC12:d} courses created in semester C12.")

totalC11 = len(showCourseTerm("C11"))
print(f"There are {totalC11:d} courses created in semester C11.")

totalC03 = len(showCourseTerm("C03"))
print(f"There are {totalC03:d} courses created in semester C03.")

totalC02 = len(showCourseTerm("C02"))
print(f"There are {totalC02:d} courses created in semester C02.\n")

## Show data of the courses offered in semester C02 and C11. 
print(f"Term C12 has {totalC12:d} courses and Term C22 has {totalC22:d} courses.")

## The difference of courses between two semesters.
countCourses = totalC22 - totalC12
print(f"The difference between C12 and C22 is {countCourses:d} courses.\n")

print("Printing the pie chart graph...")
pieChart("C22")
pieChart("C12")
pieChart("C11")
pieChart("C03")

## Printing the bar of the chart graph.
print("Printing the bar chart graph...\n")

labelTerm = ["C22", "C12", "C11", "C03", "C02"]
totalPerTerm = [totalC22, totalC12, totalC11, totalC03, totalC02]

plt.bar(labelTerm, totalPerTerm, width= 0.5)

for i in range(len(labelTerm)):
    plt.text(i, totalPerTerm[i], totalPerTerm[i], ha = "center", va = "bottom")

plt.ylim([0, (max(totalPerTerm) + 200)])
plt.xlabel("Amount of courses")
plt.ylabel("Semester (Term)")
plt.title("Total of courses created by semester")
plt.show()
