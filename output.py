# -*- coding: utf-8 -*-

import sys, zeka
reload(sys)  
sys.setdefaultencoding('utf8')

class konuskan:
    def __init__(self):
        
            giris = sys.argv[1].replace('\n', '')
            cikis = zeka.__init__(giris)
            if cikis:
                print cikis
        
if __name__ == "__main__":
    konuskan()