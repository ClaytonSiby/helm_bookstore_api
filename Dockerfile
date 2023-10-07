FROM python:3.12.0

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py test && \
    python manage.py runserver 0.0.0.0:8000

EXPOSE 8000
