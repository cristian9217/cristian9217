import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# Load the data from the Movie_dataset database
movie_df = pd.read_csv('data/movie_dataset.csv')

#####################################################
# Question 2 - Indicar la cantidad de filas         #
#####################################################
print(f"Amount of movies: {movie_df.shape[0]}")

#####################################################
# Question 3 - Mostrar un preview de los datos      # 
#####################################################
print("Mostrando los primeros 5 datos...")
print(movie_df.head())

#####################################################
# Question 4 - Mostrar los informes de atributos    # 
#####################################################
print("Mostrando los nombre de los atributos: ")
print(movie_df.info())

######################################################
# Question 5 - Sacar la estadisticas del presupuesto #
######################################################
print("Estadisticas basicas del prespuesto: ")
print(movie_df['budget'].describe())

#########################################################
# Question 6 - La mejor y peor calificacion del dataset #
#########################################################
best_movie = movie_df['rating'].max()
worst_movie = movie_df['rating'].min()

print(f"\nLa mejor calificacion es {best_movie}")
print(f"La peor calificacion es {worst_movie}")
print(f"El rango de calificacion es: {best_movie - worst_movie}")

#########################################################
# Question 7 - Pelicula mas antingua y reciente         #
#########################################################
oldest_movie = movie_df['releaseYear'].min()
newest_movie = movie_df['releaseYear'].max()

print(f"\nLa pelicula mas antigua es {oldest_movie}")
print(f"La pelicula mas reciente es {newest_movie}")
print(f"El rango de anos de las peliculas es {newest_movie - oldest_movie}")

#########################################################
# Question 8 - Cantidad de peliculas por año de estreno # 
#########################################################
movies_by_year = movie_df['releaseYear'].value_counts().sort_index()
print(movies_by_year)

#################################################################
# Question 9 - Promedio de calificacion de peliculas por genero #
#################################################################
average_rating_by_genre = movie_df.groupby('genre')['rating'].mean()
print(average_rating_by_genre)

#########################################################
# Question 10 - Idioma mas utilizado en las peliculas   #
#########################################################
predominant_language = movie_df['language'].mode()[0]
print(f"El idioma más común en las películas es: {predominant_language}")

#########################################################
# Question 11 - Peliculas dirigidas por un director     #
#########################################################
movies_by_director = movie_df[movie_df['director'] == 'Ingmar Goldine']
print(movies_by_director)

########################################################
# Question 12 - Movie title starts with the letter S.  #
########################################################
movies_by_letter = movie_df[movie_df['titleMovie'].str.startswith('S')]
print(movies_by_letter)

#########################################################
# Question 13 - Peliculas mas producidas en cada decada #
#########################################################
movies_by_decade = movie_df.groupby(movie_df['releaseYear'] // 10 * 10).size()
print(f"Películas producidas en cada década: {movies_by_decade}")

##############################################################
# Question 14 - Prespupuesto medio de las peliculas por año. #
##############################################################
average_budget_by_year = movie_df.groupby('releaseYear')['budget'].mean()
print(f"Presupuesto promedio por año de lanzamiento: {average_budget_by_year}")

#########################################################
# Question 15 - Relacion entre el presupuesto y su calificacion. 
#########################################################
budget_rating_relation = movie_df[['budget', 'rating']].corr().iloc[0, 1]
print(f"Relación entre presupuesto y calificación: {budget_rating_relation}")

#########################################################
# Question 16 - Pelicula con el genero mas comun.
#########################################################
most_common_genre = movie_df['genre'].mode()[0]
print(f"Género más común: {most_common_genre}")

#####################################################################
# Question 17 - Pais que ha producido la mayor cantidad de peliculas
#####################################################################
most_productive_country = movie_df['country'].mode()[0]
print(f"País que ha producido la mayor cantidad de películas: {most_productive_country}")

#########################################################
# Question 18 - Grafica circular de classification
#########################################################
genre_counts = movie_df['classifaction'].value_counts()
print(genre_counts)
plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.2f%%')
plt.title('Proporción de la clasificación')
plt.show()

#########################################################
# Question 19 - Boxplot de multiples atributos
#########################################################
boxplot_cols = ['releaseYear', 'rating', 'runtime', 'budget']

movie_df[boxplot_cols].plot(kind='box', subplots=True, layout=(2,2), figsize=(10,8))
plt.suptitle('Boxplot de releaseYear, rating, runtime y budget')
plt.show()

