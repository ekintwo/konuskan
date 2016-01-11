# -*- coding: utf-8 -*-

import sys, zeka

class konuskan:
    def __init__(self):
        
        print 'Merhaba, ben Konuşkan. Özelliklerim hakkında bilgi almak için \'bilgi\' yaz.'
        sys.stdout.write('[Ben] '); sys.stdout.flush()
        while 1:
            giris = sys.stdin.readline().replace('\n', '')
            cikis = zeka.__init__(giris)
            if cikis:
                print '\033[94m[Konuşkan] ' + cikis + '\033[0m'.encode('ascii', 'ignore')
            sys.stdout.write('[Ben] ') 
            sys.stdout.flush()
        
if __name__ == "__main__":
    konuskan()