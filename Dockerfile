FROM python:3.10

EXPOSE 5000/tcp

WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
CMD ["python","app.py"]