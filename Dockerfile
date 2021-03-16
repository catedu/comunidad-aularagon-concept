# Pull base image
FROM python:3.8

# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

RUN jupyter notebook --generate-config
RUN sed -i 's/# c.NotebookApp.allow_root = False/c.NotebookApp.allow_root = True/' /root/.jupyter/jupyter_notebook_config.py

# Copy project
COPY . /code/