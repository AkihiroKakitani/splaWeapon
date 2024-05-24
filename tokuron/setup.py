from setuptools import setup, find_packages

setup(
    name='weapon-selector1',
    version='0.1',
    py_modules=['weapon-selector1'],
    install_requires=[],
    url='https://github.com/AkihiroKakitani/splaWeapon.git',  # リポジトリのURL
    author='kakitaniakihiro',
    author_email='s2222010@stu.musashino-u.ac.jp',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
