from setuptools import setup, find_packages


setup(
    name='ML-projects-1',
    version='0.1',
    author='Raji puliyadi',
    author_email="rpuliyadi@gmail.com"
    description='A collection of machine learning projects',
    packages=find_packages(),    
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'tensorflow',  # or 'torch' if using PyTorch
    ],
    