from setuptools import setup
from setuptools import find_packages


setup(name='pyramid_taobao',
      version='0.1',
      description='Pyramid configuration with OpenTaobao-API integration',
      author='Eric Lo',
      author_email='lxneng@gmail.com',
      url='https://github.com/lxneng/pyramid_taobao',
      license='BSD',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=['requests'])
