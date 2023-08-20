# Use the Python 3.10 slim base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /code

# Copy all files from the current directory to the working directory in the container
COPY ./ .

# Define the virtual environment path
ENV VIRTUAL_ENV=/opt/venv

# Create a virtual environment
RUN python3 -m venv $VIRTUAL_ENV

# Add the virtual environment's binary path to the system PATH
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Upgrade pip inside the virtual environment
RUN pip install --upgrade pip

# Install required dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install the package from the current directory
RUN pip install .

# Use secret mounts to access sensitive data (KAGGLE_USERNAME, KAGGLE_KEY, MONGODB_CONN_STRING) & run build_model
RUN --mount=type=secret,id=KAGGLE_USERNAME \
    --mount=type=secret,id=KAGGLE_KEY \
    --mount=type=secret,id=MONGODB_CONN_STRING \
    export KAGGLE_USERNAME=$(cat /run/secrets/KAGGLE_USERNAME) && \
    export KAGGLE_KEY=$(cat /run/secrets/KAGGLE_KEY) && \
    export MONGODB_CONN_STRING=$(cat /run/secrets/MONGODB_CONN_STRING) && \
    python src/utils/build_model.py --train

# RUN python src/utils/build_model.py --train

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Start the FastAPI application using uvicorn
CMD ["uvicorn", "src.api.app:app", "--workers", "4", "--host", "0.0.0.0", "--port", "8000"]
