from setuptools import find_packages, setup

docs_require = []

tests_require = []
tests_require = [
    "coverage==4.5.4",
    "pytest==5.1.2",
    "pytest-cov==2.7.1",
    "pytest-django==3.5.1",
]


setup(
    name="django-iam-dbauth",
    version="0.0.1",
    description="Django database backends to use AWS Database IAM Authentication",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LabD/django-iam-dbauth",
    author="Lab Digital",
    author_email="opensource@labdigital.nl",
    install_requires=["Django>=1.11", "boto3"],
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
        "Framework :: Django :: 1.11",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    zip_safe=False,
)
