from setuptools import setup

setup(
    name='pdfsort',
    version='0.1',
    py_modules=['idk'],
    install_requires=[
        'Click',
        'PyPDF2',
        'mock'
    ],
    entry_points='''
        [console_scripts]
        pdfsort=pdfsort_cli.pdfsort_cli:cli
    ''',
)
