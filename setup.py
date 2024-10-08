from setuptools import setup, find_packages

setup(
    name="spankbang_api",
    version="1.0.1",
    packages=find_packages(),
    install_requires=[
        "requests", "lxml", "bs4", "eaf_base_api"
    ],
    entry_points=None,
    author="Johannes Habel",
    author_email="EchterAlsFake@proton.me",
    description="A Python API for the Porn Site spankbang.com",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license="LGPLv3",
    url="https://github.com/EchterAlsFake/spankbang_api",
    classifiers=[
        # Classifiers help users find your project on PyPI
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: Python",
    ],
)