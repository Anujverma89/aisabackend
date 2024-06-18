# Aisa Backend 

### Steps to run this app 

#### Installation
* Install Python in your machine
* Create virtal ENV
    * python -m venv env_name  
* activate Env :  
  * Windows : ./pathtoenv/Scripts/activate.bat  
  * Unix based : source pathToEnv/bin/activate
* Install all the dependencies
    * Run the below command
    * pip install req.txt
* Clone the project in local machine 
    * git clone https://github.com/Anujverma89/aisabackend.git


#### Run the project 
* python manage.py runserver
* open browser 
* hit the given url in your browser 
    * http://localhost:8000
* you can hit given below apis :
    * GET :   
        * http://localhost:8000/api/notices
        * http://localhost:8000/api/members
        * http://localhost:8000/api/getfaqs
        * http://localhost:8000/api/getevents
        * http://localhost:8000/api/getblogs
    * POST : 
        * http://localhost:8000/api/feedback
        * http://localhost:8000/api/joinaisa