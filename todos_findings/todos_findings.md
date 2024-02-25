# 26th Feb 2024 @ 00:06:46

The data files that are downloaded by the command given does not seem to be correct. Also it is not similar to the tree mentioned in the documentation. It gives the following error:


```
(snakemake) ali@ali-MS-7C02:/media/ali/Data/MPRAsnakeflow/resources/combined_basic$ snakemake -c 1 --use-conda --snakefile ../../workflow/Snakefile --configfile config.yml -n
Building DAG of jobs...
MissingInputException in rule counts_umi_create_BAM in file /media/ali/Data/MPRAsnakeflow/workflow/rules/counts/counts_umi.smk, line 9:
Missing input files for rule counts_umi_create_BAM:
    output: results/experiments/countBasic/counts/useUMI.HEPG2_1_RNA.bam
    wildcards: project=countBasic, condition=HEPG2, replicate=1, type=RNA
    affected files:
        data/SRR10800882_1.fastq.gz
        data/SRR10800882_2.fastq.gz
        data/SRR10800882_3.fastq.gz
```