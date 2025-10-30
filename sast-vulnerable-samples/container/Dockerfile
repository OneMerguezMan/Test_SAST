# Insecure Dockerfile for scanner testing
FROM node:latest

# Run as root (default) and install via curl | sh
RUN apt-get update && apt-get install -y curl \
    && curl -sL https://deb.nodesource.com/setup_12.x | bash - \
    && apt-get install -y nodejs

# Copy secrets into image
COPY ../secrets/secrets.txt /root/secrets.txt

# Expose SSH port unnecessarily
EXPOSE 22

WORKDIR /app
COPY . /app
CMD ["/bin/sh", "-c", "node -v && sleep 3600"]


