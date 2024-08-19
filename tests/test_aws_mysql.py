import boto3
import urllib
import pretend

from django_iam_dbauth.aws.mysql.base import DatabaseWrapper


def test_get_connection_params(rds_client):
    settings = {
        "NAME": "example",
        "USER": "mysql",
        "PASSWORD": "secret",
        "PORT": 3306,
        "HOST": "example-cname.labd.nl",
        "ENGINE": "django_iam_dbauth.aws.mysql",
        "OPTIONS": {
            "use_iam_auth": 1,
            "region_name": "test",
            "resolve_cname_enabled": False,
        },
    }

    db = DatabaseWrapper(settings)
    params = db.get_connection_params()

    assert params["password"].startswith("example-cname.labd.nl")
