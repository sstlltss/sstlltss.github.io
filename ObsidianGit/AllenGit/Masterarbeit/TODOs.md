# TODOs

- [ ] run methylbert after dmrs finished
- [ ] finish data preparation of LYZR and complete LYZR when data on LUIS is prepared

### LUIS

|       | fastq | bam      | cov      |
| ----- | ----- | -------- | -------- |
| CC    | -     | 30       | all done |
| DLBCL | -     | 20       | all done |
| GC    | 600/2 | 71       | 71 done  |
| PC    | 38/2  | queueing | queueing |
### MethylBERT
- [ ] Data pre-processing: multi-cancer-type input -> need to test
- [ ] Fine-tuning: classifier -> need to test

### MethyLYZR
- [x] Training: data pre-processing pipeline script
- [x] Predicting: data input without "score_per_read"
- [ ] script to "align" position of .cov to 450k array
- [ ] re-training and run