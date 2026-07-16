# OFSG SACCO Platform

This Django project provides a basic SACCO portal with custom member management.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate it:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
3. Install dependencies:
   ```bash
   pip install django
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the server:
   ```bash
   python manage.py runserver
   ```

## Members App
- Custom `Member` model extends `AbstractUser`
- `Contribution` model tracks member contributions
- `Fine` model tracks penalties
