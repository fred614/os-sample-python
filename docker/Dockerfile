FROM python:3.8

WORKDIR /home/user

COPY requirements.txt .
RUN pip install -r requirements.txt && rm requirements.txt

COPY src .

EXPOSE 8000

ENTRYPOINT ["python", "main.py"]