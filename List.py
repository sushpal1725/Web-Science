import pycurl
import cStringIO
import re

curl = pycurl.Curl()

buff = cStringIO.StringIO()
hdr = cStringIO.StringIO()

curl.setopt(pycurl.URL, 'http://example.org')
curl.setopt(pycurl.WRITEFUNCTION, buff.write)
curl.setopt(pycurl.HEADERFUNCTION, hdr.write)
curl.perform()

print "status code: %s" % curl.getinfo(pycurl.HTTP_CODE)
# -> 200

status_line = hdr.getvalue().splitlines()[0]
m = re.match(r'HTTP\/\S*\s*\d+\s*(.*?)\s*$', status_line)
if m:
    status_message = m.groups(1)
else:
    status_message = ''

print "status message: %s" % status_message