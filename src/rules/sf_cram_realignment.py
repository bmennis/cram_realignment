"""A snakefile of rules to realign a cram file."""

rule all:
"""A target rule to run through the pipeline."""
    input: DATA + 'interim/sample.realign.cram'

rule pull_ref_fa:
"""A rule to pull the reference genome hg38 and deposit it in the data/raw directory if not already available.""" 
    input: 'http://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/hg38.fa.gz'
    output: DATA + 'raw/hg38.fa'
    log: LOG + 'pull_ref_fa/sample.log 
    shell: '(wget {input} | gunzip -c > {output}) 2> {log}'

rule index_ref_fa:
"""A rule to index the reference genome fa file to convert the cram back to fa file and then realign."""
    input: DATA + 'raw/hg38.fa'
    log: LOG + 'index_ref_fa/sample.log'
    shell: 'bwa index {input} 2> {log}'

rule cram_to_fq:
"""A rule to convert the cram file of the samples to fq file using samtools fastq function."""
    input: DATA + 'raw/sample.cram'
    output: DATA + 'interim/sample.fq'
    log: LOG + 'cram_to_fq/sample.log'
    shell: 'samtools fastq {input} > {output} 2> {log}'

rule alignment:
"""A rule to align the fa file to the reference genome."""
    input:
        ref = DATA + 'raw/hg38.fa',
        sample = DATA + 'interim/sample.fq'
    output: DATA + 'interim/sample.realign.bam'
    log: LOG + 'alignment/sample.log'
    shell: '(bwa mem {input.ref} {input.sample} | samtools sort -o {output}) 2> {log}'

rule bam_to_cram:
"""A rule to convert realigned bam output to cram file if desired."""
    input: 
        sample = DATA + 'interim/sample.realign.bam',
        ref = DATA + 'raw/hg38.fa'
    output: DATA + 'interim/sample.realign.cram'
    log: LOG + 'bam_to_cram/sample.log'
    shell: 'samtools view -T {input.ref} -C -o {output} {input.sample} 2> {log}'

