from distutils.core import setup


packages=[
    	'hdftools'
]


setup(
    name='HDFTools',
    version='0.1.0',
    author='P. Castellanos',
    author_email='patti.castellanos@gmail.com',
    packages = packages,
    url='https://github.com/patticastellanos/hdftools',
    license='LICENSE.txt',
    description='Wrapper for pyhdf and PyTables',
    long_description=open('README.md').read(),
)