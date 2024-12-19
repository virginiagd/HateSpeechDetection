# HateSpeechDetection

This project aims to detect hate speech in texts. It is designed as part of the course Deep Learning and Software Engineering. 

## Docker
## Build the Docker Image

Ensure you are in the project directory, then run:

```bash
docker build -t hatespeechdetection:latest .
```

## Run the Docker Container

```bash
docker run -d -p 5000:5000 --name hatespeechdetection hatespeechdetection:latest
```
