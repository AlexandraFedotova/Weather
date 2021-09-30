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
