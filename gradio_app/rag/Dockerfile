FROM python:3.11-slim

# Allow statements and log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED True

# Install required system packages (including GLib)
RUN apt-get update \
    && apt-get install -y libgl1-mesa-glx libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt /app/requirements.txt

# Install your project dependencies, including Gunicorn
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application code
COPY . /app

# Set the working directory
WORKDIR /app

# Expose the port that Gunicorn will run on
EXPOSE 8080

# Command to run Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]
