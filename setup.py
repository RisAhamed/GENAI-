from setuptools import find_namespace_packages,find_packages,setup
setup(
    name = "mcq",
    author="RisAhamed",
    version="0.0.1",
    install_requires =['openai',"langchain","streamlit","PyPDF2"],
packages=find_packages())