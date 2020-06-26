import urllib2
import json
import justext
f = open('statusoutputs10','r+')
i=9000
for line in f:
    try:
        data = json.loads(line)
        page = urllib2.urlopen(data['finalurl']).read()
        paragraphs = justext.justext(page, justext.get_stoplist('English'))
        
        i=i+1
        for paragraph in paragraphs:
            if not paragraph.is_boilerplate:
                filename = 'textfromhtml'+str(i)
                outputfile = open(filename, 'w')
                outputfile.write(paragraph.text.encode('utf-8') + '\n')
    except Exception as e:
        print data['finalurl']
        continue