import setuptools

with open("README.md", 'r', encoding="UTF-8") as f:
    long_description = f.read()

version = "0.0.0"

REPO_NAME = "cnn-project"
AUTHOR_NAME = "Muhammad Hashir"
SRC_REPO = "cnn_classifier"
AUTHOR_EMAIL = "hashirgohar@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=version,
    description="A small Python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    url='https://github.com/Muhammad-Hashir14/End-to-End-DL-Project-DogCatClassification.git',
    project_urls={
        "Bug Tracker": f"https://github.com/Muhammad-Hashir14/End-to-End-DL-Project-DogCatClassification/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
