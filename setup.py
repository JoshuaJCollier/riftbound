import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="over-simplified-downloader",
    version="0.0.1",
    author="Awes",
    author_email="awes.me@proton.com",
    description=("A tool to convert decks from tcg-arena"
                "to paste into UVS for competitions."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoshuaJCollier/riftbound",
    project_urls={
        "Project Main": "https://github.com/JoshuaJCollier/riftbound",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "download = downloader.cli:main",
        ]
    }
)