# Intermediate+ Python Projects
This is a place to store all of the Python projects I made during the Intermediate+ stage of my 100 days of python challenge. 

The Intermediate+ stage includes days 32 to 58 inclusive and follow the '100 Days of Code™: The Complete Python Pro Bootcamp' available on Udemy 

You can find posts about the previous days [here](https://dev.to/hirave_palak/day-1-of-100-1po1).

## Days Breakdown 
Day 32 - SMTP Monday Motivation & Birthday Wisher \
&emsp;Emails you a motivational quote every monday and automatically wishes the people you've added to the birthday list.  
&emsp;Does not send actual emails over the net due to security pains & restrictions

Day 33 - API Day 33\
&emsp;Includes a Kanye Quotes Generator and a small scipt that emails you when the ISS is visible in your sky\
&emsp;Routes emails to port 1025, so you will have to plug this cmd or a similar variant : py -m aiosmtpd -n -l localhost:1025

Day 34 - Trivia App\
&emsp;Basic GUI interface\
&emsp;Contains 50 questions\
&emsp;Linked to API in so you can modify the question set on the website\
&emsp;Includes some notes

Day 35 - SMS Rain Checker\
&emsp;Sends you an SMS if there is a chance of rain in your area in the next 12 hrs\
&emsp;Uses 2 free APIs: [SMS Sandbox](https://od2.in/sms-sandbox) & [weather](https://openweathermap.org/api/forecast5)\
&emsp;The phone numbers are fake\
&emsp;API key is deactiviated and was for a free trial account so just don't bother bothering it

Day 36 - Stocks & News\
&emsp;Sends you an SMS if TSLA's stocks increased/decreased by 5%\
&emsp;SMS includes the percentage change alongsdie 3 of the latest news headlines and their contents relating to that stock\
&emsp;APIs used: [Stocks](https://www.alphavantage.co/documentation/) & [News](https://newsapi.org/)
