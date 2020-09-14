"""
Utilities to run sub processes across python versions

This package include utilities that can be used in python 2.7 to start processes in python 3
and retrieve data from them

The ICP (inter-process communication) is done using the filesystem, so it is slow and not efficient

example:

    in this example we assume:
    1. the python executable is at /python/path/python.exe
    2. the python 3 file we want to run is defined in a python module called
       example.mymodule under /pymodules/path
       so the file is at: /pymodules/path/example/mymodule.py
    3. we want to save files to /data/files/


    >> python_executable = "/python/path/python.exe"
    >> module_path = "/pymodules/path"
    >> module = "example.mymodule"
    >> workdir = "/data/files/"
    >> # We can define extra environment variables
    >> env = {
    >>     "PYTHONPATH": module_path
    >> }
    >> clear_folder(workdir)
    >> proc = run_qua_module(python_executable, module, env, workdir=workdir)
    >> code = proc.wait()

    on the other side, we have the python 3 file at: /pymodules/path/example/mymodule.py
    it has the following content:

    >> from py2compatclient import work_folder
    >> path = "%s/sample.npz" % work_folder
    >> np.savez(path, np.linspace(1, 100))

    the py2compatclient module is injected when this file will be executed

    after this execution, an NPZ file will be available in the data directory

"""
from py2compat.process import run_qua_module, clear_folder
