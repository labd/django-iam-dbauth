# Django IAM database backends

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
        "ENGINE": 'django_iam_dbauth.aws.postgresql'
        "OPTIONS": {
            "use_iam_auth": True
        }
    }
}
```

# Caveats

1. You cannot use a cname for the host, it needs to be the actual hostname of
the RDS instance.
