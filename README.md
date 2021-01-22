# Quantitative Analysis of Sexually Explicit Lyrics in Female Rap Music

by Parth Wokhlu and Mihir Nakra 

Parth Wokhlu: parth.wokhlu.843@gmail.com

Mihir Nakra: nakramihir@gmail.com

# I. Introduction

After spending the past year delving into rap music as a whole, the wide variety of topics/subjects discussed became extremely intriguing to us. Specifically, with the rise of rappers like Megan Thee Stallion and Cardi B, we noticed that there was a general stereotype that female rappers only rapped about sexually explicit material like intercourse and their own bodies. Thus, we decided to use ML to find whether or not this consensus was legitimate.

# II. Methodology
All the code for this project is open sourced (not all of it is written completely by us, so please give the original authors their due credit). 
## Data Collection
The first step was collecting a list of female rappers. To do this, we combined 2 comprehensive lists of female rappers, one from Wikipedia and one from Genius. After collecting a list of about 310 female rappers, we used Fran Gonzalez’s Itunes API to get full tracklists for each artist, and then with those lists, we compiled all the song lyrics together using  John Miller’s Genius API. Once we had the lyrics for each of those artists, we needed to compile training data for the model to be able to predict if a song was sexually explicit. Our training data consisted of 50 songs that we knew contained sexually explicit themes and 50 songs that we knew did not. We then split up the list into 3 different training sets, which can be found under the “data/” directory. 
