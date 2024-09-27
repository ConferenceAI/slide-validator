# Slide Validator

This project is an AI-powered slide deck validator for conference organizers. It provides functionality to validate slide decks based on various criteria, including file format, deterministic checks, and AI-powered probabilistic checks.

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables in `.env` file
4. Run the application: `python -m app.main`

## Usage

- POST /slides/validate: Validate a slide deck
- POST /slides/submit: Submit a validated slide deck
- GET /admin/: Access admin panel
- GET /admin/stats: Get validation statistics
- POST /admin/configure: Configure validation checks

For more details, refer to the API documentation at `/docs` when running the application.