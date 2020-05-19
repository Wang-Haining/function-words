from setuptools import setup

setup(
    name='WAW',
    version='0.0.1',
    description='''WAW is the acronym for "Words Against Words."''',
    py_modules=['WAW'],
    package_dir={'': 'src'}, install_requires=['nltk']
)