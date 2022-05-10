# Automatic-Crossword-Generator
Marvin Vihman's bachelor's thesis "Automatic crossword generator" (University of Tartu, 2022).

The program's algorithm for making crosswords is a little funky right now, for some reason it sometimes 
overwrites words, that have already been added to the table.
Current problems also include some words missing definitions in the Estonian Wordnet.

This project can only run on Python versions 3.7-3.9, because EstNLTK supports only those currently.

To use it on the web, use the given link [https://ristsona-genereerija.herokuapp.com/](https://ristsona-genereerija.herokuapp.com)

To run the program locally, it needs to have EstNLTK, Flask and Pandas installed. For easier use, it's 
recommended to download and install Anaconda (https://www.anaconda.com/distribution/), 
and for less disk usage [Miniconda](https://conda.io/en/latest/miniconda.html) can also be installed.

Using Anaconda or Miniconda GUI version or the Anaconda (Powershell) Prompt, do the next steps.

1. ```conda create -n env_name python=3.9 ```

2. ```conda activate env_name```

Now when virtual env has been created, then you can install the needed moduls.

3. ```conda install -c estnltk -c conda-forge estnltk```
4. ``pip install flask``
5. ``pip install pandas``

This project has many ways, that it can be improved upon, and those will be kept for the future.

