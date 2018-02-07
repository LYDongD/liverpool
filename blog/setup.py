# -*- coding: utf-8 -*-


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]


setup(
    name='blog',
    version='1.0.0',
    url='http://repo.xhuabu.com/galaxy/taurus/rose-history.git',
    license="ISCL",
    author="yuedong.li",
    author_email='yuedong.li@xhuabu.com',
    description="blog",
    long_description=open('README.md').read(),
    # packages=find_packages(exclude=['tests', 'venv', 'dist', 'migrations']),
    # package_dir参考https://docs.python.org/2/distutils/setupscript.html
    packages=['app'],

    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    # keywords='',
    # entry_points={
    #     'console_scripts': [
    #         'run_quote = market.main:main'
    #     ]
    # },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    # test_suite='tests',
    # tests_require=test_requirements
)
