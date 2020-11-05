import getpass

import boto3

from django_iam_dbauth.utils import resolve_cname


def get_aws_connection_params(params):
    enabled = params.pop("use_iam_auth", None)
    if enabled:
        region_name = params.pop("region_name", "ca-central-1")
        rds_client = boto3.client(service_name="rds", region_name=region_name)

        hostname = params.get("host")
        hostname = resolve_cname(hostname) if hostname else "localhost"

        params["password"] = rds_client.generate_db_auth_token(
            DBHostname=hostname,
            Port=params.get("port", 5432),
            DBUsername=params.get("user") or getpass.getuser(),
        )

    return params
