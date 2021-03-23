# Pull base image
FROM python:3.8

# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

# Set work directory
WORKDIR /code

COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["bash", "docker-entrypoint.sh"]

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# RUN jupyter notebook --generate-config
# RUN sed -i 's/# c.NotebookApp.allow_root = False/c.NotebookApp.allow_root = True/' /root/.jupyter/jupyter_notebook_config.py

# Copy project
COPY . .