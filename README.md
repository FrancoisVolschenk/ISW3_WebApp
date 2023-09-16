# About this repo
This is a simple django web application created for an activity in an ethical hacking course. 
The practical entails two teams, a blue team and a red team. 
The objective of the red team is to deploy malware in a system that locates and deletes or encrypts a file called target.txt on the opposition's computer
The objective of the blue team is to set up defenses on their system to prevent the red team from removing target.txt from their posession.
The blue team must also have this web application running as a point of entry for the red team.

# Running the application
## Requirements
The system must have python 3 installed as well as django
(pip install django)

## Start the server
To run this application on your localhost, simply navigate to the directory containing manage.py, open a command prompt in that directory and run `python manage.py runserver`

To run this application hosted on a local network, first find the IP address of the computer on the local network, then run `python manage.py runserver <Host's IP address>:8000`

## Accessing the web page
Once the server is running, the web application can be accessed via a browser at localhost:8000 or <IP address>:8000
