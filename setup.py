import setuptools
setuptools.setup(
    name='pac-maker',
    py_modules=['pac_maker'],
    entry_points={'console_scripts': ['pac-maker = pac_maker:_main']}
)
