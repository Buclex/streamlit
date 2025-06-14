from setuptools import setup, find_packages

setup(
    name="edu_pad",
    version="0.0.1",
    author="Andres Callejas",
    author_email="andres.callejas@iudigital.edu.co",
    description="ETL para análisis de datos del dólar",
    py_modules=["actividad1", "actividad2"],
    install_requires=[

        
        "streamlit-ace",
        "streamlit-discourse",
        "streamlit-disqus",
        "streamlit-elements",
        "streamlit-pandas-profiling",
        "streamlit-player",
        "streamlit-quill",
        "streamlit",
        "pandas",
        "openpyxl",
        "requests",
        "beautifulsoup4",
        "altair>=5.0.0"
    ]
)