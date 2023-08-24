# escape=`

#base image

FROM python:3.11-alpine

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONBUFFERED 1
ARG SECRET_KEY
ENV SECRET_KEY ${SECRET_KEY}
ARG DSN
ENV DSN ${DSN}

#
##copy requirements file to image
#COPY ./requirements.txt /requirements.txt
#COPY ./code *.*
#
##let pip install required packages
EXPOSE 8000
COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . .
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]

RUN python manage.py






#directory to store app source code


#switch to /app directory so that everything runs from here


#copy the app code to image working directory

#create user to run the app(it is not recommended to use root)
#we create user called user with -D -> meaning no need for home directory
#RUN adduser -D user

#switch from root to user to run our app
#USER user