# Doorman
An emotional analysis kiosk to make school guidance counseling more effective 

## Inspiration:
We see a lot of people in school who are often very sad or mentally troubled. They go through their school career hopelessly looking for someone to reach out to. Guidance counselors are currently overworked and cannot possibly cater to every student's needs. In fact, counselors outnumber students 491 to 1. We were inspired to help guidance counselors monitor the mental health of students
## What it does:

We decided to use machine learning with emotion analysis to track the mental health of students in a school. Therefore, advisors can view all the student's data in an intuitive format. It analyzes emotions via speech and image in order to approximate someone's mental state. It then graphically puts the data onto a web server.
## How does it do it:
A windows computer ran an emotional analysis and communication software within a Flask framework in order to analyze a user's emotions, and then display analytics on a webpage. An Arduino was used to swipe an RFID card which would be used to catalog students. The Kairos API was used for image analysis, and IBM Watson was used for speech analysis. A temperature sensor was used to gather environmental information, as to have a conversational topic to interact with a student (i.e. "Weird weather we've been having lately")
## Challenges we ran into:

Getting Flask to work in the first place, using webcam to import pictures to python, saving to the correct directories, faulty wires and Arduino, general instability, Python version inconsistency (i.e. 3 v. 2.7 or 32 vs 64 bit), displaying analytics in flask, and speech analysis.
## Accomplishments we are proud of:

Getting everything to work together in tandem. There were a lot of challenges in this department, so we are very happy that we are able to get it to work in the end.
## What we learned:

How hard it is to pursue such ambitious projects in 24 hours. We learned that nothing works the first time, and we always need to persevere to reach a goal.
## What's next for DoorMan:

Currently accessing all the APIs take a lot of time. We would like to streamline the process to make the products faster and more efficient. Also, to incorporate numerous students, we would use databases.
## Built With

* flask
* python
* arduino
* ibm-watson
* rfid
* pygame
* json
* google-web-speech-api
* kairos

