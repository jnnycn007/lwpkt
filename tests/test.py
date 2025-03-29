import glob, os, shutil

def main():
    retval:int = 0

    rootpath = os.getcwd()
    files = [f for f in glob.glob(os.path.join(os.getcwd(), '**', '*.cmake'), recursive=True) if '__build__' not in f]
    print(files)
    
    for file in files:
        basep = os.path.dirname(file)
        print('Test path:', basep)

        # Reset directory, delete previous runs
        os.chdir(rootpath)
        try: shutil.rmtree('__build__/', ignore_errors=True)
        except: pass

        # Run and test
        os.mkdir('__build__')
        os.chdir('__build__')
        print('Configure the CMake')
        retval += os.system('cmake -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=gcc -S.. -G Ninja -DTEST_CMAKE_FILE_NAME={}'.format(file))
        print('Compile')
        retval += os.system('cmake --build .')
        print('Run test')
        retval += os.system('ctest . --output-on-failure')

if __name__ == '__main__':
    exit(main())