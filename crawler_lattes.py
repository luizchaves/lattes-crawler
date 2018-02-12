import StringIO
import zipfile
import csv
import urllib2
import pdb

curriculos = csv.DictReader(open('data/curriculums_ifpb.csv', 'r'))

for curriculo in curriculos:
    # pdb.set_trace()
    id = curriculo['id10']
    name = curriculo['name'].split(' ')[0].lower()

    # http://buscacv.cnpq.br/buscacv/rest/espelhocurriculo/7165875430419020 JSON
    # http://buscacv.cnpq.br/buscacv/#/espelho?nro_id_cnpq_cp_s=7165875430419020 XML
    url = urllib2.urlopen('http://buscacv.cnpq.br/buscacv/rest/download/curriculo/%s' % id)
    zipFile = zipfile.ZipFile(StringIO.StringIO(url.read()))
    curriculoXML = zipFile.read('curriculo.xml')
    zipFile.close()

    file = open('data/xml/%s-%s.xml' % (name,id), 'w')
    file.write(curriculoXML)
    file.close()

    print 'data/xml/%s-%s.xml created!' % (name,id)
