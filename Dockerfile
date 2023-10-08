FROM python:3.12.0

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN mkdir /app
COPY . /app/
WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    chmod +x ./build.sh

EXPOSE 8000
ENTRYPOINT ["sh", "./build.sh"]
