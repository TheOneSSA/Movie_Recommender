import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import scipy.sparse as sp #for loading the sparse matrices of each genre
import sklearn.preprocessing as pp #for modified cosine_similarity function

# defining a function that recommends 20 most similar movies
def getRecommendations(movie, df, sparse_mat):
    movie = movie.lower()
    found = True
    title = []
    year = []
    description = []
    rating = []
    # check if the movie is in our database or not
    if movie not in df['movie_title'].unique():
        found = False
    else:
        found = True
        sim_mat = cosine_similarity(sparse_mat.T)
        
        movie_index = df[df.movie_title == movie].index[0]
        scores = sim_mat[movie_index].toarray()
        index_recomm = scores.T.argsort(axis=0)[-21:-1]
        
        for i in np.flipud(index_recomm):
            title.append(df.original_title[i[0]])
            year.append(df.year[i[0]])
            description.append(df.description[i[0]])
            rating.append(df.avg_vote[i[0]])
            
    return found, title, year, description, rating

# defining a modified way to find the cosine similarity
def cosine_similarity(mat):
    col_normed_mat = pp.normalize(mat.tocsc(), axis=0)
    return col_normed_mat.T * col_normed_mat

app = Flask(__name__)

# routing for each webpage
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/em_angry")
def em_angry():
    return render_template('em_angry.html')

@app.route("/em_anxious")
def em_anxious():
    return render_template('em_anxious.html')

@app.route("/em_serious")
def em_serious():
    return render_template('em_serious.html')

@app.route("/em_excited")
def em_excited():
    return render_template('em_excited.html')

@app.route("/em_happy")
def em_happy():
    return render_template('em_happy.html')

@app.route("/em_irritated")
def em_irritated():
    return render_template('em_irritated.html')

@app.route("/em_lonely")
def em_lonely():
    return render_template('em_lonely.html')

@app.route("/em_relaxed")
def em_relaxed():
    return render_template('em_relaxed.html')

@app.route("/em_nothing")
def em_nothing():
    return render_template('em_nothing.html')

@app.route("/em_romantic")
def em_romantic():
    return render_template('em_romantic.html')

@app.route("/em_sad")
def em_sad():
    return render_template('em_sad.html')

@app.route("/gen_all")
def gen_all():
    return render_template('gen_all.html')

@app.route("/gen_action")
def gen_action():
    return render_template('gen_action.html')

@app.route("/gen_adventure")
def gen_adventure():
    return render_template('gen_adventure.html')

@app.route("/gen_animation")
def gen_animation():
    return render_template('gen_animation.html')

@app.route("/gen_biography")
def gen_biography():
    return render_template('gen_biography.html')

@app.route("/gen_comedy")
def gen_comedy():
    return render_template('gen_comedy.html')

@app.route("/gen_crime")
def gen_crime():
    return render_template('gen_crime.html')

@app.route("/gen_documentary")
def gen_documentary():
    return render_template('gen_documentary.html')

@app.route("/gen_drama")
def gen_drama():
    return render_template('gen_drama.html')

@app.route("/gen_family")
def gen_family():
    return render_template('gen_family.html')

@app.route("/gen_fantasy")
def gen_fantasy():
    return render_template('gen_fantasy.html')

@app.route("/gen_filmnoir")
def gen_filmnoir():
    return render_template('gen_filmnoir.html')

@app.route("/gen_history")
def gen_history():
    return render_template('gen_history.html')

@app.route("/gen_horror")
def gen_horror():
    return render_template('gen_horror.html')

@app.route("/gen_music")
def gen_music():
    return render_template('gen_music.html')

@app.route("/gen_musical")
def gen_musical():
    return render_template('gen_musical.html')

@app.route("/gen_mystery")
def gen_mystery():
    return render_template('gen_mystery.html')

@app.route("/gen_romance")
def gen_romance():
    return render_template('gen_romance.html')

@app.route("/gen_scifi")
def gen_scifi():
    return render_template('gen_scifi.html')

@app.route("/gen_sport")
def gen_sport():
    return render_template('gen_sport.html')

@app.route("/gen_thriller")
def gen_thriller():
    return render_template('gen_thriller.html')

@app.route("/gen_war")
def gen_war():
    return render_template('gen_war.html')

@app.route("/gen_western")
def gen_western():
    return render_template('gen_western.html')

# final function for recommendations
@app.route("/recommend")
def recommend():
    movie = request.args.get('movie')
    genre = request.args.get('genre')
    genre = genre.lower()
    
    # declaring a generic address for all the files
    s1 = "datasets/" + genre + "_df.csv";
    s2 = "sparse_matrices/" + genre + "_sm.npz";
    
    data = pd.read_csv(s1)
    sparse_mat = sp.load_npz(s2)
    
    found, title, year, description, rating = getRecommendations(movie, data, sparse_mat)
    movie = movie.upper()
    
    if found == False:
        return render_template('recommend.html',movie=movie,title=title,year=year,description=description,rating=rating,found='NO')
    else:
        return render_template('recommend.html',movie=movie,title=title,year=year,description=description,rating=rating,found='YES')

if __name__ == '__main__':
    app.run()