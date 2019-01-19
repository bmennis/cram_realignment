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

--------

Steps
============================

* This pipeline is written for snakemake and uses a conda environment.
* This pipeline begins by pulling the hg38 reference genome, assuming that it is not given, and unzips it.
* The next step is to index the unzipped reference genome as this is necessary for alignment and conversion of bam file from alignment to cram file if desired.
* Next the input cram file is converted back to fastq file by use of samtools fastq function in order to realign the sample data.
* The sample fastq file is then realigned to the indexed reference genome and the output is in bam format.
* Last the pipeline is able to convert the aligned sample data from bam format to cram format using the reference genome for annotation if desired.
* All rules are set to output errors to a log file in the log directory and the constants file const.py is imported to allow rules to grab inputs and direct outputs.
* Requirements and tools used in this project environment have been exported to the cram_realign_env.yml file
* The shell script, run.sh, is to run the snakemake pipeline and is set to submit the jobs to the cluster.
* The run script can be modified to run locally or left to submit to the cluster.

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
