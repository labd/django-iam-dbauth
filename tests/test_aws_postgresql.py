import boto3
import pretend

from django_iam_dbauth.aws.postgresql.base import DatabaseWrapper


def test_get_connection_params(mocker):

    token_kwargs = {}

    def generate_db_auth_token(**kwargs):
        token_kwargs.update(kwargs)
        return "generated-token"

    client = pretend.stub(generate_db_auth_token=generate_db_auth_token)
    mocker.patch.object(boto3, "client", return_value=client)

    settings = {
        "NAME": "example",
        "USER": "postgresql",
        "PASSWORD": "secret",
        "PORT": 5432,
        "HOST": "example-cname.labdigital.dev",
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
        "host": "example-cname.labdigital.dev",
    }
    assert params == expected
    assert token_kwargs == {
        "DBHostname": "www.labdigital.nl",
        "DBUsername": "postgresql",
        "Port": 5432,
    }
