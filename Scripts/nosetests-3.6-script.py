#!E:/python/anaconda\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'nose==1.3.7','console_scripts','nosetests-3.6'
__requires__ = 'nose==1.3.7'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('nose==1.3.7', 'console_scripts', 'nosetests-3.6')()
    )
