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
