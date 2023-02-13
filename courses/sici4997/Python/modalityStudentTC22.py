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

# file = "uprb_database.csv"
file = "C:\\Users\\crist\\Documents\\R\\C22_Python.csv"

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
    return df[(df['Term'] == term) & (df['Days'] == days)]

## This function returns the amount of data for each semester. 
def showCourseTerm(term: str):
    return df[(df['Term'] == term)]

def pieChart(term: str):
    hybrid = len(modalityTerm(term, "(H) - Hybrid"))
    presencial = len(modalityTerm(term, "(P) - Presencial"))
    distance = len(modalityTerm(term, "(D) - Distance"))

    totalModality = np.array([hybrid, presencial, distance])
    labelModality = ["Hybrid", "Presencial", "Distance"]

    plt.pie(totalModality, labels = labelModality, autopct='%1.2f%%')
    plt.legend()
    plt.title("Modality for the semester")
    plt.show()

## Show the amount of data for each semester and its hybrid modality.
hybridC12 = len(modalityTerm("C12", "(H) - Hybrid"))
print(f"Semester C12 has {hybridC12:d} in hybrid mode.")

hybridC22 = len(modalityTerm("C22", "(H) - Hybrid"))
print(f"Semester C22 has {hybridC22:d} in hybrid mode.\n")

## Show the amount of data for each semester and its face-to-face modality.
presencialC12 =  len(modalityTerm("C12", "(P) - Presencial"))
print(f"Semester C12 has {presencialC12:d} in face-to-face mode.")

presencialC22 =  len(modalityTerm("C22", "(P) - Presencial"))
print(f"Semester C22 has {presencialC22:d} in face-to-face mode.\n")

## Show the amount of data for each semester and its distance modality.
distanceC12 = len(modalityTerm("C12", "(D) - Distance"))
print(f"Semester C12 has {distanceC12:d} in distance mode.")

distanceC22 = len(modalityTerm("C22", "(D) - Distance"))
print(f"Semester C22 has {distanceC22:d} in distance mode.\n")

## Show the amount of data for each semester, its face-to-face modality and
## the course code is COTI3101 - Algorithms & Prog Dev I
cotiPresC12 = len(modalityTermCourse("C12", "(P) - Presencial", "COTI3101"))
print(f"Semester C12 in COTI3101 has {cotiPresC12:d} in presencial mode.")

cotiPresC22 = len(modalityTermCourse("C22", "(P) - Presencial", "COTI3101"))
print(f"Semester C22 in COTI3101 has {cotiPresC22:d} in presencial mode.\n")

## Show the amount of data which been created from COTI 3101 for semester C22
coti3101C12 = len(modalityCourse("C12", "COTI3101"))
print(f"Semester C12 in COTI3101 has the amount of {coti3101C12:d} courses.")

coti3101C22 = len(modalityCourse("C22", "COTI3101"))
print(f"Semester C22 in COTI3101 has the amount of {coti3101C22:d} courses.\n")

## Show the amount of data which has been teach by a professor for semester C22
profSolaC12 = len(modalityProfesor("C12", "JUAN M. SOLA SLOAN"))
print(f"Semester C12 has the professor Juan M. Sola is given {profSolaC12:d} courses.")    

profSolaC22 = len(modalityProfesor("C22", "JUAN M. SOLA SLOAN"))
print(f"Semester C22 has the professor Juan M. Sola is given {profSolaC22:d} courses.\n")            

## Show the amount of data which been created are 
## offered on Tuesdays and Thursdays in semester C22
TwoDaysC12 = len(modalityTermDays("C12", "TuTh"))
print(f"On Tuesdays and Thursdays at {TwoDaysC12:d} courses are offered in term C12.")

TwoDaysC22 = len(modalityTermDays("C22", "TuTh"))
print(f"On Tuesdays and Thursdays at {TwoDaysC22:d} courses are offered in term C22.\n")

## Show the amount of data which been created are 
## offered on Wednesday in semester C22
OneDayC12 = len(modalityTermDays("C12", "W"))
print(f"On Wednesday at {OneDayC12:d} courses are offered in term C12.")

OneDayC22 = len(modalityTermDays("C22", "W"))
print(f"On Wednesday at {OneDayC22:d} courses are offered in term C22.\n")

## Mostrar la cantidad de datos de cada semestre.
totalC12 = len(showCourseTerm("C12"))
print(f"There are {totalC12:d} courses created in semester C12.")

totalC22 = len(showCourseTerm("C22"))
print(f"There are {totalC22:d} courses created in semester C22.\n")

## Show data of the courses offered in semester C02 and C11. 
print(f"Term C12 has {totalC12:d} courses and Term C22 has {totalC22:d} courses.")

## The difference of courses between two semesters.
countCourses = totalC22 - totalC12
print(f"The difference between C12 and C22 is {countCourses:d} courses.\n")

## Printing the pie of the chart graph.
print("Printing the pie chart graph...")
pieChart("C12")
pieChart("C22")

## Printing the bar of the chart graph.
print("Printing the bar chart graph...\n")

labelTerm = ["C22", "C12"]
totalPerTerm = [totalC22, totalC12]

plt.bar(labelTerm, totalPerTerm, width= 0.5)

for i in range(len(labelTerm)):
    plt.text(i, totalPerTerm[i], totalPerTerm[i], ha = "center", va = "bottom")

plt.ylim([0, (max(totalPerTerm) + 200)])
plt.xlabel("Amount of courses")
plt.ylabel("Semester (Term)")
plt.title("Total of courses created by semester")
plt.show()
