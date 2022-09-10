##############################################################
# File: modalityStudent.py                                   #
# Author: Cristian M. Pagan 841-17-0264                      #
# Course: SICI 4997 - Special Topics and New Technologies    #
# Date: September 11, 2021                                   #
##############################################################

# Import libraries
import pandas as pd ## For the CSV
import matplotlib.pyplot as plt ## Graphs
import numpy as np ## For the dataframe of the CSV. 

## Reading csv to a dataframe
df = pd.read_csv("uprb_database.csv")

## This function returns the amount of data for each semester and its modality.
def modalityTerm(term, modality):
    return df[(df['Term'] == term) & (df['Modality'] == modality)]

## This function returns the amount of data for each semester and its modality
## by the course code. 
def modalityTermCourse(term, modality, courseCode):
     return df[(df['Term'] == term) & (df['Modality'] == modality) & 
               (df['Course'] == courseCode)]

## This function returns the amount of data for each semester
## by the course code. 
def modalityCourse(term, courseCode):
    return df[(df['Term'] == term) & (df['Course'] == courseCode)]

## This function returns the amount of data for each semester
## by the full name of the profesor given the course. 
def modalityProfesor(term, fullnameProfesor):
    return df[(df['Term'] == term) & (df['Professor'] == fullnameProfesor)]

## This function returns the amount of data for each semester
## by the days given the course. 
def modalityTermDays(term, days):
    return df[(df['Term'] == term) & (df['Days'] == days)]

## This function returns the amount of data for each semester. 
def showCourseTerm(term):
    return df[(df['Term'] == term)]

def pieChart(term):
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
print("Semester C12 has {:d} in hybrid mode. ".format(hybridC12))

hybridC11 = len(modalityTerm("C11", "(H) - Hybrid"))
print("Semester C11 has {:d} in hybrid mode. ".format(hybridC11))

hybridC03 = len(modalityTerm("C03", "(H) - Hybrid"))
print("Semester C03 has {:d} in hybrid mode. ".format(hybridC03))

hybridC02 = len(modalityTerm("C02", "(H) - Hybrid"))
print("Semester C02 has {:d} in hybrid mode. ".format(hybridC02))

## Show the amount of data for each semester and its face-to-face modality.
presencialC12 =  len(modalityTerm("C12", "(P) - Presencial"))
print("Semester C12 has {:d} in face-to-face mode.".format(presencialC12))

presencialC11 = len(modalityTerm("C11", "(P) - Presencial"))
print("Semester C11 has {:d} in face-to-face mode.".format(presencialC11))

presencialC03 = len(modalityTerm("C03", "(P) - Presencial"))
print("Semester C03 has {:d} in face-to-face mode.".format(presencialC03))

presencialC02 = len(modalityTerm("C02", "(P) - Presencial"))
print("Semester C02 has {:d} in face-to-face mode.".format(presencialC02))

## Show the amount of data for each semester and its distance modality.
distanceC12 = len(modalityTerm("C12", "(D) - Distance"))
print("Semester C12 has {:d} in distance mode.".format(distanceC12))

distanceC11 = len(modalityTerm("C11", "(D) - Distance"))
print("Semester C11 has {:d} in distance mode.".format(distanceC11))

distanceC03 = len(modalityTerm("C03", "(D) - Distance"))
print("Semester C03 has {:d} in distance mode.".format(distanceC03))

distanceC02 = len(modalityTerm("C02", "(D) - Distance"))
print("Semester C02 has {:d} in distance mode.".format(distanceC02))

## Show the amount of data for each semester, its face-to-face modality and
## the course code is COTI3101 - Algorithms & Prog Dev I
cotiPresC11 = len(modalityTermCourse("C11", "(P) - Presencial", "COTI3101"))
print("Semester C11 in COTI3101 has {:d} in presencial mode.".format(cotiPresC11))

## Show the amount of data which been created from COTI 3101 for semester C11
coti3101C11 = len(modalityCourse("C11", "COTI3101"))
print("Semester C11 in COTI3101 has the amount of {:d}.".format(coti3101C11))

## Show the amount of data which has been teach by a professor for semester C11
profSolaC11 = len(modalityProfesor("C11", "JUAN M. SOLA SLOAN"))
print("Semester C11 has the professor Juan M. Sola is given {:d} courses.".
       format(profSolaC11))

## Show the amount of data which been created are 
## offered on Tuesdays and Thursdays in semester C11
TwoDaysC11 = len(modalityTermDays("C11", "TuTh"))
print("On Tuesdays and Thursdays at {:d} courses are offered in term C11.". 
        format(TwoDaysC11))

## Show the amount of data which been created are 
## offered on Wednesday in semester C11
OneDayC11 = len(modalityTermDays("C11", "W"))
print("On Wednesday at {:d} courses are offered in term C11.".
        format(OneDayC11))

## Mostrar la cantidad de datos de cada semestre.
totalC12 = len(showCourseTerm("C12"))
print("There are {:d} courses created in semester C12.".format(totalC12))

totalC11 = len(showCourseTerm("C11"))
print("There are {:d} courses created in semester C11.".format(totalC11))

totalC03 = len(showCourseTerm("C03"))
print("There are {:d} courses created in semester C03.".format(totalC03))

totalC02 = len(showCourseTerm("C02"))
print("There are {:d} courses created in semester C02.".format(totalC02))

## Show data of the courses offered in semester C02 and C11. 
print("Term C02 has {:d} courses and Term C11 has {:d} courses.".
        format(totalC02, totalC11))

## The difference of courses between two semesters.
countCourses = totalC11 - totalC02
print("The difference between C11 and C02 is {:d} courses.". 
        format(countCourses))

print("Printing the pie chart graph...")
pieChart("C12")
pieChart("C11")
pieChart("C03")

print("Printing the bar chart graph")
labelTerm = np.array(["C12", "C11", "C03", "C02"])
totalPerTerm = np.array([totalC12, totalC11, totalC03, totalC02])

plt.bar(labelTerm, totalPerTerm, width= 0.5)
plt.xlabel("Amount of courses")
plt.ylabel("Semester (Term)")
plt.title("Total of courses created by semester")
plt.show()
