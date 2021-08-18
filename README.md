# FlightFareEstimatorProject
## Problem Statement:

<p>Travelling through flights has become an integral part of today’s lifestyle as more and more people are opting for faster travelling options. The flight ticket prices increase or decrease every now and then depending on various factors like timing of the flights, destination, and duration of flights various occasions such as vacations or festive season. Therefore, having some basic idea of the flight fares before planning the trip will surely help many people save money and time.</p>

## Approach
<p>The main goal is to predict the fares of the flights based on different factors available in the dataset.</p>
<pre> 
<li> Data Exploration     : I started exploring dataset using pandas,numpy,matplotlib and seaborn. </li>
<li> Data visualization   : Ploted graphs to get insights about dependend and independed variables. </li>
<li> Feature Engineering  :  Removed missing values and created new features as per insights.</li>
<li> Model Selection I    :  1. Tested all base models to check the base accuracy.
                             2. Also ploted residual plot to check whether a model is a good fit or not.</li>
<li> Model Selection II   :  Performed Hyperparameter tuning using gridsearchCV and randomizedSearchCV.</li>
<li> Pickle File          :  Selected model as per best accuracy and created pickle file using joblib .</li>
<li> Webpage & deployment :  Created a webform that takes all the necessary inputs from user and shows output.
                                After that I have deployed project on heroku and Microsoft Azure</li></pre>

## Deployment Links
<p> Link Heroku : https://flightfareestimatorapi1.herokuapp.com/ <br>
App Service Application URL: http://flightfareestimator.azurewebsites.net</p>

## Docker Link
link : https://hub.docker.com/repository/docker/rohanbagulwar/flight_finalapi


## UserInterface
![MainUI](https://user-images.githubusercontent.com/40850370/129313161-b74283ea-0ad7-4e7e-a196-578dc2ed49ef.png)
![DatabaseUI](https://user-images.githubusercontent.com/40850370/129313188-893dd686-5452-445d-a1ed-478ba17089c1.png)

## Technologies Used
<pre> 
1. Python 
2. Sklearn
3. Flask
4. Html
5. Css
6. Pandas, Numpy 
7. Database 
8. Hosting
9. Docker 

</pre>

## HLD , LLD & WireFrame
link : https://drive.google.com/drive/folders/1S3Ij3Sw2LRjYfrC1WaC8L6gfAg_96Dvy

## Help Me Improve
<p> Hello Reader if you find any bug please consider raising issue I will address them asap.</p>
