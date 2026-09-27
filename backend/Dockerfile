
# Use a lightweight Python image as the base
FROM python:3.9-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and the trained model
COPY main.py .
COPY superkart_model.joblib .

# Expose the port on which the Flask app will run
EXPOSE 7860

# Command to run the Flask application
CMD ["python", "main.py"]
