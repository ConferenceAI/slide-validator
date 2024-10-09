# Slide Validator

## Overview

This repo is an AI-powered slide deck validator for conference organizers. It provides functionality to validate slide decks based on various criteria, including format, deterministic and probabilistic checks.

## Features

- Supports multiple file formats: PDF, PPTX, Keynote, Canva, Figma, Markdown, Google Slides (URL).
- Performs deterministic checks on the following attributes:
  - File format
  - File size
  - Slide count
  - Image count
  - Audio count
  - Video count
  - Bullet count
  - Font types used
- Performs probabilistic checks on the following:
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
* **app/models/slide_deck.py**: SlideDeck model with all the slide related attributes.
* **app/utils/file_handler.py**: Manages file uploads and URL processing for slide decks.
* **app/utils/file_handler.py**: To analyze specific file formats and conversions required.
* **app/utils/deterministic_checks.py**: Implements deterministic validation checks on slide decks.
* **app/utils/probabilistic_checks.py**: Implements AI-powered checks on slide content and structure.
* **app/services/openai.py**: To integrate with OpenAI APIs
* **app/services/anthropic.py**: To integrate with Anthropic APIs
* **app/services/huggingface.py**: To integrate with HuggingFace APIs

## Development

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables in `.env` file
4. Run the application: `python -m app.main`

## Questions

Questions or suggestions? Please open an issue in this repository.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.