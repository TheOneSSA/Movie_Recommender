# Movie_Recommender
An interactive movie recommendation system that recommends the user top movies based on user's choices, using content-based filtering.
Here's the dataset we collected from different sources: https://github.com/TheOneSSA/IMDb_Movies_Datasets

For deployment, we used Flask web framework and the Heroku platform.
Link to the web application :- https://project-movie-recommender.herokuapp.com/ (some features aren't working properly, as Heroku has a 512 MB dyno limit under free subscription, but it will run properly on deploying on your local machine, with RAM >= 2 GB)

# Files Brief

In the *Movie Recommender.ipynb* file the Data Preprocessing part has been done. The sparse matrices for each genre has also been saved in the folder - *sparse_matrices*.

The application is run from the *app.py* file.

*Procfile and requirements.txt* consists of all the requirements for deployment in Herolu platform.

Folder - *datasets* and *sparse_matrices* has genre-wise datasets + 1 master dataset of 75k+ movies and sparse matrices containing the Tf-idf scores of each, respectively.

Folder - *templates* has all the html files, for diiferent pages.

Folder - *static* has all the files for flask routing.
