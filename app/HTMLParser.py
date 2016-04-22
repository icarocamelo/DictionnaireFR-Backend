from lxml import etree
import urllib


class HTMLParser:

    def __init__(self):
        pass

    def parse(self, term):
        url = 'http://www.le-dictionnaire.com/definition.php?mot='
        wp = urllib.urlopen(url + term)
        tree = etree.parse(wp, etree.HTMLParser())

        result = tree.xpath('//td[@class=\'arial-12-gris\']')[0]

        # Clean up
        for bad in result.xpath("//a"):
            bad.getparent().remove(bad)

        for bad in result.xpath("//script"):
            bad.getparent().remove(bad)

        for bad in tree.xpath("//img"):
            bad.getparent().remove(bad)

        for bad in result.xpath("//p"):
            bad.getparent().remove(bad)

        for bad in result.xpath("//div"):
            bad.getparent().remove(bad)

        return etree.tostring(result, pretty_print=True)
