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


# 27th Feb 2024 @ 23:1937

When downloaded the SRA file for the combined workflow the download result  was like as follow. 

```
(snakemake) ali@ali-MS-7C02:~/Documents/MPRAsnakeflow/resources/combined_basic/data$ prefetch SRR10800986

^[[D2024-02-27T21:38:23 prefetch.3.0.10: Current preference is set to retrieve SRA Normalized Format files with full base quality scores.                                                                                                      2024-02-27T21:38:24 prefetch.3.0.10: 1) Downloading 'SRR10800986'...
2024-02-27T21:38:24 prefetch.3.0.10: SRA Normalized Format file is being retrieved, if this is different from your preference, it may be due to current file availability.
2024-02-27T21:38:24 prefetch.3.0.10:  Downloading via HTTPS...                                                       2024-02-27T21:57:23 prefetch.3.0.10:  HTTPS download succeed
2024-02-27T21:57:41 prefetch.3.0.10:  'SRR10800986' is valid
2024-02-27T21:57:41 prefetch.3.0.10: 1) 'SRR10800986' was downloaded successfully
2024-02-27T21:57:41 prefetch.3.0.10: 'SRR10800986' has 0 unresolved dependencies
(snakemake) ali@ali-MS-7C02:~/Documents/MPRAsnakeflow/resources/combined_basic/data$ 

```