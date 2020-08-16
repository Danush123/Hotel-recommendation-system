from flask import Flask, redirect, url_for, request 
import numpy as np
import csv
from nltk.corpus import movie_reviews
from textblob import classifiers
from textblob import TextBlob

app = Flask(__name__) 

print('hello') 



@app.route('/rev', methods=["GET", "POST"]) 

    
 
 
def rev():

    
 
	comment1 = request.form['comment']
	
	rating = request.form['rate']
	
	hotel_name = request.form['hotel']
	
	print(comment1) 
	
	print(rating)
	
	print(hotel_name)
	
	blob = TextBlob(comment1)
	

	
	if blob.sentiment.polarity < 0:
	
		ans =  "Negative Response Recorded"
		sent = "negative"
		
	elif blob.sentiment.polarity > 0:
	
		ans = "Positive Response Recorded"
		sent="positive"
	else:
	
		ans =  "Neutral Response Recorded"
		sent = "neutral"
	
	return '{}<html><body><br><br><a href = "http://localhost:8080/index.html">Home</a></body></html>'.format(ans)		
		
		
		
		
		
		
		
		
	
if __name__ == '__main__': 
   app.run(debug = True) 