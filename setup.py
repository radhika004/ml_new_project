# for package building for Ml application anyone can download and use 
from setuptools import find_packages,setup
from typing import List

HYPEN_E_Dot = '-e .'
def get_requirements(file_path:str)->list[str]:
  """this function will return the list of requirements"""
  requirements=[]
  with open(file_path) as file_obj:
    requirements=file_obj.readlines()
    requirements = [req.replace("\n", "") for req in requirements]
    # [req.replace("\n","")for req in requirements]
    
    if HYPEN_E_Dot in requirements:
      requirements.remove(HYPEN_E_Dot)
      
  return requirements 
  

setup(
  name = "ML Project",
  version ='0.0.1',
  author = "radhika",
  author_email = "radhikachare2004@gmail.com",
  packages = find_packages(),
  install_requires=get_requirements('requirements.txt')
  
)
