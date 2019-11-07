import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ThawPY',
    version='1.0',
    url='https://github.com/fahadahammed/ThawPY',
    license='MIT License ',
    author='Fahad Ahammed',
    author_email='obak.krondon@gmail.com',
    description="""ThawPY is for you if you want to make markdown to html files with predefined design. 
    It is just like a static site generator.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        'pytz', 'markdown', 'jinja2'
    ],
    python_requires='>=3.6'
)
