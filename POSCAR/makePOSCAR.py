
import pandas as pd
import os
from ase.db import connect
from pymatgen.io.ase import AseAtomsAdaptor
from pymatgen.io.vasp import Poscar

ase_db_path = '/home/ucl/modl/hayu/Modelrank/binary_phase_diagram_test/final_db.db'

output_directory = '/home/ucl/modl/hayu/git_repos/POSCAR'

os.makedirs(output_directory, exist_ok=True)

db = connect(ase_db_path)

for row in db.select():
    mp_id = row.get('mp_id')
    if mp_id:
        atoms = row.toatoms()
        structure = AseAtomsAdaptor().get_structure(atoms)
        poscar = Poscar(structure)
        poscar.write_file(os.path.join(output_directory, f'POSCAR_{mp_id}'))

print("POSCAR file generation completed.")

