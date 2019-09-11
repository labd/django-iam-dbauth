from django_iam_dbauth.aws.postgresql.base import DatabaseWrapper


def test_get_connection_params():
    db_settings = {}
    db = DatabaseWrapper(db_settings)
