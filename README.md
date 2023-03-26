# Emergency Response Network

## Prerequisites

* Python 3.7 or higher.
* Twilio 
* OpenAI API
* git -v2.13 or greater
* NodeJS
* npm - v6 or greater
* Flask

## Getting Started

To get started, a user would need to access the web app online, then submit your name, location, phone number, the date, and a description of the problem.

Once they submit their information, the description of their issue is sent to volunteers in your community using Twilio and 

The app uses Twilio to send messages to users and volunteers, meaning that help can be contacted at the push of a button.

## Description

When a user inputs their data, the data is taken from the website using Flask. The description of the user's issue is passed to categorize.py which puts the description into one of three categories using OpenAI's API. The user's data with the categorization is then stored on MongoDB. The user's problem is then sent to volunteers who can help them, and a response is sent to the user's phone with suggested resources they can access based on the category of their problem.

## Features

### Messaging Volunteers

The Emergency Response Network enables users to connect with nearby volunteers in the community to find one who can assist.

### Directly Reporting Emergencies

Users can report emergencies directly in the app, which will alert nearby volunteers to help them.

### 911 and Emergency Contact Integration

In case of dire or major emergencies, users can call 911 or their emergency contact for help.

### Real-time Communication

The app provides real-time communication between users and volunteers.

### Accessibility

The app is designed to be accessible for all users, including those with disabilities.
