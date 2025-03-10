[![DOI](https://zenodo.org/badge/905667462.svg)](https://doi.org/10.5281/zenodo.15002841)

# HateSpeechDetection

This project aims to detect hate speech in texts. It is designed as part of the course Deep Learning and Software Engineering. 

### Docker
#### Build the Docker Image

Ensure you are in the project directory, then run:

```bash
docker build -t hatespeech .
```

#### Run the Docker Container

```bash
docker run -p 5000:5000 hatespeech
```

#### Access the Application

The application will be available at http://localhost:5000. 
