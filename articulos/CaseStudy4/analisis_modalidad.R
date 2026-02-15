# File: analisis_modalidad.R
# Author: Cristian M. Pagan 
# Date: February 14, 2026
# Purpose: Load and analyze the cleaned 
# modalidad dataset for analysis in R.

df_modalidad <- read.csv("cleaned_modalidad.csv")

if (!exists("df_modalidad") || nrow(df_modalidad) == 0) {
  stop("df_modalidad is empty or not loaded.")
}

print("File was loaded with success and save as dataframe!")

# Show dataframe structure
print("Estructura del DataFrame")
sapply(df_modalidad, class)       

# Show first few rows
print("Primeras filas del DataFrame")
print(head(df_modalidad))

# Calculate and display average age
average_age <- mean(df_modalidad$Edad, na.rm = TRUE)
sprintf("La edad promedio de los estudiantes es %.0f años", average_age)

# Distribution by city
city_distribution <- table(df_modalidad$Municipio)
cat("Distribución de estudiantes por ciudad (top 5):\n")
print(head(sort(city_distribution, decreasing = TRUE), 5))

# Information by educational level
niveles <- unique(df_modalidad$NivelEducativo)
for (nivel in niveles) 
{
  nivelEducativo <- subset(df_modalidad, NivelEducativo == nivel)
  cat("\nInformación del nivel educativo:", nivel, "\n")
  
  tabla <- table(nivelEducativo$Programa, nivelEducativo$Modalidad)
  print(addmargins(tabla))
}

# City with the most students
conteo_municipio <- table(df_modalidad$Municipio)
municipio_max <- names(conteo_municipio)[which.max(conteo_municipio)]
print(paste("Municipio con más estudiantes:", municipio_max))

# Count of students in Distance modality
distancia <- subset(df_modalidad, Modalidad == "Distancia")
conteo_distancia <- table(distancia$NivelEducativo)
print("Conteo de estudiantes por modalidad a distancia:")
print(conteo_distancia)

# Count the number of students in each modality in Barplot
modalidades_count <- table(df_modalidad$Modalidad)
barplot(modalidades_count,
        main = "Distribución de Estudiantes por Modalidad",
        xlab = "Modalidad", ylab = "Número de Estudiantes",
        col = "skyblue")
