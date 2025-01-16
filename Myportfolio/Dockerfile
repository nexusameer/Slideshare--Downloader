# Use an official Python runtime as a parent image
FROM python:3.12.2-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies if needed (e.g., for Postgres or other libraries)
# RUN apt-get update && apt-get install -y <some_package>

# Install Python dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files for production use (optional if you need static assets served)
RUN python manage.py collectstatic --noinput

# Expose port 8000 for Django to run
EXPOSE 8000

# Install Gunicorn for production server
RUN pip install gunicorn

# Command to run the Django app with Gunicorn
# CMD ["gunicorn", "Myportfolio.wsgi:application", "--bind", "0.0.0.0:8000"]
CMD ["gunicorn", "Myportfolio.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120"]


