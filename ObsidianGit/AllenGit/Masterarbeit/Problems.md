### MethyLYZR
- some samples only matched a few(~3k) probes on 450k array, which leads to a lot of NA in matrix -> filter those samples out
- for kernel.py: only calc mean of the matrix -> NA is fine.
- for weight.py: distance between vectors will be calculated, so the NA is not intolerable
```
# Calculate the pairwise distances using cdist from scipy
dist_centroid_mat = distance.cdist(betas_mean, betas, metric = 'euclidean').T
```
