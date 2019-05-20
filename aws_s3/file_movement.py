from os.path import join
from filecmp import dircmp

L_dir = 'C:\temp1'
R_dir = 'C:\temp2'

def find_uncommon(L_dir, R_dir):
    dcmp = dircmp(L_dir, R_dir)
    # L_only = [join(L_dir, f) for f in dcmp.left_only]
    # R_only = [join(R_dir, f) for f in dcmp.right_only]
    # for sub_dir in dcmp.common_dirs:
    #     new_L, new_R = find_uncommon(join(L_dir, sub_dir), join(R_dir, sub_dir))
    #     L_only.extend(new_L)
    #     R_only.extend(new_R)
    # return L_only, R_only