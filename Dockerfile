FROM python:3.10.6
WORKDIR /app
COPY requirements.txt .
COPY . .
RUN pip install Flask 
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
