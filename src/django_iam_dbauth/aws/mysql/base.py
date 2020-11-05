from django.db.backends.mysql import base

from django_iam_dbauth.aws.database_wrapper import get_aws_connection_params


class DatabaseWrapper(base.DatabaseWrapper):
    def get_connection_params(self):
        params = super().get_connection_params()
        params.setdefault("port", 3306)

        return get_aws_connection_params(params)
