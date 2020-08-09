import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name='pytorch-fid',
    version='1.0.0',
    author='Max Seitzer',
    author_email='contact@max-seitzer.de',
    description=('Package for calculating Frechet Inception Distance (FID) '
                 'using PyTorch'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mseitzer/pytorch-fid',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache 2.0 License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'pytorch-fid = pytorch_fid.fid_score:main',
        ],
    },
    install_requires=[
        'numpy',
        'pillow',
        'scipy',
        'torch',
        'torchvision'
    ]
)
