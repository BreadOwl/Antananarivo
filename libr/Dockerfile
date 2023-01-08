FROM python:3.6

WORKDIR /libr

COPY requirements.txt /libr
RUN pip install -r requirements.txt
# Run app.py when the container launches
COPY . /libr
CMD python run.py
