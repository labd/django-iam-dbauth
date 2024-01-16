from django.contrib.gis.db.backends.postgis import base

from django_iam_dbauth.aws.database_wrapper import get_aws_connection_params


class DatabaseWrapper(base.DatabaseWrapper):
    def get_connection_params(self):
        params = super().get_connection_params()
        params.setdefault("port", 5432)

        return get_aws_connection_params(params)
