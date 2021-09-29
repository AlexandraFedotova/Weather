#Dockerfile
FROM python

COPY main.py main.py
COPY api_key.txt api_key.txt

RUN pip install Flask==2.0.1
RUN pip install numpy==1.21.2
RUN pip install requests==2.26.0
RUN pip install geopy==2.2.0

EXPOSE 8080

CMD ["python", "/main.py"]