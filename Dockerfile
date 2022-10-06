FROM python:3.10.6
WORKDIR .
COPY requirements.txt .
COPY data.db .
RUN pip install Flask 
RUN pip install -r requirements.txt
COPY app.py .
COPY templates/ /templates/
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
