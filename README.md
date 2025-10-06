# AI-Doctor (Medical Chatbot Analyze Image Application)

AI-Doctor is a medical chatbot designed to analyze uploaded images of skin conditions, such as acne, and provide personalized health tips and product recommendations. This application uses advanced image analysis techniques and machine learning models (Llama-3) to provide relevant and useful advice based on the visual input.

## Features

- **Image Upload**: Users can upload images of their skin to get an analysis of potential issues such as acne.
- **Ask Questions**: Users can ask specific health-related questions, and the chatbot will respond with helpful tips and advice.
- **Medical Diagnosis and Recommendations**: The application provides suggestions for managing skin conditions, including skincare routines and product recommendations.
- **Multiple Model Responses**: Two Llama models (Llama-3-2-1b-vision and Llama-3-2-90b-vision) provide different but complementary responses based on the uploaded image and user query.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AI-Doctor.git
   cd AI-Doctor
```
2.Install dependencies
3.Run the application
 ```bash
python app.py
```
## Technologies Used

Python: Programming language for backend development.

Flask: Web framework for building the web application.

Llama-3: Large Language Model used for generating medical advice based on input image and queries.

TensorFlow: For image processing and model deployment.

HTML/CSS/JavaScript: For frontend development.

## Usage

Upload Image: Click on the "Click to Upload" button to upload an image of your skin.

Ask Question: Enter a health-related question in the "Ask Question" box and click "Submit Query" to receive personalized advice.

Get Responses: Based on the uploaded image, the chatbot will provide a detailed response, including potential issues (e.g., acne), recommended actions, and products to use.

## Example Use Case

Upload Image: A user uploads a close-up image of their face showing acne.

Chatbot Response: The chatbot, powered by the Llama-3 model, analyzes the image and responds with advice such as maintaining a consistent skincare routine, using non-comedogenic products, and avoiding touching the face.

Ask Question: The user asks, "What are the tips you can recommend for this type of acne?" The chatbot provides a customized response, including product recommendations like CeraVe Foaming Facial Cleanser and Neutrogena Salicylic Acid Face Wash.

