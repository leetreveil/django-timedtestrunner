from setuptools import setup

setup(
    name='django-timedtestrunner',
    version='0.0.1',
    py_modules=['django_timedtestrunner'],
    author='Lee Treveil',
    author_email='leetreveil@gmail.com',
    license='MIT',
    long_description=open('README.rst').read(),
    url='https://github.com/leetreveil/django-timedtestrunner',
    install_requires=['Django>=1.4'],
)