
FROM python:3.12


WORKDIR /app


COPY ./configuration/requirements.txt requirements.txt


RUN pip install --no-cache-dir --upgrade -r requirements.txt


COPY . .


CMD ["fastapi", "run", "server.py", "--port", "8000"]

