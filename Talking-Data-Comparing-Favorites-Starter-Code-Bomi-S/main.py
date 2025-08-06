#Talking Data Starter Code

#Part 2 Setting up the program
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "The Iron Giant"

print("My favorite movie is " + favMovie)


#Part 3 Investigate the data
print(movieData["movie_title"])


#Part 4 Filter data
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information
favMovieBooleanList = movieData["movie_title"] == favMovie
#print(favMovieBooleanList)
favMovieData = movieData.loc[favMovieBooleanList]
print(favMovieData)


print("\n\n")

#Create a new variable to store a new data set with a certain genre

animationMovieBooleanList = movieData["genres"].str.contains("Animation")
animationMovieData = movieData.loc[animationMovieBooleanList]


numOfMovies = animationMovieData["movie_title"].shape[0]

print("We will be comparing " + favMovie +
      " to other movies under the genre Animation in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Animation.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#Part 5 Describe data
#min
min = animationMovieData["audience_rating"].min()
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " is rated " + str(90 - min) + " points higher than the lowest rated movie.")
print()

#find max
max = animationMovieData["audience_rating"].max()
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated " + str(max - 90) + " points lower than the highest rated movie.")
print()

#find mean
mean = animationMovieData["audience_rating"].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " is higher than the mean movie rating.")

#find median
median = animationMovieData["audience_rating"].median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " is higher than the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 6 Create graphs
#Create histogram
plt.hist(animationMovieData["audience_rating"], range = (0, 100), bins = 20)

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Animated Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Animation Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, the data is left skewed and unimodal."
)
print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show histogram
plt.show()

#Create scatterplot
plt.scatter(data = animationMovieData, x = "audience_rating", y = "critic_rating")

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Ratings vs. Critic Ratings of Animated Movies")
plt.xlabel("Audience Ratings")
plt.ylabel("Critic Ratings")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, there is a positive correlation between audience ratings and critic ratings."
)
print()

print("Close the graph by pressing the 'X' in the top right corner.")

#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
