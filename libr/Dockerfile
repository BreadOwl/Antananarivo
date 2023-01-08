FROM python:3.6

WORKDIR /libr

COPY requirements.txt /libr
RUN python -m pip install --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt
#RUN pip install -r requirements.txt
# Run app.py when the container launches
COPY . /libr
CMD python run.py
