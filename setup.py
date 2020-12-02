import os
from setuptools import setup, Extension
from Cython.Build import cythonize

program_path = "/".join(os.path.abspath(__file__).split("\\")[:len(os.path.abspath(__file__).split("\\"))-1])
program_files = [program_path + val.replace("\\", "/")[1:] for sublist in [[os.path.join(i[0], j) for j in i[2]] for i in os.walk('./')] for val in sublist]

setup(
    name='INETBF Network Testing Library',
    maintainer="Drakeo",
    maintainer_email="obfuscate@riseup.net",
    install_requires=[
        "numpy", "psutil", "cython", "requests", 
        "pymysql", "paramiko"
    ],
    description="Framework set for testing persistence and hardening of a protocol",
    
    ext_modules=[
        cythonize(pyx_file)
        for pyx_file in program_files
        if(program_files.endswith(".pyx"))   
    ]
)