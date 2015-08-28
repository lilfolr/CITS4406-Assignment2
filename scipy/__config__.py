# This file is generated by /home/jordan/Desktop/CITS3200/CITS4406-Assignment2/scipy-0.16.0/setup.py
# It contains system_info results at the time of building this package.
__all__ = ["get_info","show"]

blas_mkl_info={}
atlas_3_10_blas_info={}
mkl_info={}
openblas_info={}
openblas_lapack_info={}
lapack_opt_info={'define_macros': [('NO_ATLAS_INFO', 1)], 'libraries': ['lapack', 'blas'], 'library_dirs': ['/usr/lib'], 'language': 'f77'}
blas_opt_info={'define_macros': [('NO_ATLAS_INFO', 1)], 'libraries': ['blas'], 'library_dirs': ['/usr/lib'], 'language': 'f77'}
atlas_blas_info={}
atlas_3_10_info={}
lapack_mkl_info={}
atlas_3_10_threads_info={}
atlas_info={}
atlas_3_10_blas_threads_info={}
lapack_info={'language': 'f77', 'libraries': ['lapack'], 'library_dirs': ['/usr/lib']}
blas_info={'language': 'f77', 'libraries': ['blas'], 'library_dirs': ['/usr/lib']}
atlas_blas_threads_info={}
atlas_threads_info={}

def get_info(name):
    g = globals()
    return g.get(name, g.get(name + "_info", {}))

def show():
    for name,info_dict in globals().items():
        if name[0] == "_" or type(info_dict) is not type({}): continue
        print(name + ":")
        if not info_dict:
            print("  NOT AVAILABLE")
        for k,v in info_dict.items():
            v = str(v)
            if k == "sources" and len(v) > 200:
                v = v[:60] + " ...\n... " + v[-60:]
            print("    %s = %s" % (k,v))
    