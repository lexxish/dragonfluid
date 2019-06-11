from setuptools import setup
import os
import codecs

# get the long description from the relevant file
here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="dragonfluid",
    version="0.9.1.a7",
    description=("A dragonfly extension to allow voice commands to be spoken "
                 "together without pausing. Supports Dragon NaturallySpeaking "
                 "and Windows Speech Recognition."),
    long_description=long_description,    
    url="https://github.com/chajadan/dragonfluid",
    author="Charles J. Daniels",
    author_email="dragonfluid@chajadan.net",
    license="http://www.chajadan.net/licenses/NFFFLicenseV1.txt",
    keywords="speech recognition, voice coding, dragonfly, Dragon, Dragon NaturallySpeaking, Windows Speech Recognition, WSR",
    packages=["dragonfluid"],
    install_requires=[
        "dragonfly2>=0.14.1",
        "six>=1.12.0"
    ],      
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2 :: Only",
        "Programming Language :: Python :: 2.7",
        "Topic :: Adaptive Technologies",
        "Topic :: Other/Nonlisted Topic",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: User Interfaces",        
    ]
)
