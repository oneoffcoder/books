
from setuptools import setup, find_packages

with open('README.rst', 'r') as fh:
    long_desc = fh.read()

setup(
    name='pydemo',
    version='0.0.1',
    author='One-Off Coder',
    author_email='info@oneoffcoder.com',
    packages=find_packages(),
    description='Just a demo!',
    long_description=long_desc,
    long_description_content_type='text/x-rst',
    url='https://github.com/oneoffcoder',
    keywords=' '.join(['docker', 'python']),
    install_requires=['numpy', 'scipy', 'pandas'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Development Status :: 5 - Production/Stable'
    ],
    include_package_data=True
)