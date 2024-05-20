# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the FastAPI app files to the container
COPY ./app /app

# Copy the lr_model.joblib file to the container
COPY lr_model.joblib /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the port that the FastAPI app runs on
EXPOSE 8080

# Define the command to run the FastAPI app when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
