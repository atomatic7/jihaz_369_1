# Jihaz_369 
# Flask Chat Application

A simple chat application built with Flask, designed to be deployed on Vercel. This application enables real-time messaging with a minimalistic design and RESTful API.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment on Vercel](#deployment-on-vercel)
- [Contributing](#contributing)
- [License](#license)

## Features

- Real-time messaging
- Simple and user-friendly interface
- Flask backend API
- Deployable on Vercel

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or above
- Flask
- Vercel CLI

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/atomatic7/jihaz_369_1.git)
   cd flask-chat-app

2. **Set Up Virtual Environment**

Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

2. **Install Dependencies**

Install the necessary dependencies from requirements.txt:

    ```bash
    pip install -r requirements.txt

3. **Start Application**

Start the Flask development server:

    ```bash
    flask run

### Deployment on Vercel

1. **Install Vercel CLI**

 
   ```bash
   npm install -g vercel

2. **Log in to Vercel**

Authenticate your Vercel account in the terminal:

    ```bash
    vercel login
    
3. **Create vercel.json File**

In the root of your project, create a file named vercel.json. This file helps configure how Vercel handles your Flask application. Here's a basic configuration for Flask:

4. **Deploy to Vercel**

From the project directory, run:

    ```bash
    vercel

5. **Finalize Deployment**

Once the deployment is complete, Vercel will provide a unique URL for your application (e.g., https://jihaz-369.vercel.app). You can access your application there.

6. **Subsequent Deployments**

After making changes to your app, redeploy it using:

    ```bash
    vercel --prod

### Contributing

1. **Fork the repository.
 
2. **Create a new branch (git checkout -b feature-branch).
 
3. **Commit your changes (git commit -m 'Add new feature').
 
4. **Push to the branch (git push origin feature-branch).
 
5. **Create a Pull Request.


    

