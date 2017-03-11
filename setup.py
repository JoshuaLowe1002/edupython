from setuptools import setup, find_packages

"""
Copyright (c) 2017 All About Code

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        ]

setup(
    name='edupython',
    version='0.0.2',
    url='https://github.com/AllAboutCode/EduPython',
    description='A Python Library For The EduPython Kits',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    author='All About Code',
    author_email='support@edupython.co.uk',
    license='MIT',
    keywords='edupython camjam edukit python gpio education',
    packages=find_packages(),
    classifiers=classifiers,
    install_requires=['gpiozero', 'guizero'],
    package_data={
        'edupy': ['*.gif']
    },
    
)
