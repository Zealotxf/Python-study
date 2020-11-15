try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
          'description': '龙珠',
          'author': 'Zealotxf',
          'url': 'URL to get it at.',
          'download_url': 'Where to download it.',
          'author_email': '2353612220@qq.com',
          'version': '0.1',
          'install_requires': ['nose'],
          'packages': ['NAME'],
          'scripts': [],
          'name': 'projectname'
}

setup(**config)
