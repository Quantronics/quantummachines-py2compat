import setuptools

with open("VERSION", "r") as f:
    version = f.readline()

if len(version) < 1:
    raise Exception("No version specified")

print("Building version {}".format(version))
setuptools.setup(
    name='py2compatclient',
    version=version,
    scripts=[],
    author="Tal Shani",
    author_email="tal@quantum-machines.co",
    description="Compatibility layer to start python 3 processes and execute QUA programs",
    url="https://quantum-machines.co",
    packages=["py2compat"],
    data_files=["VERSION", "py2compat/_remote/py2compatclient/__init__.py", "py2compat/_remote/py2compatclient/icp.py"],
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
    ],
)
