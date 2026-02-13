
"""
    Name: movieAnalysis.py
    Author: Cristian M. Pagan 
    Date: August 5, 2025
    Purpose: Load and analyze the movie_bluebox 
    dataset for insights extraction.
"""

# Import pandas for data manipulation and analysis
import pandas as pd

# Import matplotlib for data visualization
import matplotlib.pyplot as plt 

def main():
    """ Main function to load the movie dataset and display information. """
    
    try:
        # Load the data from the Movie Dataset database
        movie_df = pd.read_csv('data/movie_dataset.csv')
        movie_data = movie_df.copy()
        print("Data loaded successfully!", "\n")
    except Exception as e:
        print(f"An error ocurred: {e}")

    # Question 1 - Show the number of rows        
    print(f"Number of movies: {movie_data.shape[0]}", "\n")

    # Question 2 - Show a preview of the data
    print("Showing the first 5 rows of the dataset...")
    print(movie_data.head(), "\n")

    # Question 3 - Displays a summary of the DataFrame
    print("Showing the column names and dataset info: ")
    print(movie_data.info(), "\n")

    # Question 4 - Get basic statistics for the budget
    print("Basic statistics for the budget: ")
    print(movie_data['budget'].describe(), "\n")

    # Question 5 - The highest and lowest ratings in the dataset
    best_rating = movie_data['rating'].max()
    worst_rating = movie_data['rating'].min()
    range_rating = best_rating - worst_rating

    print(f"The highest rating is {best_rating}")
    print(f"The lowest rating is {worst_rating}")
    print(f"The rating range is {range_rating}", "\n")

    # Question 6 - Oldest and newest movie
    oldest_year = movie_data['releaseYear'].min()
    newest_year = movie_data['releaseYear'].max()
    range_year = newest_year - oldest_year

    print(f"The oldest movie was released in {oldest_year}")
    print(f"The newest movie was released in {newest_year}")
    print(f"The range of movie release years is {range_year}\n")

    # Question 7 - Number of movies per release year
    movies_year = movie_data['releaseYear'].value_counts().sort_index()
    print("Number of movies released each year:")
    for year, count in movies_year.items():
        print(f"{year}: {count}")
    print()

    # Question 8 - Average movie rating by genre
    average_rating_genre = movie_data.groupby('genre')['rating'].mean()
    print("Average rating by genre:")
    print(average_rating_genre, "\n")

    # Question 9 - Most common language in movies
    predominant_language = movie_data['language'].mode()[0]
    print(f"Most common language: {predominant_language}", "\n")

    # Question 10 - Movies directed by a specific director
    movies_director = movie_data[movie_data['director'] == 'Ingmar Goldine']
    print("Movies directed by Ingmar Goldine:")
    print(movies_director, "\n")

    # Question 11 - Movies with titles starting with 'S'
    movies_letter = movie_data[movie_data['titleMovie'].str.startswith('S')]
    print("Movies with titles starting with 'S':")
    print(movies_letter, "\n")

    # Question 12 - Movies produced per decade
    movie_data['decade'] = (movie_data['releaseYear'] // 10) * 10
    movies_decade = movie_data.groupby('decade').size()
    print(f"Películas producidas en cada década: ")
    print(movies_decade, "\n")

    # Question 13 - Average movie budget by release year
    average_budget_year = movie_data.groupby('releaseYear')['budget'].mean()
    print("Average budget per release year:")
    print(average_budget_year, "\n")

    # Question 14 - Correlation between budget and rating
    budget_rating_corr = movie_data[['budget', 'rating']].corr().iloc[0, 1]
    print(f"Correlation between budget and rating: {budget_rating_corr}\n")

    # Question 15 - Most common movie genre
    most_common_genre = movie_data['genre'].mode()[0]
    print(f"Género más común: {most_common_genre}\n")

    # Question 16 - Country that produced the most movies
    most_productive_country = movie_data['country'].mode()[0]
    print(f"Country with the most movies produced: {most_productive_country}\n")

    # Question 17 - Pie chart of movie classification
    # Create a pie chart to visualize the proportion of each classification
    rating_counts = movie_data['classifaction'].value_counts()
    plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.2f%%')
    plt.title('Proportion of Movie Classifications')
    plt.show()

    # Question 18 - Boxplot of multiple attributes
    # Generate boxplots for selected numerical columns
    boxplot_cols = ['releaseYear', 'rating', 'runtime', 'budget']
    
    movie_data[boxplot_cols].plot(kind='box', subplots=True, 
        layout=(2,2), figsize=(12,8))
    plt.suptitle('Boxplot of Release Year, Rating, Runtime and Budget')
    plt.show()

# Execute the main function only if this script is run directly
if __name__ == "__main__":
    main()
