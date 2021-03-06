from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()

version = '0.1'

install_requires = [
    'xattr',
    'psutil'
]


setup(name='collectdcvmfs',
    version=version,
    description="Collectd Plugin to Monitor CvmFS Clients",
    long_description=README + '\n\n' + NEWS,
    long_description_content_type="text/x-rst",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: System :: Monitoring",
    ],
    keywords='collectd cvmfs monitoring',
    author='Luis Fenandez Alvarez',
    author_email='luis.fernandez.alvarez@cern.ch',
    url='https://github.com/cvmfs/collectd-cvmfs',
    license='Apache II',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    data_files = [('/usr/share/collectd/', ['resources/collectdcvmfs.db'])],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires
)
