FROM python:3.7
WORKDIR /app
RUN pip install Flask
RUN pip install flask_sqlalchemy, pymysql, render_template, request, redirect, url_for, flash 
COPY app.py .
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
