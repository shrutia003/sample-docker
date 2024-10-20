# Use lightweight Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /home/data

# Copy the Python script and the text files into the container
COPY script.py ./
COPY IF.txt ./
COPY AlwaysRememberUsThisWay.txt ./

# Install necessary dependencies (if any)
RUN pip install --no-cache-dir -r requirements.txt || true

# Run the script when the container launches
CMD ["python", "script.py"]
