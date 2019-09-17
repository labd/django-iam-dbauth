import boto3
import pretend
from django_iam_dbauth.aws.postgresql.base import DatabaseWrapper


def test_get_connection_params(mocker):
    client = pretend.stub(generate_db_auth_token=lambda **kwargs: "generated-token")
    mocker.patch.object(boto3, "client", return_value=client)

    settings = {
        "NAME": "example",
        "USER": "postgresql",
        "PASSWORD": "secret",
        "PORT": 5432,
        "HOST": "db.example.com",
        "ENGINE": "django_iam_dbauth.aws.postgresql",
        "OPTIONS": {"use_iam_auth": 1},
    }

    db = DatabaseWrapper(settings)
    params = db.get_connection_params()

    expected = {
        "database": "example",
        "user": "postgresql",
        "password": "generated-token",
        "port": 5432,
        "host": "db.example.com",
    }
    assert params == expected
