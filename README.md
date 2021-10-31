# text-mining

Please read the [instructions](instructions.md).

**Project Writeup and Reflection**

1. Project Overview 

# I chose to explore my favorite historical dramas to gauge the positive and negative sentiment surrounding them, counting the frequency of some keywords throughout the Wikipedia articles. Though some of my favorite TV series, Outlander, Reign, and Downton Abbey have mixed reviews due to historical innacuracy, dramatization, and sexual content. Many find the themes of historical dramas more explicit and developed than most American sitcoms and Netflix originals. In preparation for my team's final project for a foodie catalog featuring Boston restaurants and one of our brainstormed ideas of a movie review database, I decided to create a quick method to check the critical response and cultural response to these historical dramas for any potential viewers. Sentiment analysis and 

2. Implementation 

# My code utilized a for loop to repeat the function as many times as the number of Wikipedia articles. By importing libraries [MediaWiki, bs4, sys, requests, and NLTK],based on the recommendations from Stack Overflow coders, these functions converted the Wikipedia articles into text files. From this point onwards, text analysis became more manageable as lists and dictionaries were elements recently learned. The exercises went over in class of converting data types assisted in the process of using lists to structure the Wikipedia pages, Wikipedia page URLs, negative words, and positive words. Dictionaries compiled the words extracted from the texts, and for loops and if statements were logically written towards the end of the analyze_dramas() function to print the word and its frequency count.

# Using mediawiki allowed me to quickly pull data from the MediaWiki site of choice instead of dealing directly with the API, and many developers on Reddit and Stack Overflow utilized this python wrapper and parser for the MediaWiki API instead of using multiple API’s and JSON files. 

# I considered running summary statistics and computing the similarity of the three texts, yet I did not find this as relevant as sentiment analysis and word frequency count. 

3. Results 

# As I am having some issues in running my code, I am unable to fully examine my results with sentiment analysis. However, I was able to run parts of my word frequency code. See charts in the Assignment 2 images file for the frequency of "inaccurate" and "success". I found that the number of mentions of a word is not enough to gauge the tone and public opinion of a show, which is where sentiment analysis contributes to the text analysis. Finding the top 10 words from an article, word count, or text similarity is often inaccurate without context. For example, in the Wikipedia pages, much of the content is a summery of the plot and characters. How can the tone and sentiment be determined of the TV series itself and the public opinion of the TV series when the dramatic plot is being described.

# {'neg': 0.026, 'neu': 0.931, 'pos': 0.044, 'compound': 0.8201}
# Sentiment Analysis of Downton Abbey Wiki Page 

# The Mitsubishi Outlander is printed in the results and output of my code, as well as the background of the word "reign" instead of the TV series Reign. It would be interesting to debug this error, and I have already begun to look at the code to test where this miscommunication occured.

4. Reflection 

# I decided early in the process that I wanted to incorporate media in my code, whether in the form of Project Gutenberg novels (ex_ Anne of Green Gables), IMDB pages, or Wikipedia articles. I knew the elements I needed to incorporate to perform the sentiment analysis and word frequency test, including the lists, dictionaries, for loops, and if statements; I planned my code logically with pseudo-code when first receiving the assignment instructions, utilizing online resources such as GitHub, w3schools, and Stack Overflow. I pieced together code that made sense to me based on our class demo code and homework exercises, however, I did not foresee the issues I had running the code. Once I realized the issues with the imports, I decided to look more deeply into each import name (mediawiki, bs4, requests) to debug  my code, finding the installation protocols for each. I was able to partially debug this error, as shown in the terminal when running the code. In the future, I plan to test more frequently with more print statements and in phases; writing and running a bigger block of code before testing parts of it leads to errors later in the process, which I found to be true in my case. While I have improved at logically thinking through the given problem to solve with pseudo-code and tying elements we have learned together, I hope to practice running code in iterations to ensure success rather than hope for success at the end. I wish I was more knowledgeable about Python libraries to better utilize any relevant tools as a shortcut; more extensive research and experience will omly further this goal of mine.