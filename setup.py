import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

version = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "vaishnavv04"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "vaishnaveega@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version = version,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A package to summarize text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)