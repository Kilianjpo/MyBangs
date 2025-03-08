FROM python:3.13-alpine

WORKDIR /app

COPY . /app
WORKDIR /app

RUN pip install .

EXPOSE 8000
CMD ["python", "-m", "gunicorn", "-w", "4", "-b", "0.0.0.0", "mybangs:create_app()"]