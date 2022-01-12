FROM python:3.8

WORKDIR /home/code

COPY requirements.txt .
RUN pip install -r requirements.txt && rm requirements.txt

COPY *.py .
EXPOSE 8000
ENTRYPOINT ["python", "wsgi.py"]