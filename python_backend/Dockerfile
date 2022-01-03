# Set base image (host OS)
FROM python:3.10.0

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY deployment/requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Get API keys
ARG forvo_api_key
ENV FORVO_API_KEY=$forvo_api_key
ARG wanikani_api_key
ENV WANIKANI_API_KEY=$wanikani_api_key

# Create .env file
RUN touch ./.env
RUN echo "FORVO_API_KEY=$FORVO_API_KEY" >> ./.env
RUN echo "WANIKANI_API_KEY=$WANIKANI_API_KEY" >> ./.env

# Generate certificates for HTTPS
# RUN openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365 -batch

# Copy the content of the local src directory to the working directory
COPY ./ .

# Specify the command to run on container start
CMD [ "python", "./app.py" ]
