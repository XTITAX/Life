from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='Life',
    version='1.0',
    author='XTITAX',
    author_email='xtitax@yandex.ru',
    description='Библиотека игры Жизнь',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/XTITAX/Life',
    packages=find_packages(include=['life', 'life.*']),  # исправлено на 'life'
    include_package_data=True,
    install_requires=[
        'numpy',
    ],
    package_data={
        'life': ['examples/*'],  # исправлено на 'life'
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
