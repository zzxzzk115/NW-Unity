from setuptools import setup
from os import path

DIR = path.dirname(path.abspath(__file__))
# INSTALL_PACKAGES = open(path.join(DIR, 'requirements.txt')).read().splitlines()

with open(path.join(DIR, 'README.md')) as f:
    README = f.read()

setup(
    name='nwunity',
    packages=['nwunity'],
    entry_points = {
        'console_scripts': [
            'nwunity = nwunity.cli:main',
        ],
    },
    description="NW-Unity is a tool for auto packing your Unity WebGL output files to a NW.js executable file.",
    long_description=README,
    long_description_content_type='text/markdown',
    # install_requires=INSTALL_PACKAGES,
    version='0.2.16',
    url='https://github.com/zzxzzk115/NW-Unity',
    author='Lazy_V',
    author_email='954294627@qq.com',
    keywords=['NW.js', 'GameShell', 'Unity', 'WebGL'],
    # tests_require=[
    #     'pytest',
    #     'pytest-cov',
    #     'pytest-sugar'
    # ],
    include_package_data=True,
    python_requires='>=3'
)