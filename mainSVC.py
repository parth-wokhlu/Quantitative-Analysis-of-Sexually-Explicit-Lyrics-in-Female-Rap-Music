import lyricsgenius
import numpy as np
import json
import config
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from collections import Counter
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import SVC

# Initialize the genius object from the lyricsgenius api
genius = lyricsgenius.Genius(config.geniusToken)

# Initialize the global count_vect and tfidf_transformer variables
# These will be used to format the song lyrics
count_vect = CountVectorizer()
tfidf_transformer = TfidfTransformer()


# This method reads the training data from the data folder and formats it using the count_vect and tfidt_transformer
# It then creates an SVC linear model and trains it with the data it formatted
# It returns the trained model
def train():
    global count_vect, tfidf_transformer
    df = pd.read_csv('data/dataV1.csv')

    counter = Counter(df['Topic'].tolist())
    top_2_varieties = {i[0]: idx for idx, i in enumerate(counter.most_common(2))}
    print(top_2_varieties)
    df = df[df['Topic'].map(lambda x: x in top_2_varieties)]

    description_list = df['Lyrics'].tolist()
    varietal_list = [top_2_varieties[i] for i in df['Topic'].tolist()]
    varietal_list = np.array(varietal_list)
    x_train_counts = count_vect.fit_transform(description_list)
    x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts, 15)

    clf = SVC(kernel='linear').fit(x_train_tfidf, varietal_list)
    return clf


# This removes the extra phrases (such as "[Chorus]") that are returned from the lyricsgenius api
def removeExtra(lyrics):
    for i in range(0, 10):
        try:
            a = lyrics.index("[")
            b = lyrics.index("]")
            lyrics = lyrics[0:a] + lyrics[b + 1:len(lyrics)]

        except:
            break

    temp = lyrics.split("\n")
    str = ""
    for l in temp:
        str += l + " "


    return str


# Gets the starting year and intializes the songs variable with the song names
# Intializes the variables needed to quantify the data (i.e. numTotal, numRacist, count, totalSongs)

with open("allFemaleSongs.json", "r") as file:
    songs = json.load(file)

songLyrics = []
clf = train()

numTotal = 0
numExplicit = 0
numExplicitArtist = 0
count = 0


# Gets the prediction using the song lyrics and model
# returns an array this is either equal to [0] if the song has themes of racism or
# [1] if it does not
def getPredict(lyrics, clf):
    global count_vect, tfidf_transformer
    x_train_counts = count_vect.transform([lyrics])
    x_test = tfidf_transformer.transform(x_train_counts)
    return clf.predict(x_test)


# Gets predictions for all the songs through 2020
# Saves the predictions in a text file
for artist in songs:
    lyrics = songs.get(artist)
    if (len(lyrics) > 0):
        for lyric in lyrics:
            lyric = removeExtra(lyric)
            prediction = getPredict(lyric, clf)
            if prediction[0] == 1:
                numExplicit += 1
                numExplicitArtist += 1

        file = open("results.txt", "a")
        file.write(artist + ": " + str(numExplicitArtist) + "/" + str(len(lyrics)) + " = " + str(numExplicitArtist / len(lyrics)) + "\n")
        numExplicitArtist = 0

file = open("results.txt", "a")
file.write("\nTotal Explicit Songs: " + str(numExplicit) + "/2735 = " + str(numExplicit/2735))