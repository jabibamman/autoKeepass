import importlib
import os


def parseRequirements():
    with open('requirements.txt', 'r') as f:
        requirements = f.read().splitlines()
    return requirements


def verifyImport():
    for requirement in parseRequirements():
        try:
            importlib.import_module(requirement)
        except ImportError:
            print(f'{requirement} module not found, installing...')
            os.system(f'pip install {requirement}')
            print(f'{requirement} module installed')


if __name__ == '__main__':
    verifyImport()
