# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory to the container's working directory
COPY . .

# Install the necessary Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port (not really necessary for this bot but a common practice)
EXPOSE 8080

# Command to run the bot
CMD ["python", "bot.py"]
