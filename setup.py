from setuptools import setup

setup(name='perceptual_similarity',
      version='1.0',
      description='perceptual similarity code from '
                  'https://github.com/richzhang/PerceptualSimilarity made '
                  'installable.',
      author='Zhang, Richard and Isola, Phillip and Efros, Alexei A and '
             'Shechtman, Eli and Wang, Oliver',
      packages=['perceptual_similarity'],
      install_requires=[
            'torch>=0.4.0',
            'torchvision>=0.2.1',
            'numpy>=1.14.3',
            'scipy>=1.0.1',
            'scikit-image>=0.13.0',
            'matplotlib>=1.5.1'
          ],
      zip_safe=False)
