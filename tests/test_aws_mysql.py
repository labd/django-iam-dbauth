import boto3
import pretend

from django_iam_dbauth.aws.mysql.base import DatabaseWrapper


def test_get_connection_params(mocker):

    token_kwargs = {}

    def generate_db_auth_token(**kwargs):
        token_kwargs.update(kwargs)
        return "generated-token"

    client = pretend.stub(generate_db_auth_token=generate_db_auth_token)
    mocker.patch.object(boto3, "client", return_value=client)

    settings = {
        "NAME": "example",
        "USER": "mysql",
        "PASSWORD": "secret",
        "PORT": 3306,
        "HOST": "example-cname.labd.nl",
        "ENGINE": "django_iam_dbauth.aws.mysql",
        "OPTIONS": {"use_iam_auth": 1, "region_name": "test"},
    }

    db = DatabaseWrapper(settings)
    params = db.get_connection_params()

    assert params["password"] == "generated-token"
    assert token_kwargs == {
        "DBHostname": "cluster-name.accountandregionhash.eu-west-1.rds.amazonaws.com",
        "DBUsername": "mysql",
        "Port": 3306,
    }
