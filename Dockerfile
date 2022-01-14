FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /capstoneProject3
COPY requirements.txt /capstoneProject3/
RUN pip3 install -r requirements.txt
COPY . /capstoneProject3/
