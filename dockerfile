# Make the Linux container running with Python
FROM python:3.11-alpine
# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
# prevents python buffering stdout and stderr
ENV PYTHONBUFFERED 1
# prevents Python from copying pyc files to the container
ENV PYTHONDONTWRITEBYTECODE 1
# Environement key for django and sentry
ARG SECRET_KEY
ENV SECRET_KEY ${SECRET_KEY}
ARG DSN
ENV DSN ${DSN}
# install dependencies
RUN pip install --upgrade pip
#
EXPOSE 8000
#
COPY requirements.txt .
# Don't able to cache pip for the moment
RUN pip install --no-cache-dir -r requirements.txt
# copy the app code to image working directory
COPY . .
# Run Django!!
CMD gunicorn --bind=0.0.0.0:8000 --timeout 600 oc_lettings_site.wsgi
