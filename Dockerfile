# Start with a base image that has Python
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the repository files into the container
# If you want to clone directly within the Dockerfile (not recommended for production):
RUN apt-get update && apt-get install -y git \
    && git clone https://github.com/iShshnk/groq-llama3-rag-bot.git . \
    && rm -rf /var/lib/apt/lists/*

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set up environment variable for the API key
# Pass this as an argument when running the container
ARG GROQ_API_KEY
ENV GROQ_API_KEY=$GROQ_API_KEY

# Replace the placeholder in app.py with the environment variable value
RUN sed -i "s/your_groq_api_key_here/${GROQ_API_KEY}/g" app.py

# Expose the port that the app will run on
EXPOSE 7860

# Command to run the application
CMD ["python", "app.py"]

