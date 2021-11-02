# Neighbourhood

## Project by:
Halima Yahya 
Email: halima.yahya@student.moringaschool.com

## Description
This is a web app that allows you to be in the loop about everything happening in your neighbourhood. From contact information of different handyman to meeting announcements or even alerts.

## User Story  
  
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## Setup and Installation  
To get the project .......  

```bash
git clone
https://github.com/halima254/neighbourhood
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Neighbourhood
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations hood
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
## Technologies used
* Python 3.8
* postgresql
* HTML
* Botstrap


## License
https://opensource.org/licenses/MIT

* Copyright (c) 2021 **Halima Yahya**