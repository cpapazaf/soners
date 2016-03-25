from setuptools import setup
kwargs = {}


setup(
    name='soners',
    version="2.0.0",
    url='',
    license='Apache License',
    author='C.P',
    author_email='xpapazaf@gmail.com',
    description='tornado extension for raspberry serial handling',
    long_description=__doc__,
    packages=['soners'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'tornado>=4.2.1',
    ],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    **kwargs
)
