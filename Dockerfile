FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Render provides PORT environment variable
EXPOSE $PORT

# Use Render's PORT environment variable
CMD uvicorn app:app --host 0.0.0.0 --port $PORT 
