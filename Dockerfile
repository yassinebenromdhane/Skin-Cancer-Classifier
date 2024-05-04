# Stage 1: Build the application
FROM python:3.10 as build

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Run the application
FROM python:3.10-slim as runtime

# Set the working directory inside the container
WORKDIR /app

# Copy the Python dependencies from the build stage
COPY --from=build /app /app

# Expose the port the app runs on
EXPOSE 5000

# Set the entry point for the container
CMD ["python", "app.py"]