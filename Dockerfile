# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the backend directory contents into the container at /app/backend
COPY backend /app/backend

# Copy the frontend directory contents into the container at /app/frontend
COPY frontend /app/frontend

# Install the required packages
RUN pip install fastapi uvicorn jinja2

# Set the environment variable for Python to run in unbuffered mode
ENV PYTHONUNBUFFERED 1

# Command to run the application
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]