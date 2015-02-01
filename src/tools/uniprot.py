import fasta
import files
import urllib2


def read_one(label):
    return fasta.read_one_from(urllib2.urlopen('http://www.uniprot.org/uniprot/%s.fasta' % (label)))


def read(labels):
    data = []

    for label in labels:
        data.append((label, read_one(label)))

    return data
