FROM pmoneda/azure-functions-python-opencv:v1.0
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get install -y \
	tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
