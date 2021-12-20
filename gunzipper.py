import sys
import os
import shutil
import gzip

def file_unzip(abs_fn):
    if abs_fn.endswith(".gz"):
        uz_fn = abs_fn[0:-3]
        if os.path.isfile(uz_fn):
            uz_fn = uz_fn[0:-4] + "_DUP_" + uz_fn[-4:]
        with gzip.open(abs_fn, 'rb') as f_in:
            with open(uz_fn, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
                if os.path.isfile(abs_fn):
                    os.remove(abs_fn)
                    print("\'%s\' is decompressed as \'%s\'." % (abs_fn, uz_fn))

def proc_dir(abs_path):
    try:
        files = os.listdir(abs_path)
    except FileNotFoundError:
        print("Error. \'%s\' does not exist!" % abs_path)
        quit()
    for f in files:
        fn = os.path.join(abs_path, f)
        if os.path.isdir(fn) and not f.startswith("."):
            proc_dir(fn)
        elif os.path.isfile(fn) and not f.startswith("."):
            file_unzip(fn)


def gunzip_proc(abs_path):
    print("Start gunzipping...")
    proc_dir(abs_path)
    print("Gunzipping is done.")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        gunzip_proc(os.getcwd())
    elif len(sys.argv) == 2:
        gunzip_proc(os.path.abspath(sys.argv[1]))
    else:
        print("Error. Improper number of parameters.")
        print("Usage: \'python %s\' or \'python %s <directory>\'" % (sys.argv[0], sys.argv[0]))
        print("This script is for gunzipping the all .gz files in the current or specifed directory.")