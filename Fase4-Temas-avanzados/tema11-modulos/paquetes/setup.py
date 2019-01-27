# setuptools por defecto
# paquete distribuible
# para crear el distribuible python setup.py sdist
# para usar stuptools installar con pip
# para instalar paguete distribuible pip3 install paquete-0.1.tar.gz
from setuptools import setup

setup(
    name="paquete",
    version="0.1",
    description="Este es un paquete de ejemplo",
    author= "Alejandro Ortegano",
    author_email= "tus@perritos.com",
    url="http://tusperrico.com",
    scripts=[],
    packeges=["paquete","paquete.adios","paquetes.hola"]
)
