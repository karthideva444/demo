FROM python:3.12.0

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN mkdir /demo_crud/

WORKDIR /demo_crud

RUN pip install --upgrade pip

COPY requirements.txt /demo_crud/

RUN pip install -r requirements.txt

COPY . /demo_crud/

CMD ./manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000