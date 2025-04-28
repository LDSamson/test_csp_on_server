# listener/Dockerfile.listener

# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file (if you had one, for now just install flask directly)
# COPY requirements.txt requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Install Flask
RUN pip install Flask

# Copy the listener script into the container
COPY csp_listener.py .

# Expose the port the Flask app will run on
EXPOSE 5000

# Command to run the Flask application
# The script itself handles listening on 0.0.0.0:5000
CMD ["python", "csp_listener.py"]
