# Use Node.js LTS as base image
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package files for dependency installation
COPY package*.json ./

# Install dependencies
RUN npm install

# Expose port for the dev server
EXPOSE 8080

# Set NODE_ENV to development for hot reloading
ENV NODE_ENV=development

# Command to run the development server with hot reloading
CMD ["npm", "run", "serve"]

