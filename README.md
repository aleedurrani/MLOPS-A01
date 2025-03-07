# CI/CD Pipeline for Machine Learning Project

## Project Overview
This repository implements a comprehensive CI/CD pipeline for a machine learning project, featuring automated testing, code quality checks, and containerized deployment. The pipeline integrates various DevOps tools to ensure smooth development and deployment workflows.

## Tools & Technologies
- Jenkins (CI/CD orchestration)
- GitHub (Version control & collaboration)
- GitHub Actions (Automated workflows)
- Git (Version control)
- Docker (Containerization)
- Python (Programming language)
- Flask (Web framework)
- Flake8 (Code quality checker)

## Repository Structure
The repository follows a three-branch strategy:
- master: Production-ready code
- test: Feature validation and testing
- dev: Active development and feature implementation

## Pipeline Workflow

### 1. Development Process
1. Create feature branch from dev
2. Implement changes
3. Submit pull request to dev
4. Automated Flake8 code quality check
5. Code review and merge to dev

### 2. Testing Phase
1. Create pull request from dev to test
2. Automated unit tests execution
3. Test validation
4. Merge to test branch upon success

### 3. Production Deployment
1. Create pull request from test to master
2. Final review by admin
3. Merge triggers Jenkins pipeline
4. Docker image creation and push to Docker Hub
5. Admin notification via email

## Setup Instructions

### Prerequisites
1. Install required tools:
   bash
   pip install flask flake8 pytest
   
2. Configure Jenkins with necessary plugins
3. Set up Docker Hub credentials
4. Configure GitHub Actions

### Repository Setup
1. Clone the repository:
   bash
   git clone <repository-url>
   
2. Create and switch to dev branch:
   bash
   git checkout -b dev
   

## GitHub Actions Workflows

### Code Quality Check
- Triggered on pull requests to dev
- Runs Flake8 for code style verification
- Must pass before merge approval

### Feature Testing
- Triggered on pull requests to test
- Executes unit tests
- Validates feature functionality

## Jenkins Pipeline

The Jenkins pipeline performs the following steps:
1. Pulls latest code from master branch
2. Builds Docker image
3. Runs tests inside container
4. Pushes image to Docker Hub
5. Sends notification to admin