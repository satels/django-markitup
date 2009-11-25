from setuptools import setup
import subprocess
import os.path

try:
    # don't get confused if our sdist is unzipped in a subdir of some 
    # other hg repo
    if os.path.isdir('.hg'):
        p = subprocess.Popen(['hg', 'parents', r'--template={rev}\n'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if not p.returncode:
            fh = open('HGREV', 'w')
            fh.write(p.communicate()[0].splitlines()[0])
            fh.close()
except (OSError, IndexError):
    pass
    
try:
    hgrev = open('HGREV').read()
except IOError:
    hgrev = ''
    
long_description = (open('README.txt').read() + 
                    open('CHANGES.txt').read() +
                    open('TODO.txt').read())

setup(
    name='django-markitup',
    version='0.5.2',
    description='Markup handling for Django using the MarkItUp! universal markup editor',
    long_description=long_description,
    author='Carl Meyer',
    author_email='carl@dirtcircle.com',
    url='http://bitbucket.org/carljm/django-markitup/',
    packages=['markitup', 'markitup.templatetags'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    test_suite='tests.runtests.runtests',
    package_data={'markitup': ['templates/markitup/*.html',
                               'media/markitup/*.*',
                               'media/markitup/sets/*/*.*',
                               'media/markitup/sets/*/images/*.png',
                               'media/markitup/skins/*/*.*',
                               'media/markitup/skins/*/images/*.png',
                               'media/markitup/templates/*.*']}
)
