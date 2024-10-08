# Slide Validator

## Overview

This project is an AI-powered slide deck validator for conference organizers. It provides functionality to validate slide decks based on various criteria, including format, deterministic and probabilistic checks.

## Features

- Supports multiple file formats: PPTX, PDF, Keynote, Canva, Figma, Google Slides etc.
- Performs deterministic checks on the following:
  - File Size
  - Slide count
  - Image count
  - Audio count
  - Video count
  - Bullet point count
  - Fonts used
  - Presence of title slide
- Implements AI-powered checks
- Provides an admin interface for configuring validation criteria
- Offers a user-friendly web interface for uploading and validating slides

## APIs

- POST /slides/validate: Validate a slide deck
- POST /slides/submit: Submit a validated slide deck
- GET /admin/: Access admin panel
- GET /admin/stats: Get validation statistics
- POST /admin/configure: Configure validation checks

For more details, refer to the API documentation at `/docs` when running the application.

## Structure

The app is divided into several components:

* **app/main.py**: The main FastAPI application that serves as the entry point for the web service.
* **app/routers/slides.py**: Handles API routes for slide validation and submission.
* **app/routers/admin.py**: Handles API routes for admin criteria configuration.
* **app/services/file_handler.py**: Manages file uploads and URL processing for slide decks.
* **app/services/file_analyzer.py**: Performs detailed analysis on various file formats (PPTX, PDF, Keynote, etc.).
* **app/services/deterministic_checks.py**: Implements deterministic validation checks on slide decks.
* **app/services/ai_checks.py**: Implements AI-powered checks on slide content and structure.

## Development

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables in `.env` file
4. Run the application: `python -m app.main`

## Questions

Questions or suggestions? Please open an issue in this repository.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.