FROM postgres:latest

ENV POSTGRES_PASSWORD=password
ENV POSTGRES_USER=myuser
ENV POSTGRES_DB=mydatabase

COPY init_db.sql /docker-entrypoint-initdb.d/
