import glob, os, shutil, sys

def main():
    retval:int = 0

    rootpath = os.getcwd()
    files = [f for f in glob.glob(os.path.join(os.getcwd(), '**', '*.cmake'), recursive=True) if '__build__' not in f]
    print(files, flush=True)
    
    for file in files:
        basep = os.path.dirname(file)
        print('Test path:', basep, flush=True)

        # Reset directory, delete previous runs
        os.chdir(basep)
        try: shutil.rmtree('__build__/', ignore_errors=True)
        except: pass

        # Run and test
        os.mkdir('__build__')
        os.chdir('__build__')
        print('Configure the CMake', flush=True)
        retval |= os.system('cmake -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=gcc -S../.. -G Ninja -DTEST_CMAKE_FILE_NAME={}'.format(file))
        print('Compile', flush=True)
        retval |= os.system('cmake --build .')
        print('Run test', flush=True)
        retval |= os.system('ctest . --output-on-failure')

    return retval

if __name__ == '__main__':
    sys.exit(1 if main() != 0 else 0)