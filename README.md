# DevOps Automated CI/CD Pipeline Demo

This repository demonstrates an automated CI/CD pipeline using GitHub Actions. The workflow automatically tests, builds, and pushes a Docker image to Docker Hub whenever changes are pushed to the main branch.

## Project Overview

- **Server:** The `server.py` script prints a message indicating that the server is running.
- **App:** The `app/__init__.py` module contains a function that returns a success message.
- **Tests:** `test_app.py` verifies that the app function works as expected.
- **Docker:** The `Dockerfile` builds a Docker image that runs the server.
- **CI/CD:** The GitHub Actions workflow in `.github/workflows/ci-cd.yml` runs tests and, if they pass, builds and pushes the Docker image.

## Setup Instructions

1. **GitHub Repository:** Create a new repository on GitHub and push all these files.
2. **Docker Hub:** Create a repository on Docker Hub (e.g., named `ci_cd_demo`).
3. **Secrets:** In your GitHub repository, add the following secrets (Settings > Secrets > Actions):
   - `DOCKERHUB_USERNAME`: Your Docker Hub username.
   - `DOCKERHUB_TOKEN`: Your Docker Hub access token.
4. **Workflow Trigger:** Any push to the main branch will trigger the CI/CD pipeline.

## Screenshots

1. **Docker Hub Image:**  
   Below is a screenshot of the Docker image published on Docker Hub:

   ![Docker Hub Image](https://github.com/user-attachments/assets/4684fd81-5d01-4ca7-bd2e-c36080ad9da7)

2. **GitHub Actions Log:**  
   Below is a screenshot of the GitHub Actions log showing the successful workflow run:

   ![GitHub Actions Log](https://github.com/user-attachments/assets/ed9aca6d-776e-4523-9cc4-e92fa480197b)
