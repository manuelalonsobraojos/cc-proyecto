from setuptools import setup, find_packages

setup(
    name='bot',
    version='1.3',
    packages=find_packages(exclude=["tests", "tools"]),
    url='',
    license='',
    author='Manuel Alonso',
    author_email='',
    description='',
    install_requires=['beautifulsoup4==4.8.1','certifi==2019.9.11','cffi==1.13.2','chardet==3.0.4','Click==7.0',
                      'Flask==1.1.1','sanic==20.12.6', 'Flask-Caching==1.8.0', 'gevent==1.4.0','greenlet==0.4.15','idna==2.8','itsdangerous==1.1.0','Jinja2==2.10.3', 'linecache2==1.0.0', 'MarkupSafe==1.1.1',
                      'peewee==3.11.2', 'psycopg2==2.8.4', 'pycparser==2.19', 'requests==2.22.0', 'six==1.13.0', 'soupsieve==1.9.5', 'traceback2==1.4.0', 'unittest2==1.1.0', 'urllib3==1.25.6', 'Werkzeug==0.16.0']
)
