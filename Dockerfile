FROM duruo850/ubuntu18.04-python3.6

ENV PYTHONBUFFERED 1
RUN mkdir /code

RUN apt-get update && apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv

RUN apt-get update && apt-get install -y libmysqlclient-dev
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD ./bookmyshow_project /code/
EXPOSE 8000 8001
#CMD ["/code/entrypoint_script.sh"]

#CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000" ]
