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

## Running the malware
To run this, go to the Dist folder in either the encrypt or delete folder, and an executable has been compiled of the Python scripts. Upload the executable by changing the file extension to a PNG and then uploading it. Then, navigate back and go to the Elevate folder. Create a batch file with a PNG file extension. The code for the file can be found in the batch.txt, and an example is called qw.png for reference. Once done, upload that file to the server. Then, find the Elevate script and replace the batch file name with the one you just created (as a PNG). Compile it into an executable. This can be done by installing PyInstaller `pip install pyinstaller`. If you have a conda environment installed, it may ask you to remove specific packages first. After installing it, navigate to where the Python script is located and open the command prompt in that directory. Run the `pyinstaller –onefile script.py`. Change the script.py to match what you have called yours. Once done, change the file extension to a PNG and upload it to the server. Copy that name to the executable you just uploaded to the server (This will be a file path). This must be the file path that is on the server now. Go to the run page and paste the file path you just copied, and it should work.
