from django.conf import settings


def pytest_configure():
    settings.configure(
        HEALTH_CHECKS={},
        MIDDLEWARE_CLASSES=[],
        SECRET_KEY="0123456789",
        INSTALLED_APPS=[
            "django.contrib.admin",
            "django.contrib.contenttypes",
            "django.contrib.auth",
            "django.contrib.sessions",
        ],
        CACHES={
            "default": {
                "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
                "LOCATION": "unique-snowflake",
            }
        },
        DATABASES={
            "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite"}
        },
        MIDDLEWARE=(
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
        ),
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "OPTIONS": {
                    "loaders": ("django.template.loaders.app_directories.Loader",)
                },
            }
        ],
        USE_TZ=True,
        ROOT_URLCONF="test_urls",
    )
