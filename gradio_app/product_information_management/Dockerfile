FROM python:3.8

RUN pip install gradio>=3.36.1
RUN pip install google-cloud-aiplatform==1.25.0 google-cloud-logging
RUN pip install google-api-python-client
RUN pip install google-cloud



COPY . /app

WORKDIR /app

EXPOSE 8080

CMD ["python", "app.py"]
