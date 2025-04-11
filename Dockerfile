FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 for the bot (or port 5000 depending on your setup)
EXPOSE 80

# Run the bot
CMD ["python", "bot.py"]
