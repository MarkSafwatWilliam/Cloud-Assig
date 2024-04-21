FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and the text file into the container
COPY main.py /app/main.py
COPY paragraph.txt /app/paragraph.txt

# Install NLTK and download necessary resources
RUN pip install nltk && \
    python -m nltk.downloader punkt stopwords

# Run the Python script
CMD ["python", "main.py"]
