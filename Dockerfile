# Use an official Python runtime as a parent image
FROM python:3.12-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
# Install Playwright

# Install streamlit and any other dependencies
RUN pip3 install streamlit

# Install any needed packages specified in requirements.txt
# Note: We're using pip3 as specified in the devcontainer.json
RUN pip3 install --no-cache-dir -r requirements.txt
# Install Playwright dependencies
RUN playwright install-deps

# Install Playwright browsers
RUN playwright install

# Note: You may need to adjust this if your app uses a different port
EXPOSE 8501


# Run the application
# Note: You'll need to replace 'your_main_script.py' with the actual name of your main Python script
CMD ["streamlit", "run", "/app/src/interface.py"]

