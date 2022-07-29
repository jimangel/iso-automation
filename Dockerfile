FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt iso.py ./
RUN pip3 install -r requirements.txt
CMD [ "python3", "iso.py"]