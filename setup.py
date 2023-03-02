import re

from setuptools import find_packages, setup

docs_require = []

tests_require = [
    "coverage[toml]>=6.2,<=7.2.1",
    "pretend==1.0.9",
    "pytest>=7.0.1,<=7.3",
    "pytest-cov==4.0.0",
    "pytest-mock>=3.6.1,<=3.11",
    "pytest-django==4.5.2",
    "psycopg2==2.9.5",
    "mysqlclient==1.4.6,<=2.2",
]


with open("README.md") as fh:
    long_description = re.sub(
        "<!-- start-no-pypi -->.*<!-- end-no-pypi -->\n",
        "",
        fh.read(),
        flags=re.M | re.S,
    )

setup(
    name="django-iam-dbauth",
    version="0.1.4",
    description="Django database backends to use AWS Database IAM Authentication",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LabD/django-iam-dbauth",
    author="Lab Digital",
    author_email="opensource@labdigital.nl",
    install_requires=["Django>=3.2", "boto3", "dnspython"],
    tests_require=tests_require,
    extras_require={"docs": docs_require, "test": tests_require},
    entry_points={},
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    zip_safe=False,
)
