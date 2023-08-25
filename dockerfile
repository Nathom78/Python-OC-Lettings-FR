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

# upgrade pip &&
RUN pip install --upgrade pip
#
EXPOSE 8000
#
COPY requirements.txt .
RUN pip install -r requirements.txt
# copy the app code to image working directory
COPY . .
#
CMD python manage.py collectstatic
#
CMD python manage.py runserver && gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000

#switch to /app directory so that everything runs from here



#create user to run the app(it is not recommended to use root)
#we create user called user with -D -> meaning no need for home directory
#RUN adduser -D user
#switch from root to user to run our app
#USER user