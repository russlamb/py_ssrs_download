from setuptools import setup

setup(name="py_ssrs_download",
		version='0.0.1',
		description='download files from SSRS using NTLM authentication.',
		url='http://github.com/russlamb/py_ssrs_download',
		author='Russ Lamb',
		author_email='revoltingrobot@gmail.com',
		license='MIT',
		py_modules=['download_ssrs','encode_ssrs_url','date_gen'],
		zip_safe=False,
		install_requires=['python_ntlm','requests','requests_ntlm','calendar'])