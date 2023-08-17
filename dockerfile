#base image
FROM python:3.11-alpine

#maintainer
LABEL Author="Nathom78"

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
#ENV PYTHONBUFFERED 1
#
##copy requirements file to image
#COPY ./requirements.txt /requirements.txt
#
##let pip install required packages
#RUN pip install -r requirements.txt






#directory to store app source code


#switch to /app directory so that everything runs from here


#copy the app code to image working directory

#create user to run the app(it is not recommended to use root)
#we create user called user with -D -> meaning no need for home directory
#RUN adduser -D user

#switch from root to user to run our app
#USER user