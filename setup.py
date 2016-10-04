from setuptools import setup, find_packages

setup(
    name="jmbo-faq",
    version="0.0.1",
    description="FAQs App for JMBO",
    # long_description = open("README.rst", "r").read() + open("AUTHORS.rst", "r").read() + open("CHANGELOG.rst", "r").read(),
    author="Praekelt Consulting",
    author_email="dev@praekelt.com",
    license="BSD",
    url="http://github.com/praekelt/jmbo-faq",
    packages = find_packages(),
    install_requires = [
        "django-ckeditor>=4.2.1",
        #"jmbo>=3.0.0", uncomment when released
        "beautifulsoup4",
    ],
    include_package_data=True,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
