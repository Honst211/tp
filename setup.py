from setuptools import setup

import versioneer

setup(
    name="tp",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
