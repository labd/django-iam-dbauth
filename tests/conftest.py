from django.conf import settings
from moto import mock_aws
import boto3
import pytest


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


@pytest.fixture
def rds_client():
    # Use moto to mock the RDS client
    with mock_aws():
        session = boto3.session.Session()
        client = session.client(service_name="rds", region_name="us-west-2")
        yield client
