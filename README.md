# Quantitative Analysis of Sexually Explicit Lyrics in Female Rap Music

by Parth Wokhlu and Mihir Nakra 

Parth Wokhlu: parth.wokhlu.843@gmail.com

Mihir Nakra: nakramihir@gmail.com

# I. Introduction

After spending the past year delving into rap music as a whole, the wide variety of topics/subjects discussed became extremely intriguing to us. Specifically, with the rise of rappers like Megan Thee Stallion and Cardi B, we noticed that there was a general stereotype that female rappers only rapped about sexually explicit material like intercourse and their own bodies. Thus, we decided to use ML to find whether or not this consensus was legitimate.

# II. Methodology
All the code for this project is open sourced (not all of it is written completely by us, so please give the original authors their due credit). 

## Data Collection
The first step was collecting a list of female rappers. To do this, we combined 2 comprehensive lists of female rappers, one from [Wikipedia](https://en.wikipedia.org/wiki/Category:American_female_rappers) and one from [Genius](https://genius.com/Genius-users-list-of-female-rappers-annotated). After collecting a list of about 310 female rappers, we used [Fran Gonzalez’s Itunes API](https://github.com/sleepyfran/itunespy) to get full tracklists for each artist, and then with those lists, we compiled all the song lyrics together using  [John Miller’s Genius API](https://github.com/johnwmillr/LyricsGenius). Once we had the lyrics for each of those artists, we needed to compile training data for the model to be able to predict if a song was sexually explicit. Our training data consisted of 50 songs that we knew contained sexually explicit themes and 50 songs that we knew did not. We then split up the list into 3 different training sets, which can be found under the “data/” directory. 

## Neural Network
At first, the idea of a neural network seemed like a far off possibility. It seemed interesting, but neither of us had any idea what it actually was. As we delved into the topic, we found numerous [YouTube videos](https://www.youtube.com/watch?v=aircAruvnKk&feature=youtu.be) and [articles](https://news.codecademy.com/taylor-swift-lyrics-machine-learning/) that allowed us to wrap our heads around this topic. 

From what we understood, the method we should attack this problem with was to classify a song based on the lyrics using a linear support vector machine. This method had a fast computational time and could provide accurate results without thousands and thousands of training inputs. Essentially, a linear support vector machine is made to mathematically determine a hyperplane which will allow it to classify data points. A hyperplane is, to put it simply, a line of best fit for the data with a margin outside of it. The calculations done by the machine create a hyperplane with the largest margin possible so that data can be classified as accurately as possible. 

So now we have the hard part: how do we turn words into data points for the machine to use? The method we used was implementing a count vectorizer, which creates a matrix using the words given. An example of this is below:

![Example of count vectorizer matrix](https://kavita-ganesan.com/wp-content/uploads/how-hashingvectorizer-works.png)

From the matrix, we used something called a tfidf transformer to allow the machine to get a better understanding of what words matter. A tfidf transformer highlights the words that are unique to certain songs and helps to reduce the influence of a word like “the,” which appears likely in all songs numerous times. After applying these calculations to our text, we gave the training data to the model and allowed it to determine the hyperplane. To do all of this, we used the python sklearn library.

To determine the accuracy of our training data, we split it up so that 70% of it would be used to train and then 30% of it would be used to test. We would then train the model with that 70% and tell it to predict the themes of the song of the remaining 30% of the songs. Then we would compare the data it predicted to what we know it should’ve predicted. We tested it many times, and it had an average accuracy of about 85%. 

After determining our model was fairly accurate, we could use it to predict the themes of all the songs we had. Each time we wanted to predict if a song contained sexually explicit themes in it, we could give that model the count vectorized and tfidf transformed song lyric, and using the already determined hyperplane, it would identify where the song lyrics would lie on the graph in relation to the hyperplane. Based on that it would tell us if a certain song contained the ideas of racial injustice or not. This type of machine learning that we are using is called supervised learning, in which the program is given prior knowledge of what kinds of things it should categorize into each section.

The credit for providing us with the design of this model goes to [Shanglun Wang](https://www.toptal.com/machine-learning/nlp-tutorial-text-classification), who made another linear support vector machine to classify wine reviews. He was kind enough to open source the code and explain it thoroughly, which allowed us to understand it and adapt it to our needs.

## Implementing the Code
Now that we had an accurate model and the required testing and training data, the rest of the code was pretty simple. Once we trained the model on the given data, it was time to run it through the nearly 2,400 songs we had compiled. The full syntax for the class we wrote can be found under the title of “mainSVC.py” in the repository
From there, the process was standard. We created a for loop to go through each artist’s song lyrics and identify how many of them contained sexually explicit themes. At the end of processing the songs for the respective artist, the program calculated the percentage of songs from that artist that were sexually explicit and saved them to a text file. This cycle repeated until we had quantified the content of all the songs made by all the female rappers that we identified. We ran that program 3 times, once for each training set that we made.

## Limitations/Flaws
1. We’re high schoolers, there’s bound to be mistakes within our data analysis.
2. The definition of “sexually explicit” for most of the population is quite similar, but some people may classify mere references as such, so the training data is relatively subjective.
3. We didn’t want our own knowledge of rappers to influence the list and thus the overall data, so we used the Wikipedia and Genius list of female rappers to scan through. These were the most objective lists of artists possible because they were made through multiple different contributors.

# III. Results
Compiling the average of three trials, 28.01% of rap songs written by female artists were found as sexually explicit in nature. We found that the amount of these types of songs varied drastically artist-to-artist, and can be visualized in the scatterplot below.

<p align="center">
  <img src="https://github.com/parth-wokhlu/Quantitative-Analysis-of-Sexually-Explicit-Lyrics-in-Female-Rap-Music/blob/main/femrapGraph.PNG">
</p>

We’ve open sourced the excel sheet with the full data above titled “Rap Analysis Results.” Overall, it’s clear that a large majority of female rap songs don’t discuss themes of nudity and sex. We aren’t comparing it to the percentage of men’s rap about sexually explicit music because the hypothesis we are testing is whether or not a majority of women rappers 

# IV. Conclusion and Implications
Utilizing a natural language processing neural network model, we conclude that, in contrast to popular belief, sexually explicit themes are not the main focus of rap music made by women. 

This has two key implications. First, it means that the general population will characterize women as “sexualizing/objectifying” themselves given any chance to do so. A majority of people have probably resorted to this stereotype that “women rappers only talk about sex” to feed their preconceived notions without having to actually explore an artist's discography. This is most likely rooted in society’s inherently patriarchal structure, but should be more researched. 

The second implication of this study is that the consumption of women’s rap music tends to be the songs centered around sexually explicit themes. Labels (and artists) most likely push and advertise these songs the most as they are more likely to go viral/become popular. This could be due to their attention-grabbing explicit lyrics and/or a result of the first implication of enforcing sexist stereotypes.

However, this does not mean that women should not make music about sex or their bodies or that making said music is bad. Indeed, several [articles](https://thehoya.com/women-in-hip-hop-navigate-objectification-owning-their-sexual-power/) and studies have discussed self-sexualization in rap music as a way to combat hyper-masculinity and demonstrate self love in the face of the unfair beauty standards women of color often have to live up to. This report was simply meant to see the extent of validity a certain stereotype had and in no way was meant to say that music about sex is an excuse to be blatantly mysognist. 

Overall, we encourage anyone who believes that women “only rap about sex” to truly explore their catalogs and to stop characterizing a whole genre of music off of a minority of songs. 
