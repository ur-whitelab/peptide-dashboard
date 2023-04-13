Peptide Dashboard
=====

![concept](https://user-images.githubusercontent.com/51170839/231787783-91f143fe-2035-4e89-bf09-bd9ffda0260d.png)


We present three deep learning sequence-based prediction models for peptide properties including hemolysis, solubility, and resistance to nonspecific interactions that achieve comparable results to the state-of-the-art models. Our sequence-based solubility predictor, MahLooL, outperforms the current state-of-the-art methods for short peptides. These models are implemented as a static website without the use of a dedicated server or cloud computing. Web-based models like this allow for accessible and effective reproducibility. Most existing approaches rely on third-party servers that typically require upkeep and maintenance. Our predictive models do not require servers, require no installation of dependencies, and work across a range of devices. The specific architecture is bidirectional recurrent neural networks. This serverless approach is a demonstration of edge machine learning that removes the dependence on cloud providers. 

Web-app: [peptide.bio](https://peptide.bio)

## CLI Implementation

Check out [this notebook](https://github.com/ur-whitelab/peptide-dashboard/blob/master/examples/Quick_start.ipynb) for the CLI implementation of our trained models.

## Citation

[See paper](https://pubs.acs.org/doi/10.1021/acs.jcim.2c01317) and the citation:

```bibtex
@article{doi:10.1021/acs.jcim.2c01317,
author = {Ansari, Mehrad and White, Andrew D.},
title = {Serverless Prediction of Peptide Properties with Recurrent Neural Networks},
journal = {Journal of Chemical Information and Modeling},
volume = {0},
number = {0},
pages = {null},
year = {0},
doi = {10.1021/acs.jcim.2c01317},
    note ={PMID: 37010950},

URL = { 
        https://doi.org/10.1021/acs.jcim.2c01317
    
},
eprint = { 
        https://doi.org/10.1021/acs.jcim.2c01317
    
}

}
```
