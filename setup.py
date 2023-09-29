from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "readme.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = '''The `FlowGen` is a simple and flexible module that allows users to visualize actor-based interfaces for their systems or projects. It's especially useful for system designers, developers, and architects to quickly draft and visualize interfaces based on different user roles and their associated functionalities.'''

setup(
    name='WebTorchX',
    version='0.0.1',
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=open('readme.md').read() + '\n\n' +
    open('CHANGELOG.txt').read(),
    url='http://nagipragalathan.pythonanywhere.com/',
    author='NagiPragalathan',
    author_email='nagipragalathan@gmail.com',
    license='MIT',
    install_requires=[
        'TerminalDesigner',
        'webdriver_manager==3.8.6',
        'selenium==4.9.0',
        'black==23.7.0',
        'numpy==1.23.5',
        'Stack_data==0.6.2',
        'pyautogui==0.9.53',
        'pytest==7.4.1',
        'colorama'
    ],  # Replace with actual dependencies
    entry_points={
        'console_scripts': [
            'webtorch = PyLowCodeTest.main:main'
        ]
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    KEYWORDS=[
        'LCTP', 'Selenium', 'Low-Code', 'Web Testing Automation', 'Python',
        'JSON Configuration', 'Test Automation', 'Work in Progress', 'Author',
        'Version', 'WebTorch', 'GitHub', 'Contributors', 'Top Language',
        'Telegram', 'Contributions Welcome', 'FAQ', 'GitHub Repo Stars',
        'Twitter Follow', 'Setup', 'Installation', 'Usage', 'JSON Configuration',
        'Login Testing', 'Home Page Testing', 'View Cart Testing',
        'Advanced Features', 'Screen Recording', 'Running and Waiting',
        'Taking Screenshots', 'Executing Python Code'
    ],
    packages=find_packages(),

)
