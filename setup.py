from setuptools import setup, find_packages

hypen_e_dot = '-e .'

def get_requirements(file_path:str)-> list[str]:
    """Gets requirements from requirements.txt
    Args:
        file_path (str): takes file path as string
    Returns:
        list[str]: returns a list of strings
    """
    requirements=[]
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [r.replace('\n','') for r in requirements]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)

    return requirements
        

    

setup(
    name="ML Project",
    version="0.0.1",
    author="Ayush Sai",
    author_email="ayxshsai@gmail.com",
    description="A machine learning project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Ayxsh03/ML-Projects",
    packages=find_packages(),
    install_requires=[get_requirements('requirements.txt')],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)