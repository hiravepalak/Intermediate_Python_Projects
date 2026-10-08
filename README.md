# Intermediate+ Python Projects
This is a place to store all of the Python projects I made during the Intermediate+ stage of my 100 days of python challenge. 

The Intermediate+ stage includes days 32 to 40 inclusive and days 45 to 57 inclusive and follow the '100 Days of Code™: The Complete Python Pro Bootcamp' available on Udemy 

You can find posts about the previous days on my [dev.to account](https://dev.to/hirave_palak).

## Days Breakdown 
Day 32 - SMTP Monday Motivation & Birthday Wisher \
&emsp;Emails you a motivational quote every monday and automatically wishes the people you've added to the birthday list.  
&emsp;Does not send actual emails over the net due to security pains & restrictions\
&emsp;Uses the aiosmtpd module 

Day 33 - API Day 33\
&emsp;Includes a Kanye Quotes Generator and a small scipt that emails you when the ISS is visible in your sky\
&emsp;Routes emails to port 1025, so you will have to plug this cmd or a similar variant : py -m aiosmtpd -n -l localhost:1025
