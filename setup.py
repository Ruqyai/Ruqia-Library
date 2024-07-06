
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="ruqia",  # Required
    version="0.0.23",  # Required
    description="Arabic NLP",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url="https://github.com/Ruqyai/Ruqia-Library",  # Optional
    author="Ruqiya Bin Safi",  # Optional
    author_email="",  # Optional
    classifiers=[  # Optional
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="Arabic, NLP, development",  # Optional
    package_dir={"": "src"},  # Optional
    packages=find_packages(where="src"),  # Required
    python_requires=">=3.7, <4",
    install_requires=["peppercorn"],  # Optional
    extras_require={  # Optional
        "dev": ["check-manifest"],
        "test": ["coverage"],
    },
    package_data={  # Optional
        "ruqiya": ["package_data.dat"],
    },
    data_files=[("my_data", ["data/data_file"])],  # Optional
    entry_points={  # Optional
        "console_scripts": [
            "ruqiya=ruqiya:main",
        ],
    },
    project_urls={  # Optional
        "Bug Reports": "https://github.com/Ruqyai/Ruqia-Library/issues",
        "Become a sponsor": "https://github.com/sponsors/Ruqyai",
        "Source": "https://github.com/Ruqyai/Ruqia-Library",
    },
)
