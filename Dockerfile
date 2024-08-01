FROM python:3.8-slim-buster

# Install dependencies that require network access
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY wheels /wheels

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY src/app /app
WORKDIR /app

# Copy utilities
COPY src/utilities /app/utilities

# Expose the port Streamlit will run on
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "robotapp.py"]