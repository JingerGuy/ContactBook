FROM python:3.10.6
WORKDIR /app
COPY requirements.txt /usr/src/app/
RUN pip install Flask 
COPY app.py .
COPY templates/ /usr/src/app/templates/
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
