# Use official Python slim base
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Install system deps (optional, needed for some libs)
RUN apt-get update && apt-get install -y build-essential

# Copy dependencies file and install Python packages
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy your FastAPI app code
COPY ./src ./src

# Set working dir to src (where main.py is)
WORKDIR /app/src

# Expose API port
EXPOSE 8080

# Run the app using Hypercorn
CMD ["hypercorn", "main:app", "--bind", "0.0.0.0:8080"]
