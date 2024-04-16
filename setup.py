# to set src as local area where we will make our (constructor file )imports from to do that we do below which will search the whole folder and then decide the one which is supposed to be local    

# here src - local
from setuptools import find_packages, setup

setup(
    name = 'Medical Chatbot',
    version= '0.0.0',
    author= 'nathan pimenta',
    author_email= 'n.pimenta2004@gmail.com',
    packages= find_packages(),
    install_requires = []

)  