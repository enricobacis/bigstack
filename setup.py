from setuptools import setup

with open('README.rst') as README:
    long_description = README.read()
    long_description = long_description[long_description.index('Description'):]

setup(name='bigstack',
      version='0.1.1',
      description='Decorator that increase the stack size for a function',
      long_description=long_description,
      url='http://github.com/enricobacis/bigstack',
      author='Enrico Bacis',
      author_email='enrico.bacis@gmail.com',
      license='MIT',
      packages=['bigstack'],
      keywords='stack stacksize recursive recursion decorator'
)
