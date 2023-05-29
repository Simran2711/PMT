# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code to the container
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]
