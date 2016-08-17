from setuptools import setup, find_packages

setup(
    name='transfer_lib',
    version='1.0.3',
    description='Transfer Library',
    long_description='https://pypi.python.org/pypi/transfer_lib',
    url='https://github.com/Akira-Taniguchi/transfer_libb',
    author='AkiraTaniguchi',
    author_email ='dededededaiou2003@yahoo.co.jp',
    packages=find_packages(),
    license='MIT',
    keywords='ftp sftp ftps https http transfer download upload',
    classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Programming Language :: Python :: 2.7',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License'
    ],
    install_requires=['pysftp==0.2.8']
)
