FROM python:3.10-slim

WORKDIR /app

COPY ./backend /app

RUN pip install --upgrade flask werkzeug
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app"]
