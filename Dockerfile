# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
# This includes app.py, lda.py, requirements.txt, and the folders templates/ and static/
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader wordnet


# Make port 5000 available to the world outside this container
EXPOSE 8000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
