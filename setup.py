from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="HAED-IDS-Framework",
    version="1.0.0",
    author="Rittamar22",
    description="Hybrid Anomaly-Ensemble Detection Framework for Network Intrusion Detection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rittamar22-cmd/HAED-IDS-Framework",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Security",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
)