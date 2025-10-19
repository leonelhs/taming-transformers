from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

def main():
    setup(
        name='taming-transformers',
        version='0.0.2',
        description='Taming Transformers for High-Resolution Image Synthesis',
        url='https://github.com/CompVis/taming-transformers',
        author='Patrick Esser, Robin Rombach, Bjorn Ommer',
        author_email='patrick.esser@iwr.uni-heidelberg.de',
        packages=find_packages(),
        install_requires=required
    )

if __name__ == "__main__":
    main()