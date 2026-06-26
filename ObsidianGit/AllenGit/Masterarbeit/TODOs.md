- 等tnt上的dmr跑完，跑通methylbert
- 等luis上的数据跑完，把lyzr的data preparation跑了，然后完成lyzr的部分

### LUIS

|       | fastq | bam               | cov      |
| ----- | ----- | ----------------- | -------- |
| CC    | -     | 30                | done     |
| DLBCL | -     | 20                | done     |
| GC    | 600/2 | 150 in processing | queueing |
| PC    | 38/2  | queueing          | queueing |
### MethylBERT
1. Data pre-processing: multi-cancer-type input
2. Training: /
3. Fine-tuning：classifier


### MethyLYZR
- [x] Training: data pre-processing pipeline script
- [x] Predicting: data input without "score_per_read"
- [ ] 把cov对齐到450k array需要的脚本