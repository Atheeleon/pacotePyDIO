from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="buscareceita",
    version="0.0.1",
    author="Antonio",
    author_email="poeticum.visum@gmail.com",
    description="Busca dados de CNPJ na API Minha Receita e devolve um Array JSON",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atheeleon/pacotePyDIO",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)