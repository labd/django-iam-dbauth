from django_iam_dbauth.aws.postgresql.base import DatabaseWrapper


def test_get_connection_params(rds_client):
    settings = {
        "NAME": "example",
        "USER": "postgresql",
        "PASSWORD": "secret",
        "PORT": 5432,
        "HOST": "example-cname.labd.nl",
        "ENGINE": "django_iam_dbauth.aws.postgresql",
        "OPTIONS": {
            "use_iam_auth": 1,
            "region_name": "test",
            "resolve_cname_enabled": False,
        },
    }

    db = DatabaseWrapper(settings)
    params = db.get_connection_params()

    assert params["password"].startswith("example-cname.labd.nl")
