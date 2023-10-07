# syntax=docker/dockerfile:1

FROM python:3.12.0
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /app
COPY . /app/
WORKDIR /app
RUN set -e; \
    /usr/local/bin/python -m pip install --upgrade pip ;\
    python -m pip install -r ./requirements.txt ;\
    chmod +x ./entrypoint.sh ;

EXPOSE 8000
ENTRYPOINT ["./entrypoint.sh"]
