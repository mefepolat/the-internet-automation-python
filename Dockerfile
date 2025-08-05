# Use an official Python image as base
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg \
    chromium-driver \
    chromium \
    && apt-get clean

# Set environment variables to use Chrome in headless mode
ENV CHROME_BIN=/usr/bin/chromium
ENV PATH="$PATH:/usr/lib/chromium/"

# Create working directory
WORKDIR /app

# Copy project files into the container
COPY . /app
COPY test_data /app/test_data

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run pytest and generate the HTML report
CMD ["pytest", "--html=reports/report.html", "--self-contained-html"]
