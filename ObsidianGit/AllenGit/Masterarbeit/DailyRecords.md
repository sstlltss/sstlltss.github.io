### 26.06.2026
- dmrs finished - split .cov into chrs and compare them one by one to avoid OOM; chrX, chrY, chrM are not needed
- methylbert - finetuning_data_prepare.py: customized for multi-cell-type input and multi-dmr-file input.

### 27.06.2026
- running finetuning_data_prepare.py

### 29.06.2026
- keep debugging finetuning_data_prepare.py
- continue data processing on LUIS

### 30.06.2026
- finetuning_data_prepare.py
	- OOM Error: optimizing... -> read as chunks


## Processing record
- Original data we have: 
	1. DLBCL WGBS data in .fastq.gz
	2. colorectal cancer scBS-seq data in .fastq.gz
	3. pancreatic cancer WGBS data in .fastq.gz
	4. gastrointestinal cancers targeted BS-seq data in .fastq.gz
	5. normal cell atlas in .pat.gz
- Data processing for fastq:
	1. [alignment with Bismark](D:\Study\LUH5\Codes\bismark_alignment.sh)
	2. [sort in name with Samtools, then deduplication with Bismark](D:\Study\LUH5\Codes\bismark_deduplication.txt)
	3. [extraction with Bismark](D:\Study\LUH5\Codes\bismark_deduplication.sh), only keep .cov files (and .bedGraph but not used for so far)
	4. for all the cov files, split them by chromosomes
		- ready for DMRs analysis
	5. for all the original cov files, start -1 to align to 450k Array's position
		- ready for MethyLYZR
- Data processing for .pat.gz:
	1. sum up to cov(where is the script???)
	2. filter with and start+1 to align to 450k Array