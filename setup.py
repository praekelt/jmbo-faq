from setuptools import setup, find_packages

def construct_long_description():
    long_description = ""
    for file_name in ["README.rst", "AUTHORS.rst", "CHANGELOG.rst"]:
        try:
            file_buffer = open(file_name, "r")
            long_description += file_buffer.read()
        except IOError:
            pass
        finally:
            file_buffer.close()
    return long_description


setup(
    name="jmbo-faq",
    version="0.1.0",
    description="FAQs App for JMBO",
    long_description=construct_long_description(),
    author="Praekelt Consulting",
    author_email="dev@praekelt.com",
    license="BSD",
    url="http://github.com/praekelt/jmbo-faq",
    packages = find_packages(),
    install_requires = [
        "django-simplemde",
        #"jmbo>=3.0.0", uncomment when released
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
