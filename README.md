# honorableTag

Label videos for computer vision projects using PyQT5, pims, and SQLite.

# Features

Basics functionality implemented including class labeling, pan & zoom, SQL storage, and export in darknet (YOLO) format.

![Labeling Feature](https://media.giphy.com/media/fYC5IGe6ApmXwRgncP/giphy.gif)

![Saving Loading](https://media.giphy.com/media/VbcFlzSvE1VB6iSbXQ/giphy.gif)

![Web Repositories](https://media.giphy.com/media/kdi7GKIakKVU4HSfrX/giphy.gif)

An internal web app to share repositories among teams is in development.

# Installation
Make sure conda-forge is appended to your conda config channels before moving forward with installation.

`conda config --append channels conda-forge`


[PyAV](https://github.com/mikeboers/PyAV)
> Due to the complexity of the dependencies, PyAV is not always the easiest Python package to install. The most straight-foward install is via conda-forge:
`conda install av -c conda-forge`


[PyQt5](https://pypi.org/project/PyQt5/)

`pip install PyQt5`


[PIMS](https://github.com/soft-matter/pims)

Currently using the development version of pims due to a compatability issue.

`pip install git+https://github.com/soft-matter/pims.git`


# Testing
Writing more tests is on the todo list. To run the tests that are available, use the command below.

`python -m tests.test`


## Todo

1. Implement more testing
2. Color change feature
3. Learn to make better README files