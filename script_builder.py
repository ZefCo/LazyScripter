import os
from sys import platform

hello_world = '''
import os
from sys import platform


def main():
    # home = platformer()
    # cdrive, ddrive = platformer()
    pass


def platformer():
    user: str = 'ethanspeakman'
    if platform == 'linux' or platform == 'linux2':
        home: str = os.path.join('/', 'home', user)

        return home

    elif platform == 'win32':
        cdrive: str = os.path.join('C:/')
        ddrive: str = os.path.join('D:/')

        return cdrive, ddrive

if __name__ in '__main__':
    main()
    '''


def build_script(*args, file_name='main.py'):    
    cwd: str = os.getcwd()
    directory: str = os.path.join(cwd, '')
    for dirs in args:
        directory = os.path.join(cwd, dirs)
    if not os.path.isdir(directory):
        os.makedirs(directory)
    file_path: str = os.path.join(cwd, directory, file_name)
    with open(file_path, 'w+') as py_file:
        py_file.write(hello_world)

def main():
    file_name: str = input('Input file name (leave blank for default = main.py): ')
    print(os.getcwd())
    dire_name: str = input('Input directory to make (leave blank for none): ')
    if not file_name in '':
        build_script(dire_name, file_name=file_name)
    else:
        build_script(dire_name)

if __name__ in '__main__':
    main()