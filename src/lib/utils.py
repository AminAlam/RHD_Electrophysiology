import subprocess
import os
import sys
import re

def get_matlab_engine():
    """Installs MATLAB engine for Python
    input:
    output:
        eng: MATLAB engine for Python
    """
    matlab_installation_url = 'https://uk.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html'
    try:
        import matlab.engine
    except:
        Warning('MATLAB engine for Python not installed. Trying to install...')
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'matlabengine'])
        except:
            raise ImportError(f'MATLAB engine for Python not installed. Please install MATLAB engine for Python from {matlab_installation_url}')        
    
    return matlab.engine.start_matlab()

def sort_file_names(file_names):
    """Sorts file names in ascending order
    input:
        file_names: list of file names - type: list
    output:
        file_names: sorted list of file names - type: list
    """
    file_names.sort(key=lambda f: int(re.sub('\D', '', f)))
    return file_names