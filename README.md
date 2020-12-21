# Django IAM database backends

<!-- start-no-pypi -->
[![codecov](https://codecov.io/gh/labd/django-iam-dbauth/branch/master/graph/badge.svg)](https://codecov.io/gh/labd/django-iam-dbauth)
[![pypi](https://img.shields.io/pypi/v/django-iam-dbauth.svg)](https://pypi.python.org/pypi/django-iam-dbauth/)
[![readthedocs](https://readthedocs.org/projects/django-iam-dbauth/badge/)](https://django-iam-dbauth.readthedocs.io/en/latest/)
[![tests](https://github.com/labd/django-iam-dbauth/workflows/Python%20Tests/badge.svg)](https://github.com/labd/django-iam-dbauth/actions)
<!-- end-no-pypi -->

## Usage

```shell
pip install django-iam-dbauth
```

In your settings use the following

```python
DATABASES = {
    "default": {
        "HOST": "<hostname>",
        "USER": "<user>",
        "NAME": "<db name>",
        "ENGINE": 'django_iam_dbauth.aws.postgresql',
        "OPTIONS": {
            "use_iam_auth": True,
            "sslmode": "require",   # See discussion on SSL below
        }
    }
}
```

### SSL and PostgreSQL

When using IAM authentication with RDS, SSL is required. If it's not used, such as when using a CNAME (see below), login will be denied with the below error:

```
django.db.utils.OperationalError: FATAL:  pg_hba.conf rejects connection for host "1.2.3.4", user "some_user", database "some_database", SSL off
```

### CNAME considerations

Currently, IAM authentication is not supported with CNAMEs. However, this package does CNAME resolution so that the
signed request for a password will work. The issue with this approach is that from the DB library's point of view, the
connection is initiated to the hostname as defined in the settings. If using SSL, certificate verification will fail.
In this case, for PostgreSQL you may want to set `sslmode` to `require` or `verify-ca`.

Further documentation:

* [PostgreSQL SSL modes](https://www.postgresql.org/docs/current/libpq-ssl.html#LIBPQ-SSL-PROTECTION)
* [AWS guide on IAM DB authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html)