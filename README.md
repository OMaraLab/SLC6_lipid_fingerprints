# SLC6_lipid_fingerprints

MARTINI models used to investigate the lipid fingerprints of
SLC6 transporters in both a complex neuronal plasma membrane and a
simple POPC/CHOL membrane are in data/.

The neuronal plasma membrane is based on:

Ingólfsson, H. I.; Carpenter, T. S.; Bhatia, H.; Bremer, P. T.; Marrink, S. J.; Lightstone, F. C. Computational Lipidomics of the Neuronal Plasma Membrane. Biophys. J. 2017, 113 (10), 2271–2280.

Parameters are available in martini.ff/

Scripts to run the analyses to obtain the area per lipid (mapl),
lipid depletion-enrichment index (mdei),
and lipid flop-flop (mflipflop) are in the scripts folder.

**Please cite the below paper if you use any code from this project (including in the branch linked below):**

[Wilson, K. A.; Wang, L.; Lin, Y. C.; O’Mara, M. L. *Investigating the Lipid Fingerprint of SLC6 Neurotransmitter Transporters: A Comparison of DDAT, HDAT, HSERT, and GlyT2.* BBA Advances 2021, 1, 100010. https://doi.org/10.1016/j.bbadva.2021.100010.](https://doi.org/10.1016/j.bbadva.2021.100010)


Please see the [slc6-transporters](https://github.com/lilyminium/mdanalysis/tree/slc6-transporters/package/MDAnalysis/analysis/leaflets) branch of Lily Wang's MDAnalysis repository
for the actual implementation of each analyses.

All material is provided under an MIT license. Please cite the above references
if you use this material in published work.
