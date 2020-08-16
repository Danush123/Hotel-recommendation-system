
from flask import Flask, redirect, url_for, request 
import numpy as np
import csv
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
	
app = Flask(__name__) 
 
@app.route('/predict', methods=["GET", "POST"]) 
def predict():
    area = request.form['area']
    price = int(request.form['price'])
    guest_recommendation = int(request.form['guest_recommendation'])
    hotel_star_rating = int(request.form['hotel_star_rating'])
    positive_reviews = int(request.form['positive_reviews'])
    critical_reviews = int(request.form['critical_reviews'])
    room_area = int(request.form['room_area'])
    room_count = int(request.form['room_count'])
    site_review_rating = float(request.form['site_review_rating'])
    service_quality = int(request.form['service_quality'])
    amenities = int(request.form['amenities'])
    food_and_drinks = int(request.form['food_and_drinks'])
    value_for_money = int(request.form['value_for_money'])
    location_rating = int(request.form['location_rating'])
    cleanliness = int(request.form['cleanliness'])


    fil = 'D:\\CIP\\areas\\'
    fil = fil+area+'.csv'
    names = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
    dataset = pd.read_csv(fil, names=names)
    x = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 14].values
    scaler = StandardScaler()
    scaler.fit(x)

    x = scaler.transform(x)
	
    classifier = KNeighborsClassifier(n_neighbors=1)
    classifier.fit(x, y)

    x_t = [[price, guest_recommendation, hotel_star_rating, positive_reviews, critical_reviews, room_area, room_count, site_review_rating, service_quality, amenities, food_and_drinks, value_for_money, location_rating, cleanliness]]

    x_t = scaler.transform(x_t)

    y_pred = classifier.predict(x_t)

    with open(fil, 'r') as inp, open('D:\\CIP\\star.csv', 'w') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[2] == str(hotel_star_rating):
                writer.writerow(row)
    fil = 'D:\\CIP\\star.csv'
    names = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
    dataset = pd.read_csv(fil, names=names)
    x = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 14].values
    scaler = StandardScaler()
    scaler.fit(x)

    x = scaler.transform(x)
	
    classifier = KNeighborsClassifier(n_neighbors=1)
    classifier.fit(x, y)

    x_t = [[price, guest_recommendation, hotel_star_rating, positive_reviews, critical_reviews, room_area, room_count, site_review_rating, service_quality, amenities, food_and_drinks, value_for_money, location_rating, cleanliness]]

    x_t = scaler.transform(x_t)

    y_star = classifier.predict(x_t)
 
    fil = 'D:\\CIP\\areas\\'
    fil = fil+area+'.csv'

    with open(fil, 'r') as inp, open('D:\\CIP\\edit1.csv', 'w') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[14] != str(y_pred[0]):
                writer.writerow(row)
    
    fil = 'D:\\CIP\\edit1.csv'
    names = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
    dataset = pd.read_csv(fil, names=names)
    x = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 14].values
    scaler = StandardScaler()
    scaler.fit(x)

    x = scaler.transform(x)
	
    classifier = KNeighborsClassifier(n_neighbors=1)
    classifier.fit(x, y)

    x_t = [[price, guest_recommendation, hotel_star_rating, positive_reviews, critical_reviews, room_area, room_count, site_review_rating, service_quality, amenities, food_and_drinks, value_for_money, location_rating, cleanliness]]

    x_t = scaler.transform(x_t)

    y_pred1 = classifier.predict(x_t)


    #return  '{} {} {}'.format(y_star,y_pred,y_pred1)
    return '<html><body> <b><u>Recommendation based on star rating:</u></b><br>{}<br><br><br><b><u>Recommended hotels:</u></b><br>1. {}<br>2. {}<br><br><a href = "http://localhost:8080/booking/booking.html"><input type = "button" name = "Book now" value = "Book now"></a> </body></html>'.format(y_star,y_pred,y_pred1)
  
if __name__ == '__main__': 
   app.run(debug = True,port=5000) 



