import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='mongoassist',
    version='1.2',
    url='https://github.com/guyingbo/mongoassist',
    download_url="https://github.com/guyingbo/mongoassist/archive/master.zip",
    license='MIT',
    author='Gu Yingbo',
    author_email='tensiongyb@gmail.com',
    description='A very simple mongodb client wrapper.',
    long_description='docs: https://github.com/guyingbo/mongoassist',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=("pymongo",),
    packages=['mongoassist'],
    #include_package_data = True,
    test_suite='nose.collector',
    platforms='any'
)
