# Use a Python-specific slim image for a lightweight base
FROM python:3.8-slim-buster

# Set environment variables to avoid prompts during installation
ENV DEBIAN_FRONTEND=noninteractive
  
# Copy only the requirements file first to leverage Docker caching
COPY requirements.txt /app/requirements.txt

# Install system dependencies and Python requirements
RUN apt update -y && \
    apt install -y --no-install-recommends awscli build-essential gcc && \
    pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application code
COPY . /app

# Set the working directory
WORKDIR /app

# Default command to run the application
CMD ["python3", "app.py"]
