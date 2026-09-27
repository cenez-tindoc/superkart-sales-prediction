FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install git and git-lfs for cloning private repos or large files
RUN apt-get update && apt-get install -y git git-lfs && rm -rf /var/lib/apt/lists/*

# Install Hugging Face Hub library for downloading models
RUN pip install --no-cache-dir huggingface_hub

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Hugging Face
# IMPORTANT: Replace <your-hf-username> with your actual Hugging Face username
# and <your-hf-repo-name> with the name of the model repo on HF (e.g., superkart-model)
# You might need to pass HF_TOKEN as a build-arg or environment variable if your repo is private
ENV HF_USERNAME="cenez-tindoc" # Replace with your Hugging Face username
ENV HF_REPO_NAME="superkart-model" # Replace with your Hugging Face model repo name

# Download the model from Hugging Face Hub
# This assumes the model is public or HF_TOKEN is set as an environment variable in Codespaces
RUN python -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id=f'{os.environ.get("HF_USERNAME")}/{os.environ.get("HF_REPO_NAME")}', filename='superkart_model.joblib', local_dir='./')"

# Copy the application code
COPY . .

# Define the command to start the application using Gunicorn with 4 worker processes
# - `-w 4`: Uses 4 worker processes for handling requests
# - `-b 0.0.0.0:7860`: Binds the server to port 7860 on all network interfaces
# - `app:superkart_api`: Runs the Flask app (assuming `app.py` contains the Flask instance named `superkart_api`)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:7860", "app:superkart_api"]
