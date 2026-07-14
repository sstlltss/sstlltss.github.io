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

### 02.07.2026
- found new bugs in finetuning_data_prepare.py... 😡

### 03.07.2026
- working on finetuning.py

### 06.07.2026
- working on methylseq_simulation: asked Stefan for some help...
- get normal cell(B-cell) .bam files from Stefan's folder.
- testing: finetuning.py

### 08.07.2026
- methylbert debugging...
- take a look at TNT LLM

### 13.07.2026
- methylbert running -> load to gpu(finished)
- next steps:
	- extraction of normal cells (b-cells dataset on luis from Stefan) -> get .cov
		- methylbert: do dmr -> fine-tuning-data-generate -> fine-tuning
		- methylyzr: run

### 14.07.2026
- test methylbert with small train&test data -> overfit ->model can learn correctly
- test methylbert with giant train & test data -> high train loss + lower test loss -> check the data generator and try once more
- finished chapter "relative works" of my thesis
- filter the .cov files with 450k Array(prepare for methylyzr):
	- DLBCL and PC works fine(~400k matched)
	- CC really bad (~10k matched) -> abandoned
	- GC looks doable (~170k matched)
	- B-Cells doesn't match -> aligned with hg38(by Stefan), need to re-processing, now aligning

## Processing record
- Original data we have: 
	1. **DLBCL** WGBS data in .fastq.gz
	2. **colorectal cancer** scBS-seq data in .fastq.gz
	3. **pancreatic cancer** WGBS data in .fastq.gz
	4. **gastrointestinal cancers** targeted BS-seq data in .fastq.gz
	5. normal cell data(**B-Cells**) in .fastq.gz
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