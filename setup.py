from setuptools import setup, find_packages

setup(
    name='JsonLand',
    version='0.1.0',
    description='A tool for converting and formatting between JSON and SQL data',
    author='Yavuz The Dracula',
    author_email='yavuzthedracula@gmail.com',
    packages=find_packages(),
    install_requires=[
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'jsonland=jsonland:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
