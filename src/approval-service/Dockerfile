FROM python:3.10-slim

WORKDIR /app

COPY ./src /app

RUN pip install --upgrade flask werkzeug
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:6000", "app:app"]
