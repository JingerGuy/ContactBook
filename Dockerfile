FROM python:3.10.6
WORKDIR /app
COPY requirements.txt /app/
COPY data.db .
RUN pip install Flask 
RUN pip install -r requirements.txt
COPY app.py .
COPY templates/ /usr/src/app/templates/
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
