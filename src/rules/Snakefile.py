"""Main snakefile"""

include: "const.py"
include: "sf_cram_realignment.py"

rule all:
    output: LOG + 'DONE'
    shell:  'touch {output}'
