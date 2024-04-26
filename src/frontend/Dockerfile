# Use the official Node.js image as a base image
FROM node:alpine as build

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json files to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the entire project directory to the working directory
COPY . .

# Build the React app for production
RUN npm run build

# Use the official Nginx image as a base image for serving the React app
FROM nginx:alpine

# Copy the build files from the previous stage to the default Nginx public folder
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
