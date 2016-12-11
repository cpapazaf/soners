from setuptools import setup
kwargs = {}


setup(
    name='soners',
    version="1.0.0",
    url='https://github.com/cpapazaf/soners',
    license='Apache License',
    author='Christos Papazafeiropoulos',
    author_email='xpapazaf@gmail.com',
    description='PySerial reader extension for Tornado',
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
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    **kwargs
)
