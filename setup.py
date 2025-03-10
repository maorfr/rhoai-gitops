from setuptools import find_packages, setup

setup(
    name="gitops",
    version="0.1.0",
    description="Red Hat OpenShift AI GitOps",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Red Hat OpenShift AI DevOps team",
    author_email="openshift-ai-devops@redhat.com",
    url="https://github.com/red-hat-data-services/rhoai-gitops",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
    install_requires=[
        "PyGithub",
        "ruamel.yaml",
    ],
)
