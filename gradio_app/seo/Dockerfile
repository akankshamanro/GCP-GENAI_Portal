FROM python:3.8

RUN pip install gradio>=3.36.1
RUN pip install openai

COPY . /app

WORKDIR /app

EXPOSE 8080

CMD ["python", "app.py"]
