########################################
# ->         Smoke Root             <- #
# ->                                <- #
# ->          SCAN SQLi             <- #
# ->          DEVELOPED             <- #
# ->             IN                 <- #
# ->           PYTHON               <- #
# ->                                <- #
# ->       DATE: 08/21/2021         <- #
########################################

import requests
import re

url = '' #LINK EX: http(s)://www.google.com.br/artists.php?artist=2

padrao = re.search(r'([\w:/\._-]+\?[\w_-]+=)([\w_-]+)', url)

INJECTION = padrao.groups()[0] + '\''

print INJECTION

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.103 Safari/537.36'}

req = requests.get(INJECTION, headers=header)

html = req.text

if 'mysql_fetch_array()' in html:
    print 'VULNERABLE'
else:
    print 'NOT VULNERABLE'