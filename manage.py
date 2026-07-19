#!/usr/bin/env python
import os
import sys
from pathlib import Path

if __name__ == '__main__':
    repo_root = Path(__file__).resolve().parent
    app_root = repo_root / 'ofsg_platform'

    # Ensure imports like `config.settings` resolve when running from repo root.
    if str(app_root) not in sys.path:
        sys.path.insert(0, str(app_root))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH? "
            "Did you forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)
