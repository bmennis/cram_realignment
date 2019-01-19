cram_realignment
==============================

A small pipeline to realign a cram file

Project Organization
------------

    ├
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   ├── raw            <- The original, immutable data dump.
    │   
    ├── log                <- Stores log output from tools
    │
    │
    ├── run.sh             <- Run the main snakefile
    |
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    |   ├── rules          <- Snakefile rules
    │   │   ├── const.py   <- File of constants used by rules
    │   │   └── Snakefile      <- Main snakefile
    |   |
    │   ├── scripts        <- Analysis scripts
    |   |
    |   | 
    │

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
