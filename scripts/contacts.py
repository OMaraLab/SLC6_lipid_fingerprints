import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import MDAnalysis as mda
from MDAnalysis.analysis.base import AnalysisBase
from MDAnalysis.analysis.distances import capped_distance


class ContactAnalysis(AnalysisBase):
    def __init__(self, u, select="protein", select_other="not protein",
                 cutoff=6, group_by_attr="resnames"):
        super().__init__(u.universe.trajectory)
        self.universe = u.universe
        self.protein = u.select_atoms(select)
        self.group = u.select_atoms(select_other)
        self.cutoff = cutoff
        self.group_by_attr = group_by_attr
        self.ids = getattr(self.group.residues, group_by_attr)
        self.unique_ids = np.unique(self.ids)

    def _prepare(self):
        self.select_string = f"around {self.cutoff} global group selgroupname"
        self.percent_contact = np.zeros((len(self.protein.residues),
                                         len(self.unique_ids)),
                                         dtype=float)

        protein_dct = {r.resindex: i for i, r in enumerate(self.protein.residues)}
        lst = list(self.unique_ids)
        indices = [lst.index(x) for x in self.ids]
        group_dct = {r.resindex: i for r, i in zip(self.group.residues, indices)}
        self.protein_rix = np.array([protein_dct[x] for x in self.protein.resindices])
        self.group_rix = np.array([group_dct[x] for x in self.group.resindices])
        
        # print(self.group_dct)

    
    def _single_frame(self):

        pairs = capped_distance(self.protein.positions, self.group.positions,
                                self.cutoff, box=self.universe.dimensions,
                                return_distances=False)

        prot = self.protein_rix[pairs[:, 0]]
        group = self.group_rix[pairs[:, 1]]

        tmp = np.zeros_like(self.percent_contact)
        tmp[(prot, group)] = 1

        self.percent_contact += tmp

    def _conclude(self):
        self.percent_contact /= self.n_frames