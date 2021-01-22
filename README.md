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

## Neural Network
At first, the idea of a neural network seemed like a far off possibility. It seemed interesting, but neither of us had any idea what it actually was. As we delved into the topic, we found numerous [YouTube videos](https://www.youtube.com/watch?v=aircAruvnKk&feature=youtu.be) and [articles](https://news.codecademy.com/taylor-swift-lyrics-machine-learning/) that allowed us to wrap our heads around this topic. 

From what we understood, the method we should attack this problem with was to classify a song based on the lyrics using a linear support vector machine. This method had a fast computational time and could provide accurate results without thousands and thousands of training inputs. Essentially, a linear support vector machine is made to mathematically determine a hyperplane which will allow it to classify data points. A hyperplane is, to put it simply, a line of best fit for the data with a margin outside of it. The calculations done by the machine create a hyperplane with the largest margin possible so that data can be classified as accurately as possible. 

So now we have the hard part: how do we turn words into data points for the machine to use? The method we used was implementing a count vectorizer, which creates a matrix using the words given. An example of this is below:

![Example of count vectorizer matrix](https://kavita-ganesan.com/wp-content/uploads/how-hashingvectorizer-works.png)

From the matrix, we used something called a tfidf transformer to allow the machine to get a better understanding of what words matter. A tfidf transformer highlights the words that are unique to certain songs and helps to reduce the influence of a word like “the,” which appears likely in all songs numerous times. After applying these calculations to our text, we gave the training data to the model and allowed it to determine the hyperplane. To do all of this, we used the python sklearn library.

To determine the accuracy of our training data, we split it up so that 70% of it would be used to train and then 30% of it would be used to test. We would then train the model with that 70% and tell it to predict the themes of the song of the remaining 30% of the songs. Then we would compare the data it predicted to what we know it should’ve predicted. We tested it many times, and it had an average accuracy of about 85%. 

After determining our model was fairly accurate, we could use it to predict the themes of all the songs we had. Each time we wanted to predict if a song contained sexually explicit themes in it, we could give that model the count vectorized and tfidf transformed song lyric, and using the already determined hyperplane, it would identify where the song lyrics would lie on the graph in relation to the hyperplane. Based on that it would tell us if a certain song contained the ideas of racial injustice or not. This type of machine learning that we are using is called supervised learning, in which the program is given prior knowledge of what kinds of things it should categorize into each section.

The credit for providing us with the design of this model goes to [Shanglun Wang](https://www.toptal.com/machine-learning/nlp-tutorial-text-classification), who made another linear support vector machine to classify wine reviews. He was kind enough to open source the code and explain it thoroughly, which allowed us to understand it and adapt it to our needs.
