from setuptools import setup, find_packages

version = "0.0.6"

long_description = ""
try:
    long_description=file('README.md').read()
except Exception:
    pass

license = ""
try:
    license=file('LICENSE').read()
except Exception:
    pass


setup(
    name = 'livecodingtv-publisher',
    version = version,
    description = 'A livecodingtv streaming tool',
    author = 'Pablo Saavedra',
    author_email = 'saavedra.pablo@gmail.com',
    url = 'http://github.com/psaavedra/livecodingtv-publisher',
    packages = find_packages(),
    package_data={
    },
    scripts=[
        "tools/livecodingtv-publisher",
    ],
    zip_safe=False,
    install_requires=[
    ],
    data_files=[
        ('/usr/share/doc/livecodingtv-publisher/',
            ['cfg/livecodingtv-publisher.cfg.example']
        ),
    ],

    download_url= 'https://github.com/psaavedra/livecodingtv-publisher/zipball/master',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Topic :: System :: Operating System Kernels :: Linux",
        "Programming Language :: Python",
        "Topic :: Multimedia :: Video :: Capture",
    ],
    long_description=long_description,
    license=license,
    keywords = "python libav avconv video streaming livecodingtv",
)
