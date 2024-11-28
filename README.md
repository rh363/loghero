# LogHero

LogHero is a simple Django application designed to log generic information in the database in a structured way. 
It provides a convenient way to record and manage logs with customizable severity and status levels.

## Project Overview

- **Name**: LogHero
- **Version**: 1.0.2
- **Description**: A Django app for structured logging of various actions and information.
- **License**: OSI Approved :: The Unlicense
- **Homepage**: [LogHero on GitHub](https://github.com/rh363/LogHero)
- **Issues**: [Issue Tracker](https://github.com/rh363/LogHero/issues)

## Features

- **Logging**: Tracks actions, actors, target entities, severities, statuses, and contextual metadata.
- **Admin Integration**: Provides an admin interface for log monitoring and filtering.
- **Enums for Choices**: Uses Django's `TextChoices` for handling log statuses and severities.
- **Location auto discovery**: LogHero use [hostip_client](https://github.com/rh363/hostip_client) for get ip location from [hostip.info](https://hostip.info/).

## Prerequisites

- Python 3.8 or higher
- Django 4.2 or higher

## Installation

To install LogHero, follow these steps:

1. Clone the repository:
   ```bash
   pip install loghero
   ```

2. Add `loghero` to your `INSTALLED_APPS` in your Django project's `settings.py`:
   ```python
   INSTALLED_APPS = [
       ...
       'loghero',
       ...
   ]
   ```

3. Run database migrations:
   ```bash
   python manage.py migrate
   ```

## Usage

### Logging Actions

Use the `add_log` function to create a new log entry:

```python
from loghero.models import Severity, Status
from loghero import add_log, get_client_ip

ip = get_client_ip(request) # django http request optional
add_log(
    actor='John Doe',
    action='Login Attempt',
    severity=Severity.INFO,
    status=Status.SUCCESS,
    target='user@example.com',
    target_type='User',
    ip_address=ip, #optional
)
```

### Admin Interface

Access the admin panel to view and filter log entries. Customize log visibility using admin configurations in `admin.py`:

- Display crucial log attributes.
- Filter logs by severity and status.
- Search through logs using predefined fields.

## Contributing

If you wish to contribute to LogHero, feel free to open issues or submit pull requests via the GitHub repository linked above.

## License

This project is licensed under the terms of [The Unlicense](LICENSE).

## Dependencies

The project depends on the following packages:

- Django
- ASGIRef
- Certifi
- Charset Normalizer
- Hostip Client
- IDNA
- Requests
- SQLParse
- URLLib3

---
