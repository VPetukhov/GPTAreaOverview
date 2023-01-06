# Attempt 1

# Improving article title by the content from its abstract

- Title. Cascade Forest-Based Model for Prediction of RNA Velocity
- Abstract. In this paper, we develop a cascade forest model to predict RNA velocity. Compared with other popular ensemble classifiers, such as XGBoost, RandomForest, LightGBM, NGBoost, and TabNet, it performs better in predicting RNA velocity. The investigation of RNA velocity is a new topic in the study of cellular dynamics using single-cell RNA sequencing data.
- Improved title. Improving prediction of RNA velocuty using Cascade Forest-Based models

===

- Title. GSEApy: a comprehensive package for performing gene set enrichment analysis in Python.
- Abstract. The new GSEApy with Rust extension is deposited in PyPI: https://pypi.org/project/gseapy/. The Enrichr API enables GSEApy to perform over-representation analysis for an input gene list. However, the currently available tools used to perform GSEA have a limited ability to analyze large datasets, which is particularly problematic for the analysis of single-cell data.
- Improved title. A package for high-performance gene set enrichment analysis for large datasets

===

- Title. Comparison of cell type distribution between single-cell and single-nucleus RNA sequencing: enrichment of adherent cell types in single-nucleus RNA sequencing.
- Abstract. Single-cell ribonucleic acid (RNA) sequencing (scRNA-seq) is an effective technique for estimating the cellular composition and transcriptional profiles of individual cells from fresh tissue. Single-nucleus RNA sequencing (snRNA-seq) is necessary to perform this type of analysis in frozen or difficult-to-dissociate tissues, which cannot be subjected to scRNA-seq. This difference in the state of tissues leads to variation in cell-type distributions among each platform. To identify the characteristics of these methods and their differences, scRNA-seq and snRNA-seq were performed in parallel for colon and liver tissues. The two platforms revealed similar diversity but different proportions of cell types in matched tissues. The proportions of epithelial cells in the colon and hepatocytes in the liver were relatively high in snRNA-seq and that of immune cells was relatively high in scRNA-seq. This difference could be explained by variations in the expression scores of adhesion genes due to the disruption of the cytoplasmic contents during scRNA-seq. The enrichment of epithelial cells in the colon resulted in a discrepancy in the differentiation of epithelial cells. This enrichment was also well matched with the images of hematoxylin and eosin staining and the estimated distribution of cell types in bulk RNA sequencing. These results showed that snRNA-seq could be used to analyze tissues that cannot be subjected to scRNA-seq and provides more information in specific cell type analysis.
- Improved title. Examining differences in cell type composition between single-cell and single-nucleus RNA sequencing protocols

===

- Title. Jointly defining cell types from multiple single-cell datasets using LIGER.
- Abstract. High-throughput single-cell sequencing technologies hold tremendous potential for defining cell types in an unbiased fashion using gene expression and epigenomic state. A key challenge in realizing this potential is integrating single-cell datasets from multiple protocols, biological contexts, and data modalities into a joint definition of cellular identity. We previously developed an approach, called linked inference of genomic experimental relationships (LIGER), that uses integrative nonnegative matrix factorization to address this challenge. Here, we provide a step-by-step protocol for using LIGER to jointly define cell types from multiple single-cell datasets. The main stages of the protocol are data preprocessing and normalization, joint factorization, quantile normalization and joint clustering, and visualization. We describe how to jointly define cell types from single-cell RNA-seq (scRNA-seq) and single-nucleus ATAC-seq (snATAC-seq) data, but similar steps apply across a wide range of other settings and data types, including cross-species analysis, single-nucleus DNA methylation, and spatial transcriptomics. Our protocol contains examples of expected results, describes common pitfalls, and relies only on our freely available, open-source R implementation of LIGER. We also provide R Markdown tutorials showing the outputs from each individual code segment. The analysis process can be performed in 1-4 h, depending on dataset size, and assumes no specialized bioinformatics training.
- Improved title. Uncovering joint cell types from multiple single-cell datasets using LIGER

===

- Title. GeoWaVe: Geometric median clustering with weighted voting for ensemble clustering of cytometry data.
- Abstract. Clustering is an unsupervised method for identifying structure in unlabelled data. In the context of cytometry, it is typically used to categorise cells into subpopulations of similar phenotypes. However, clustering is greatly dependent on hyperparameters and the data to which it is applied as each algorithm makes different assumptions and generates a different 'view' of the dataset. As such, the choice of clustering algorithm can significantly influence results, and there is often not one preferred method but different insights to be obtained from different methods. To overcome these limitations, consensus approaches are needed that directly address the effect of competing algorithms. To the best of our knowledge, consensus clustering algorithms designed specifically for the analysis of cytometry data are lacking. We present a novel ensemble clustering methodology based on geometric median clustering with weighted voting (GeoWaVe). Compared to graph ensemble clustering methods that have gained popularity in scRNA-seq analysis, GeoWaVe performed favourably on different sets of high-dimensional mass and flow cytometry data. Our findings provide proof of concept for the power of consensus methods to make the analysis, visualisation and interpretation of cytometry data more robust and reproducible. The wide availability of ensemble clustering methods is likely to have a profound impact on our understanding of cellular responses, clinical conditions, and therapeutic and diagnostic options. GeoWaVe is available as part of the CytoCluster package https://github.com/burtonrj/CytoCluster and published on the Python Package Index https://pypi.org/project/cytocluster. Benchmarking data described are available from https://doi.org/10.5281/zenodo.7134723. Supplementary data are available at Bioinformatics online.
- Improved title. GeoWaVe: A consensus clustering approach for robust and reproducible analysis of cytometry data

===

- Title. Multimodal T Cell Analysis with CoNGA.
- Abstract. Advances in single-cell technologies have made it possible to simultaneously quantify gene expression and immune receptor sequence across thousands of individual T or B cells in a single experiment. Data from such experiments are advancing our understanding of the relationship between adaptive immune receptor sequence and transcriptional profile. We recently reported a software tool, CoNGA, specifically developed to detect correlation between receptor sequence and transcriptional profile. Here we describe in detail how CoNGA can be applied to analyze a large and diverse T cell dataset featuring multiple donors and batch annotations. Our workflow illustrates new analysis modes for the detection of TCR sequence convergence into similarity clusters and of matches to literature-derived TCR databases, as well as processing of gamma-delta T cells.
- Improved title. Exploring the relationship between T cell receptor sequence and transcriptional profile using CoNGA


## Attempt 2

*It works even with Curie.*

- Title. Multimodal T Cell Analysis with CoNGA.
- Abstract. Advances in single-cell technologies have made it possible to simultaneously quantify gene expression and immune receptor sequence across thousands of individual T or B cells in a single experiment. Data from such experiments are advancing our understanding of the relationship between adaptive immune receptor sequence and transcriptional profile. We recently reported a software tool, CoNGA, specifically developed to detect correlation between receptor sequence and transcriptional profile. Here we describe in detail how CoNGA can be applied to analyze a large and diverse T cell dataset featuring multiple donors and batch annotations. Our workflow illustrates new analysis modes for the detection of TCR sequence convergence into similarity clusters and of matches to literature-derived TCR databases, as well as processing of gamma-delta T cells.
- Detailed title. Detecting correlation between T cell receptor sequence and transcriptional profile using CoNGA across multiple donors and batches.

===

- Title. Metric learning with triplet network.
- Abstract. Many biological applications are essentially pairwise comparison problems, such as evolutionary relationships on genomic sequences, contigs binning on metagenomic data, cell type identification on gene expression profiles of single-cells, etc. To make pair-wise comparison, it is necessary to adopt suitable dissimilarity metric. However, not all the metrics can be fully adapted to all possible biological applications. It is necessary to employ metric learning based on data adaptive to the application of interest. Therefore, in this study, we proposed MEtric Learning with Triplet network (MELT), which learns a nonlinear mapping from original space to the embedding space in order to keep similar data closer and dissimilar data far apart. MELT is a weakly supervised and data-driven comparison framework that offers more adaptive and accurate dissimilarity learned in the absence of the label information when the supervised methods are not applicable. We applied MELT in three typical applications of genomic data comparison, including hierarchical genomic sequences, longitudinal microbiome samples and longitudinal single-cell gene expression profiles, which have no distinctive grouping information. In the experiments, MELT demonstrated its empirical utility in comparison to many widely used dissimilarity metrics. And MELT is expected to accommodate a more extensive set of applications in large-scale genomic comparisons. MELT is available at https://github.com/Ying-Lab/MELT.
- Detailed title.


## Attempt 3

*Insert mode. Edit works visibly worse. In completion mode Curie usually repeats the title on my tests.*

Adding details to the title by information from the abstract.

- Title. Multimodal T Cell Analysis with CoNGA.
- Expanded title. Detecting correlation between T cell receptor sequence and transcriptional profile using CoNGA across multiple donors and batches.
- Abstract. Advances in single-cell technologies have made it possible to simultaneously quantify gene expression and immune receptor sequence across thousands of individual T or B cells in a single experiment. Data from such experiments are advancing our understanding of the relationship between adaptive immune receptor sequence and transcriptional profile. We recently reported a software tool, CoNGA, specifically developed to detect correlation between receptor sequence and transcriptional profile. Here we describe in detail how CoNGA can be applied to analyze a large and diverse T cell dataset featuring multiple donors and batch annotations. Our workflow illustrates new analysis modes for the detection of TCR sequence convergence into similarity clusters and of matches to literature-derived TCR databases, as well as processing of gamma-delta T cells.

===

- Title. Metacell-2: a divide-and-conquer metacell algorithm for scalable scRNA-seq analysis.
- Expanded title. Decomposition of datasets into small and cohesive groups (metacells) for scalable analysis, outlier detection and rare cell type identification
- Abstract. Scaling scRNA-seq to profile millions of cells is crucial for constructing high-resolution maps of transcriptional manifolds. Current analysis strategies, in particular dimensionality reduction and two-phase clustering, offer only limited scaling and sensitivity to define such manifolds. We introduce Metacell-2, a recursive divide-and-conquer algorithm allowing efficient decomposition of scRNA-seq datasets of any size into small and cohesive groups of cells called metacells. Metacell-2 improves outlier cell detection and rare cell type identification, as shown with human bone marrow cell atlas and mouse embryonic data. Metacell-2 is implemented over the scanpy framework for easy integration in any analysis pipeline.

===

- Title. Characterizing the replicability of cell types defined by single cell RNA-sequencing data using MetaNeighbor.
- Expanded title. [INSERT]
- Abstract. Single-cell RNA-sequencing (scRNA-seq) technology provides a new avenue to discover and characterize cell types; however, the experiment-specific technical biases and analytic variability inherent to current pipelines may undermine its replicability. Meta-analysis is further hampered by the use of ad hoc naming conventions. Here we demonstrate our replication framework, MetaNeighbor, that quantifies the degree to which cell types replicate across datasets, and enables rapid identification of clusters with high similarity. We first measure the replicability of neuronal identity, comparing results across eight technically and biologically diverse datasets to define best practices for more complex assessments. We then apply this to novel interneuron subtypes, finding that 24/45 subtypes have evidence of replication, which enables the identification of robust candidate marker genes. Across tasks we find that large sets of variably expressed genes can identify replicable cell types with high accuracy, suggesting a general route forward for large-scale evaluation of scRNA-seq data.

### Other problematic examples

- Title. MATCHER: manifold alignment reveals correspondence between single cell transcriptome and epigenome dynamics.
- Expanded title. [INSERT]
- Abstract. Single cell experimental techniques reveal transcriptomic and epigenetic heterogeneity among cells, but how these are related is unclear. We present MATCHER, an approach for integrating multiple types of single cell measurements. MATCHER uses manifold alignment to infer single cell multi-omic profiles from transcriptomic and epigenetic measurements performed on different cells of the same type. Using scM&T-seq and sc-GEM data, we confirm that MATCHER accurately predicts true single cell correlations between DNA methylation and gene expression without using known cell correspondences. MATCHER also reveals new insights into the dynamic interplay between the transcriptome and epigenome in single embryonic stem cells and induced pluripotent stem cells.


===

- Title. RNA splicing programs define tissue compartments and cell types at single-cell resolution.
- Expanded title. [INSERT]
- Abstract. The extent splicing is regulated at single-cell resolution has remained controversial due to both available data and methods to interpret it. We apply the SpliZ, a new statistical approach, to detect cell-type-specific splicing in >110K cells from 12 human tissues. Using 10X Chromium data for discovery, 9.1% of genes with computable SpliZ scores are cell-type-specifically spliced, including ubiquitously expressed genes

===


- Title. CITEMO
- Expanded title. [INSERT]
- Abstract. Simultaneous measurement of multiple modalities in single-cell analysis, represented by CITE-seq, is a promising approach to link transcriptional changes to cellular phenotype and function, requiring new computational methods to define cellular subtypes and states based on multiple data types. Here, we design a flexible single-cell multimodal analysis framework, called CITEMO, to integrate the transcriptome and antibody-derived tags (ADT) data to capture cell heterogeneity from the multi omics perspective. CITEMO uses Principal Component Analysis (PCA) to obtain a low-dimensional representation of the transcriptome and ADT, respectively, and then employs PCA again to integrate these low-dimensional multimodal data for downstream analysis. To investigate the effectiveness of the CITEMO framework, we apply CITEMO to analyse the cell subtypes of Cord Blood Mononuclear Cells (CBMC) samples. Results show that the CITEMO framework can comprehensively analyse single-cell multimodal samples and accurately identify cell subtypes. Besides, we find some specific immune cells that co-express multiple ADT markers. To better describe the co-expression phenomenon, we introduce the co-expression entropy to measure the heterogeneous distribution of the ADT combinations. To further validate the robustness of the CITEMO framework, we analyse Human Bone Marrow Cell (HBMC) samples and identify different states of the same cell type. CITEMO has an excellent performance in identifying cell subtypes and states for multimodal omics data. We suggest that the flexible design idea of CITEMO can be an inspiration for other single-cell multimodal tasks. The complete source code and dataset of the CITEMO framework can be obtained from https://github.com/studentiz/CITEMO.