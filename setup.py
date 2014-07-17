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
    url='http://pypi.python.org/pypi/HDFTools/',
    license='LICENSE.txt',
    description='Wrapper for pyhdf and PyTables',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.1.1",
        "caldav == 0.1.4",
    ],
)