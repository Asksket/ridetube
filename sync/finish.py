#!/usr/bin/env python3
"""RideTube with the Close button, ready for the MGU Store (run in the RideTube checkout, Close already applied).

  python3 finish.py <this folder> <the RideTube checkout>

App version: RideTube's x.y.z becomes x.y.(z * 100 + REV), so each RideTube release, and each REV raised by hand
for a change of ours alone, is newer for the Store than the one before it. mgu-repo.json: this folder's, with
jap-ridetube-d required at the version RideTube's service has.
"""
import json
import os
import re
import sys

here, repo = sys.argv[1], sys.argv[2]
rev = int(open(os.path.join(here, 'REV')).read().strip())
assert 1 <= rev <= 99, 'REV is 1 to 99'

app_path = os.path.join(repo, 'apps', 'jap_ridetube', 'app.json')
text = open(app_path).read()
x, y, z = map(int, json.loads(text)['version'].split('.'))
version = '%d.%d.%d' % (x, y, z * 100 + rev)
text, n = re.subn(r'("version"\s*:\s*")\d+\.\d+\.\d+(")', r'\g<1>' + version + r'\2', text, count=1)
assert n == 1, 'no version in app.json'
open(app_path, 'w').write(text)

service = json.load(open(os.path.join(repo, 'native', 'jap-ridetube-d', 'component.json')))['version']
spec = json.load(open(os.path.join(here, 'mgu-repo.json')))
for c in spec['components']:
    if c['id'] == 'jap_ridetube':
        c['requires']['jap-ridetube-d'] = service
open(os.path.join(repo, 'mgu-repo.json'), 'w').write(json.dumps(spec, indent=2) + '\n')
print('app %s, service %s' % (version, service))
