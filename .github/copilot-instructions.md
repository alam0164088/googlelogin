# Copilot Instructions for googlelogin-main

## Project Overview
This is a Django-based web application with Google login integration. The main components are:
- `google_login_project/`: Django project settings and root URLs.
- `mainApp/`: Core Django app containing models, views, URLs, and admin configuration.
- `static/`: Static assets (CSS).
- `db.sqlite3`: SQLite database for local development.

## Architecture & Data Flow
- All authentication and user management logic is handled in `mainApp/`.
- Google login is integrated using external packages (see `env/lib/python3.12/site-packages/`).
- URLs are routed from `google_login_project/urls.py` to `mainApp/urls.py` and then to views in `mainApp/views.py`.
- Static files are served from the `static/` directory.

## Developer Workflows
- **Run the server:**
  ```bash
  source env/bin/activate
  python manage.py runserver
  ```
- **Migrate database:**
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
- **Run tests:**
  ```bash
  python manage.py test mainApp
  ```
- **Debugging:**
  Use Django's built-in error pages and logging. Check `settings.py` for debug settings.

## Project-Specific Patterns
- All business logic is in `mainApp/views.py`.
- Models are defined in `mainApp/models.py`.
- URL routing is split between project-level and app-level for modularity.
- Static files are organized by type (e.g., `static/css/style.css`).
- Uses virtual environment in `env/` for dependency isolation.

## Integration Points
- Google login uses packages found in `env/lib/python3.12/site-packages/google/` and `allauth/`.
- External dependencies are managed via `pip` in the virtual environment.
- Database is local SQLite (`db.sqlite3`).

## Key Files & Directories
- `google_login_project/settings.py`: Django settings, including installed apps and middleware.
- `google_login_project/urls.py`: Root URL configuration.
- `mainApp/views.py`: Main business logic and authentication flows.
- `mainApp/models.py`: Data models.
- `mainApp/urls.py`: App-specific URL routing.
- `static/`: Static assets.
- `env/`: Python virtual environment.

## Example Patterns
- To add a new view, define it in `mainApp/views.py` and map it in `mainApp/urls.py`.
- To add a new model, define it in `mainApp/models.py`, run migrations, and register it in `mainApp/admin.py` if needed.

---
_If any section is unclear or missing, please provide feedback to improve these instructions._
