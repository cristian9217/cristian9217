##############################################################
# File: modalityStudent.R                                    #
# Author: Cristian M. Pagan 841-17-0264                      #
# Course: SICI 4997 - Special Topics and New Technologies    #
# Date: September 11, 2021                                   #
##############################################################

## Guarda los datos del archivo del csv (comma-separated values)
myData <- read.csv("uprb_database.csv", header = TRUE)

## Convierte los datos guardados en myData a un dataframe para ser estudiado.
studentData <- data.frame(myData)

## This function returns the amount of data for each semester and its modality.
modalityTerm = function(term, modality){
  return (length(which(studentData[[1]] == term & 
                       studentData[[11]] == modality)))
}

## This function returns the amount of data for each semester and its modality
## by the course code. 
modalityTermCourse = function(term, modality, courseCode){
  return (length(which(studentData[[1]] == term & 
                       studentData[[11]] == modality & 
                       studentData[[2]] == courseCode)))
}

## This function returns the amount of data for each semester
## by the course code. 
modalityCourse = function(term, courseCode){
  return (length(which(studentData[[1]] == term &
                       studentData[[2]] == courseCode)))
}

## This function returns the amount of data for each semester
## by the full name of the profesor given the course. 
modalityProfesor = function(term, fullnameProfesor){
  return (length(which(studentData[[1]] == term &
                       studentData[[10]] == fullnameProfesor)))
}

## This function returns the amount of data for each semester
## by the days given the course. 
modalityTermDays = function(term, days) {
  return (length(which(studentData[[1]] == term & 
                       studentData[[7]] == days)))
}

## This function returns the amount of data for each semester. 
showCourseTerm = function(term) {
  return (length(which(studentData[[1]] == term)))
}

pieChart = function(term) {
  hybrid = modalityTerm(term, "(H) - Hybrid")
  presencial = modalityTerm(term, "(P) - Presencial")
  distance = modalityTerm(term, "(D) - Distance")
  
  # Create data for the pie chart graph.
  totalModality <- c(hybrid, presencial, distance)
  labels <- c("Hybrid","Presencial","Distance")
  piepercent<- round(100* totalModality / sum(totalModality), 2)
  
  # Plot the pie chart graph.
  pie(totalModality, labels = paste(piepercent, "%"), 
      main = paste("Modality for the semester", term), 
      col = rainbow(length(totalModality))) 
      legend("topright", labels, cex = 0.9, 
      fill = rainbow(length(totalModality)))
}


## Show the amount of data for each semester and its hybrid modality.
hybridC12 <- modalityTerm("C12", "(H) - Hybrid")
sprintf("Semester C12 has %d in hybrid mode.", hybridC12)

hybridC11 <- modalityTerm("C11", "(H) - Hybrid")
sprintf("Semester C11 has %d in hybrid mode.", hybridC11)

hybridC03 <- modalityTerm("C03", "(H) - Hybrid")
sprintf("Semester C03 has %d in hybrid mode.", hybridC03)

hybridC02 <- modalityTerm("C02", "(H) - Hybrid")
sprintf("Semester C02 has %d in hybrid mode.", hybridC02)

## Show the amount of data for each semester and its face-to-face modality.
presencialC12 <- modalityTerm("C12", "(P) - Presencial")
sprintf("Semester C12 has %d in face-to-face mode.", presencialC12)

presencialC11 <- modalityTerm("C11", "(P) - Presencial")
sprintf("Semester C11 has %d in face-to-face mode.", presencialC11)

presencialC03 <- modalityTerm("C03", "(P) - Presencial")
sprintf("Semester C03 has %d in face-to-face mode.", presencialC03)

presencialC02 <- modalityTerm("C02", "(P) - Presencial")
sprintf("Semester C02 has %d in face-to-face mode.", presencialC02)

## Show the amount of data for each semester and its distance modality.
distanceC12 <- modalityTerm("C12", "(D) - Distance")
sprintf("Semester C12 has %d in distance mode.", distanceC12)

distanceC11 <- modalityTerm("C11", "(D) - Distance")
sprintf("Semester C11 has %d in distance mode.", distanceC11)

distanceC03 <- modalityTerm("C03", "(D) - Distance")
sprintf("Semester C03 has %d in distance mode.", distanceC03)

distanceC02 <- modalityTerm("C02", "(D) - Distance")
sprintf("Semester C02 has %d in distance mode.", distanceC02)

## Show the amount of data for each semester, its face-to-face modality and
## the course code is COTI3101 - Algorithms & Prog Dev I
cotiPresC11 <- modalityTermCourse("C11", "(P) - Presencial", "COTI3101")
sprintf("Semester C11 in COTI3101 has %d in presencial mode.", cotiPresC11)

## Show the amount of data which been created from COTI 3101 for semester C11
coti3101C11 <- modalityCourse("C11", "COTI3101")
sprintf("Semester C11 in COTI3101 has the amount of %d.", coti3101C11)

## Show the amount of data which has been teach by a professor for semester C11
profSolaC11 <- modalityProfesor("C11", "JUAN M. SOLA SLOAN") 
sprintf("Semester C11 has the professor Juan M. Sola is given %d courses.", 
        profSolaC11)

## Show the amount of data which been created are 
## offered on Tuesdays and Thursdays in semester C11
TwoDaysC11 <- modalityTermDays("C11", "TuTh")
sprintf("On Tuesdays and Thursdays at %d courses are offered in term C11.", 
         TwoDaysC11)

## Show the amount of data which been created are 
## offered on Wednesday in semester C11
OneDayC11 <- modalityTermDays("C11", "W")
sprintf("On Wednesday at %d courses are offered in term C11.", OneDayC11)

## Mostrar la cantidad de datos de cada semestre.
totalC12 <- showCourseTerm("C12")
sprintf("There are %d courses created in semester C12.", totalC12)

totalC11 <- showCourseTerm("C11")
sprintf("There are %d courses created in semester C11.", totalC11)

totalC03 <- showCourseTerm("C03")
sprintf("There are %d courses created in semester C03.", totalC03)

totalC02 <- showCourseTerm("C02")
sprintf("There are %d courses created in semester C02.", totalC02)

## Show data of the courses offered in semester C02 and C11. 
sprintf("Term C02 has %d courses and Term C11 has %d courses.", 
         totalC02, totalC11)

## The difference of courses between two semesters.
countCourses <- (totalC11 - totalC02)
sprintf("The difference between C11 and C02 is %d courses.", countCourses)

print("Printing the graphs...")
pieChart("C12")
pieChart("C11")
pieChart("C03")

# Create the data for the chart
amountCourse <- c(totalC12, totalC11, totalC03, totalC02, 1050)
labelTerm <- c("C12","C11","C03","C02", "Default")

# Plot the bar chart 
bp <- barplot(amountCourse,names.arg=labelTerm, xlab="Semester (Term)",
              ylab="Amount of Courses",col="blue",
              main="Total of Courses created by semester",border="red")
              text(x = bp, y = amountCourse, label = amountCourse, pos = 3, cex = 1)
