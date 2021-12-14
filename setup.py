import setuptools

setuptools.setup(
    name="streamsb-py",
    version="1.0.0",
    author="code_xed",
    author_email="telegram @necromantik",
    description="An unoffcial API wrapper for streamsb.com",
    license="MIT",
    url="https://github.com/code_xed/streamsb-py",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[
        'requests'
    ],
)
