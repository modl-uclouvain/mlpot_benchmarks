## License

The data in this repository are licensed under the
[Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/);
see [`LICENSE`](LICENSE).

If you use these data, please cite:

> H. Yu, M. Giantomassi, G. Materzanini, J. Wang and G.-M. Rignanese,
> "Systematic assessment of various universal machine-learning interatomic potentials",
> *Mater. Genome Eng. Adv.* **2**, e58 (2024), https://doi.org/10.1002/mgea.58

### Third-party data

- `entries/entries_mp.json` and the structures in `POSCAR/` and `quinaryPOSCAR/`
  are taken from the [Materials Project](https://materialsproject.org)
  (CC BY 4.0). Please also cite A. Jain *et al.*, *APL Mater.* **1**, 011002 (2013),
  https://doi.org/10.1063/1.4812323.
- `PH_DDB_DATA/`: ABINIT DFPT phonon databases (DDB files) retrieved from the
  Materials Project (CC BY 4.0). Please also cite G. Petretto *et al.*,
  *Sci. Data* **5**, 180065 (2018), https://doi.org/10.1038/sdata.2018.65.

The energies in `entries/entries_{alignn,chgnet,m3gnet}.json` and
`entries/corrected_energy_entries_mace.json` were computed for the paper above
with the corresponding pretrained models.
