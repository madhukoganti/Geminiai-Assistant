# Gemini AI Assistant

A Django-based AI chatbot powered by the Gemini API. The application provides user authentication, personalized chat history, input validation, and a responsive chatbot interface.

## Features

* Gemini AI chatbot integration
* User registration and login
* Logout functionality
* User-specific chat history
* Clear chat history
* Input validation
* Error handling for Gemini API failures
* Automated Django tests
* Responsive chatbot UI

## Technologies Used

* Python
* Django
* Django REST Framework
* Google Gemini API
* SQLite
* HTML
* CSS
* JavaScript

## Project Structure

```text
geminiai_assistant/
├── chatbot/
├── geminiai_assistant/
│   └── templates/
├── .gitignore
├── manage.py
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/madhukoganti/Geminiai-Assistant.git
cd Geminiai-Assistant
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install django djangorestframework google-genai python-dotenv
```

### 4. Create the `.env` file

Create:

```text
geminiai_assistant/.env
```

Add your Gemini API key:

```text
GEMINIAI_API_KEY=your_api_key_here
```

Never upload your real API key to GitHub.

### 5. Apply migrations

```powershell
python manage.py migrate
```

### 6. Run the development server

```powershell
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/chatbot/
```

## Running Tests

Run:

```powershell
python manage.py test chatbot
```

The project currently includes tests for:

* Empty messages
* Whitespace-only messages
* Non-string messages
* Messages longer than 5000 characters

## API Endpoint

### Chat

```text
POST /chatbot/chat/
```

Example request:

```json
{
    "message": "What is artificial intelligence?"
}
```

## Security

The Gemini API key is stored in an environment variable and excluded from Git using `.gitignore`.

## Author

Madhu Latha
