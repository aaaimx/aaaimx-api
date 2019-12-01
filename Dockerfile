FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /aaaimx
WORKDIR /aaaimx
COPY requirements.txt /aaaimx/
RUN pip install -r requirements.txt
COPY . /aaaimx/