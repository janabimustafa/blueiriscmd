FROM python:2.7
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 80
CMD ["gunicorn", "api:app", "-b", ":80", "--reload"]