import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version = "0.0.1"

Repo_Name = "Project-Text-Summarizer"
Author_Username = "pramitgarg"
Src_Repo = "Textsummarizer"
Author_Email = "pramitgarg0906@gmail.com"

setuptools.setup(
    name=Repo_Name,
    version=__version,
    author=Author_Username,
    author_email=Author_Email,
    description="A python package for NLP App",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/pramitgarg/Project-Text-Summarizer",
    project_urls={
        "Bug Tracker": f"https://github.com/pramitgarg/Project-Text-Summarizer-/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)