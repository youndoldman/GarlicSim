# Copyright 2009-2011 Ram Rachum.
# This program is distributed under the LGPL2.1 license.

'''
Defines utilities for testing GarlicSim from zip.

Used by `run_tests.py` in the GarlicSim repo root.
'''

import sys
import os.path


frozen = getattr(sys, 'frozen', None)
our_path = os.path.realpath(os.path.split(__file__)[0])


def prepare_zip_testing(package_names):
    '''Zip all GarlicSim modules and import them for testing.'''
    
    sys.stdout.write('Preparing to zip GarlicSim packages, and then run tests '
                     'with GarlicSim imported from zip files.\n')
    
    assert not frozen
    
    result = os.system(
        '"%s"' % os.path.realpath(os.path.join(our_path, 'make_zip.py'))
    )
    
    if result != 0:
        exit(result)
        
    for package_name in package_names:
        assert not exists(package_name)
        assert package_name not in sys.modules

    sys.stdout.write('Importing all GarlicSim packages from zip files... ')
        
    for i, package_name in enumerate(package_names):
        zip_file = os.path.realpath(
            os.path.join(our_path, 'build', (str(i) + '.zip'))
        )
        assert zip_file not in sys.path
        sys.path.append(zip_file)
        package = __import__(package_name)
        assert '.zip' in package.__file__
    
    sys.stdout.write('Done.\n')
    
    
def ensure_zip_testing_was_legit(package_names):
    '''
    Ensure GarlicSim packages were indeed used from zip.
    
    This is used only in `--from-zip` testing, to ensure that the GarlicSim
    packages weren't used from the source folders accidentally.
    '''
    sys.stdout.write('Confirming all GarlicSim packages were used from zip '
                     'files... ')
    for i, package_name in enumerate(package_names):
        assert package_name in sys.modules
        package = sys.modules[package_name]
        assert '.zip' in package.__file__
        
        raw_module_names = \
            [module_name for module_name in sys.modules.keys() if
             module_name.split('.')[0] == package_name]
        
        # Filtering out module names that map to `None`, because of a bug,
        # probably in `zipimport`, which litters `sys.modules` with
        # non-sense modules:
        
        module_names = [module_name for module_name in raw_module_names if
                        sys.modules[module_name] is not None]
        
        module_paths = [sys.modules[module_name].__file__ for
                        module_name in module_names]
        
        zip_file_name = str(i) + '.zip'
        snippet_from_real_folder_path = \
            os.path.sep.join((package_name, package_name))
        for module_path in module_paths:
            assert zip_file_name in module_path
            assert snippet_from_real_folder_path not in module_path
    sys.stdout.write('Done.\n')