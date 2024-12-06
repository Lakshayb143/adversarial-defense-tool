from setuptools import setup
from setuptools_rust import RustExtension

setup(
    name="adversarial_defense",  # Use underscore in Python package
    version="0.1",
    rust_extensions=[RustExtension("adversarial_defense.adversarial_defense", "Cargo.toml")],  # Match the Python package here
    packages=["adversarial_defense"],
    install_requires=["numpy"],  # Add runtime dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Rust",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
)
