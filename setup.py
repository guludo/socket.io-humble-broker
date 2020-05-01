from setuptools import setup

with open("README.rst", "r") as f:
    long_description = f.read()

setup(
    name='socket.io-humble-broker',
    version='0.0.0',
    author='Gustavo José de Sousa',
    author_email='gustavo.jo.sousa@gmail.com',
    description='A very simple socket.io message broker',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/guludo/socket.io-humble-broker',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development',
    ],
    install_requires=[
        'python-socketio~=4.5',
        'eventlet!=0.25',
    ],
    python_requires='~=3.5',
    py_modules=['socketio_humble_broker'],
    entry_points={
        'console_scripts': [
            'socket.io-humble-broker = socketio_humble_broker:run',
        ],
    },
)
