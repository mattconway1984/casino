import setuptools

setuptools.setup(
    name="casino",
    version="0.0.0",
    packages=setuptools.find_packages(),
    scripts=["casino/roller"],
    entry_points = {
        'console_scripts': [
            "roll=casino.dice:roll",
            "roll-many=casino.dice:cmd_roll",
        ],
    }
)
