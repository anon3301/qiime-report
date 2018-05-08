# qiime-report


# Joining Reads: joined_paired_ends.pbs

Pair together forward and reverse reads from raw sequencing data


# Split libraries: split_libraries.pbs	

Demultiplexing read pairs into reads from each of the 30 samples

# Picking OTUs: deNovo_OTU.pbs

Reads are clustered together into so called “organismal-taxonomic-units” (OTUs). 
These are analogous to species, but grouped pragmatically through sequence similarity
Clustering tool used was UCLUST, and the OTU picking strategy “de-novo” picking.
De-novo OTU picking is an unbiased method that clusters all reads into OTUs.
Result is a "BIOM table", a table of all OTUs in the samples.

 
# Novo_core_diversity_analyses.py   

Main analyses of the OTU table performed by Qiime1, including alpha diversity, beta diversity and taxa summaries.
  

# Creating essential OTU table: Core_microbiome.py

Filtering the original OTU table to leave only the essential OTUs found across the highest number of samples.


# CoreMicro_HeatMap

Create heatmap of all OTUs against all samples, intense colour signifies higher relative abundance.

# Performing core diversity analyses on the essential OTUs: CoreDiv_CoreMicro.py

Core diversity analyses but now on the OTU table produced by Core_microbiome.py

# Compare_categories_Full_set_Temp.py

Statistical analysis of correlation between OTU and composition and soil characteristics between samples on the full set of OTUs
Performed for K, N, P and pH

# Compare_categories_CoreMicro Temp.py

Statistical analysis of correlation between OTU and composition and soil characteristics between samples on the essential OTUs


# Group_significance.py

Statistical analysis of correlation between individual OTUs and soil characteristics, performed on the essential OTU table
Performed for K, N, P, pH, and team.


