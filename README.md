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

# Exploiting the vulnerabilities (Spoilers ahead!!!)
## Finding a way in
When the server is running, you can try a URL enumeration tool such as GoBuster to see which other URLs are available on the running server. Another approach is to try to access a URL on the server that does not exist. Because the server has been left in debug mode, an error message will appear with a list of all of the available paths. Many of these URLs lead to a bogus page that displays a random message. However, `/run` is a valid path, but requires a POST request to work correctly.

## Uploading the malware
The server is set to only allow images to be uploaded. This can be verified by trying to upload an executable or other file. This mechanism is easily bypassed by changing the extension of a file to `.png`. Once the malware has been uploaded to the server, you can navigate to the page that lists all of the files that have been uploaded. The server has intentionally been set to display the full path of the file instead of just the file name. 

## Running the malware
The vulnerability in this section has been intentionally introduced. Please note that in a real-life scenario, a server is unlikely (or at least it should be unlikely) to accept a filename from user input and try to open that file as an executable. With the full path of where the file has been saved on the server, and knowledge of the run URL, the hacker should now see a clear way forward. However, there is one last hurdle: even with the lowest possible security configuration for the django server, any form that is created requires a CSRF token. Fortunately for the hacker, this token is accesible via a hidden `input` element on the home page. To make the attacker's job easier, they can alter the HTML of the upload form on the home page. Remove the `enctype` attribute from the form, add an attribute to change the POST location: `action="run"` and remove the `file` input. Lastly, paste the full path of the executable that has been uploaded to the server in to the `flName` field and submit the form. If done correctly, this should run the uploaded malware on the server. 

## Getting Feedback
The server will simply return a message that states that an executable has been run. If the attacker wishes to get confirmation that their malware has run successfully, they need to build in a mechanism that reports back to a server or sends an email or something along those lines. This does however increase the chances of being detected, or being traced after the fact.

# The Malware
A sample of the functional malware has been added to this repo. *Please take note that this code is meant to search for a file with a specified name and encrypt or delete it*. The owner of this repo and the author of the malware scripts take no responsibility for any loss of data or corrupted systems that result from the use of these scripts. They are for educational purposes only and should be used with caution.

## Running the malware
To run this, go to the Dist folder in either the encrypt or delete folder, and an executable has been compiled of the Python scripts. Upload the executable by changing the file extension to a PNG and then uploading it. Then, navigate back and go to the Elevate folder. Create a batch file with a PNG file extension. The code for the file can be found in the batch.txt, and an example is called qw.png for reference. Once done, upload that file to the server. Then, find the Elevate script and replace the batch file name with the one you just created (as a PNG). Compile it into an executable. This can be done by installing PyInstaller `pip install pyinstaller`. If you have a conda environment installed, it may ask you to remove specific packages first. After installing it, navigate to where the Python script is located and open the command prompt in that directory. Run the `pyinstaller –onefile script.py`. Change the script.py to match what you have called yours. Once done, change the file extension to a PNG and upload it to the server. Copy that name to the executable you just uploaded to the server (This will be a file path). This must be the file path that is on the server now. Go to the run page and paste the file path you just copied, and it should work.
