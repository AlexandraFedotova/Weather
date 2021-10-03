<<<<<<< HEAD
#Dockerfile
FROM python:3.9.7
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .
ENV API_KEY="${API_KEY}"
CMD python main.py
EXPOSE 8000
=======
#Dockerfile
FROM python
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONPATH /app
ENV PATH=$PATH:/app
CMD python main.py
EXPOSE 8080
>>>>>>> origin/master
