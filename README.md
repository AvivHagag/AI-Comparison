# React Website: Comparing Products with AI

This repository contains a React-based website that utilizes artificial intelligence to compare products based on their reviews. The website allows users to send drive links of JSON files containing product data, which are then processed by the AI model. The comparison results are displayed on the website, providing insights into the products based on their reviews.

## Features

Upload JSON files from Google Drive: Users can provide drive links of JSON files containing product data. These files should follow a specific structure to ensure proper processing by the AI model.
Artificial Intelligence Comparison: The uploaded data is processed by an AI model, which analyzes the reviews and provides a comparison of the products. The AI model uses natural language processing techniques to understand the sentiment and key features mentioned in the reviews.
Interactive User Interface: The React website offers a user-friendly interface where users can easily upload the JSON files, view the comparison results, and interact with the analyzed data.

### Installation
- npm install
- pip install langchain 
- pip install openai
- Go to path : 'backend/AIApp.py' and set your Open AI API insted 'ENTER-YOUR-API-HERE' in line 102
- Go to server.py file and click "Run" to upload the server and then go to app.js and write in the console "npm run start"
