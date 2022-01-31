from setuptools import setup, Extension
from Cython.Build import cythonize


#module = Extension ('helloworld', sources=['helloworld.pyx'])

setup(
    name='Github',
    version='1.0',
    #packages=[''],
    #url='',
    #license='',
    author='TK',
    #author_email='',
    description='helloworld',
    ext_modules=cythonize(".//src//helloworld.pyx"),
    zip_safe = False,
)
