# Base image 
FROM python:3.6

# Author
MAINTAINER kanavis

# App
ADD ./heart_rater /var/lib/heart_rater
WORKDIR /var/lib/heart_rater/

# Scenario 
# Pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Django
RUN python manage.py collectstatic --noinput

# Execute
CMD exec uwsgi --uid www-data --gid www-data --chmod-socket=660 --chown-socket www-data:www-data --socket /var/sock/uwsgi/heart_rater/uwsgi.sock --module heart_rater.wsgi --logto /var/log/uwsgi/heart_rater/uwsgi.log
