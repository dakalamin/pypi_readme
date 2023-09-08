import setuptools


with open('README.md', 'r', encoding='utf-8') as readme_file:
    DESCRIPTION = readme_file.read()

setuptools.setup(
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown'
)
