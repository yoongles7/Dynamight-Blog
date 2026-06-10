# Python base image
FROM python:3.12-slim-bookworm

# App directory
WORKDIR /Dynamight-Blog

# Install system dependencies
RUN apt-get update && apt-get install -y netcat-openbsd

# Copy and install project dependencies
COPY requirements/ /Dynamight-Blog/requirements
RUN pip install -r requirements/development.txt

# Copy app code into the container
COPY . .

# Set Port environment variable
ENV PORT=8000
# Expose the port to the computer to access it
EXPOSE 8000

# Run entrypoint.sh
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

# Run the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=config.settings.development"]