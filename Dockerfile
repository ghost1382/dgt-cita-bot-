FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE port 80 for the bot or web server
EXPOSE 80  # or 5000, depending on your configuration

# Run the bot
CMD ["python", "main.py"]
