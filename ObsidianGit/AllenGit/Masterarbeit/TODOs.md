# TODOs

- [ ] run methylbert after dmrs finished
- [ ] finish data preparation of LYZR and complete LYZR when data on LUIS is prepared

### LUIS

|        | fastq | bam        | cov      | for methylyzr: align position to 450k |
| ------ | ----- | ---------- | -------- | ------------------------------------- |
| CC     | -     | 30         | all done | abandoned due to too few match        |
| DLBCL  | -     | 20         | all done | done(~400k matched)                   |
| GC     | 600/2 | 71         | 71 done  | done(~170k matched)                   |
| PC     | 38/2  | 12         | 12 done  | done(~400k matched)                   |
| B_Cell | 16/2  | processing | queueing |                                       |
### MethylBERT
- [ ] Data pre-processing: multi-cancer-type input -> need to test
- [ ] Fine-tuning: classifier -> need to test

### MethyLYZR
- [x] Training: data pre-processing pipeline script
- [x] Predicting: data input without "score_per_read"
- [ ] script to "align" position of .cov to 450k array
- [ ] re-training and run

### Codes
document everything reproducibility

## !!!send introduction to Jan!!!

## !!!reach up yuesi for git repo.!!!

## !!! contact with Stefan for the long read model!!!

