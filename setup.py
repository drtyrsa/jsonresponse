# -*- coding:utf-8 -*-
from setuptools import setup, find_packages


setup(
    name = "django-jsonresponse",
    version = "0.1.0",
    license = "BSD",
    description = "Simple Django response that encodes data in JSON",
    author = "Vlad Starostin",
    author_email = "drtyrsa@yandex.ru",
    packages = find_packages(),
    include_package_data=True,
    classifiers = [
        'Development Status :: 1 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
