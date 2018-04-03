from distutils.core import setup

# get the dependencies and installs
with open('requirements.txt') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]

setup(name='peptide-dashboard',
      version='0.01',
      description='Peptide Dashboard App',
      author='Andrew White',
      packages=['pd_app'],
      package_data={'pd_app': ['data/*.txt']},
      install_requires=install_requires,
      entry_points=
      {
        'console_scripts': ['pd-app=pd_app.app:start']
      }
     )
