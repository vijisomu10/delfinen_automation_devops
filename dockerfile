# FROM python:3.10

# # Set the working directory inside the container
# WORKDIR /app

# # Copy the requirements file into the container
# COPY requirements.txt .

# # Install the project dependencies
# RUN pip install -r requirements.txt

# # Copy the rest of the application code into the container
# COPY . .

# # Expose the port the app runs on (change this if your app runs on a different port)
# EXPOSE 8000

# # Define the command to run the application
# CMD ["streamlit run streamlit_app.py"]
# Example Dockerfile
FROM python:3.10-slim 

# Install Streamlit
RUN pip install streamlit

# Set the working directory
WORKDIR /app

# Copy the Streamlit app file into the container
COPY streamlit_app.py /app/

# Expose the port Streamlit uses (8501 by default)
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "streamlit_app.py"]
