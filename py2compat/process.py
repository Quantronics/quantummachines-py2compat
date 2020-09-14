from subprocess import Popen, PIPE, STDOUT
import os
import shutil

_remote_import_dir = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, "_remote"))


def clear_folder(workdir):
    shutil.rmtree(workdir)
    os.mkdir(workdir)


def run_qua_module(python_path, module, env, workdir):
    return _run_python([
        python_path,
        "-m",
        module,
        workdir
    ], env)


def run_qua_file(python_path, file, env, workdir):
    return _run_python([
        python_path,
        file,
        workdir
    ], env)


def _run_python(args, env):
    full_env = {}
    full_env.update(os.environ)
    full_env.update(env)
    full_env.update({
        "PYTHONPATH": full_env.get("PYTHONPATH") + os.pathsep + _remote_import_dir
    })
    proc = Popen(args, env=full_env, stdout=PIPE, stderr=PIPE)
    return proc
