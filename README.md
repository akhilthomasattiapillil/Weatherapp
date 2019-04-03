# Weatherapp
REST API using Python,Flask,Dnamic UI with HTML,AJAX,Jquery,Dictionary operations.Docker also provided.

# Rest API
 Rest API with get,post,update,delete methods.
 
 # weatherforecast_ui
Dynamic Weatherforecast service for 7 days with flask,html,python,ajax and jquery

## install
requirements.txt to install flask and flask_restful

## RUN

download the dailyweather.csv file and save in the same directory as the python file - weatherapp.py 

#### 1 open terminal and run the python file "weatherapp.py". 
#### 2 copy the link in the browser, if running from local host or use the ec2 public-dns if running from instance. append ":5000/historical" at the end of url
#### 3 for get method to obtain the whole date information , include :5000/historical" at the end of url
#### 4 for get method to obtain the weather information of particular date at the end of url , include :5000/historical/"date"
#### 5 for post method to delete the weather information of particular date at the end of url , include :5000/historical/"date"
#### 5 for post method to update the weather information of particular date at the end of url , include :5000/historical/"date"

## RUN weatherapp_UI (User Interface)

download the dailyweather.csv file and save in the same directory as the python file - weatherapp.py
place the index.html file in the templates folder which is in the same directory as python file- weatherapp.

#### 1 open terminal and run the python file "weatherapp.py". 
#### 2 copy the link in the browser, if running from local host or use the ec2 public-dns if running from instance. append ":5000/ui" at the end of url
#### 3 enter the date in textbox and click the submit button.
### the UI will display the forecast from a predetermined function.


# DOCKER of the Weatherapp


### Project Checkpoints
- Dockerizing the REST API and the dynamic UI built and hosted on Amazon_EC2.

### Step 1: Installation 
- sudo yum update -y
- sudo yum install -y docker
- sudo service docker start
- sudo usermod -a -G docker ec2-user
- docker login -u akhilthomasattiapillil
- docker pull python:3.5

### Step 2: Requirements.txt 

- It has all the libraries used for the project -flask, flask_restplus, flask_api. 


### Step 3: Creating Docker File

- Used a base image : Python
- Provided my requirements.txt
- CMD for running the python file.

### Step 4: Build Docker Image

- docker build -t <Image_name> .

### Step 5: Run Docker Image

- docker run -d --name Container_Name 80:5000 Image_name

### Step 6: Tag Docker Image

- docker tag Image_ID yourhubusername/Imagename

### Step 7: Push Docker Image

- docker push yourhubusername/Image_name






## License

MIT License

Copyright (c) [2019] [Akhil Thomas]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


