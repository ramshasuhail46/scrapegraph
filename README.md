# Graphly

Graphly is a project that combines web scraping and AI technologies, utilizing Streamlit for its user interface.

## Getting Started

This project uses DevContainers for a consistent development environment.

### Prerequisites

- Docker
- Visual Studio Code with the Remote - Containers extension

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/scrapegraph-ai.git
   ```

2. Open the project in Visual Studio Code.

3. When prompted, click "Reopen in Container" or use the command palette (F1) and select "Remote-Containers: Reopen in Container".

4. VS Code will build the DevContainer and set up the environment automatically.

## Running the Application

To run the Streamlit application locally:

1. Open a terminal in VS Code (if not already open).

2. Run the following command:
   ```
   streamlit run interface.py
   ```

3. Open a web browser and navigate to the URL provided in the terminal (usually http://localhost:8501).

## Deployment

To deploy the ScrapegraphAI application using Docker on a virtual machine:

1. Ensure Docker and Docker Compose are installed on your virtual machine.

2. Copy your project files, including the Dockerfile and docker-compose.yml, to the virtual machine.

3. Navigate to the project directory on the virtual machine.

4. Build and start the Docker containers using the following command:
   ```
   docker-compose up -d
   ```

5. The application should now be running on the virtual machine. Access it using the virtual machine's IP address and the port specified in your docker-compose.yml file.

Note: Make sure your virtual machine's firewall allows incoming traffic on the port your application is using.

## Features

- Web scraping capabilities
- AI-powered data analysis
- Interactive Streamlit interface
