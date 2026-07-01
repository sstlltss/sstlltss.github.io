### 26.06.2026
- dmrs finished - split .cov into chrs and compare them one by one to avoid OOM; chrX, chrY, chrM are not needed
- methylbert - finetuning_data_prepare.py: customized for multi-cell-type input and multi-dmr-file input.

### 27.06.2026
- running finetuning_data_prepare.py

### 29.06.2026
- keep debugging finetuning_data_prepare.py
- continue data processing on LUIS

### 30.06.2026
- finetuning_data_prepare.py -> finished!!!
	- OOM Error: optimizing... -> read as chunks

### 01.07.2026
- now working on: finetuning.py

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
	3. [extraction with Bismark](D:\Study\LUH5\Codes\bismark_deduplication.sh), only keep .cov files (and .bedGraph for just in case; not used for so far)
	4. for all the origin .cov files...
		1. split them by chromosomes
			- ready for DMRs analysis
		2. start -1 to align to 450k Array's position
			- ready for MethyLYZR
- Data processing for .pat.gz:
	1. sum up to cov files(where is my script???)
		- start +2 and split by chromosomes for DMRs analysis
	2. filter with 450k Sites and start+1 to align to 450k Array
		- ready for MethyLYZR
- DMRs analysis: [see shell](D:\Study\LUH5\Codes\dss_dmr.R)
- Get 450k Array annotation
- MethyLYZR
	1. data preparation: [see shell](D:\Study\LUH5\Codes\lyzr_data_preparation.py)
		1. samples that only match a few probes(<20000) with 450k Array will be dropped
		2. probes that appear in less than 50% of samples will be dropped
		3. since the presence of a probe exhibits high cancer specificity, imputing missing value using the mean for that specific site in the same cancer type may not yield a valid result. Therefore, use the mean value of the existing sites of the same cancer to fill NA values.