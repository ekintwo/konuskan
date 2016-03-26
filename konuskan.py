# -*- coding: utf-8 -*-

import sys, zeka
reload(sys)  
sys.setdefaultencoding('utf8')

class konuskan:
    def __init__(self):
        
        print '''\033[95m
 _   __                      _               
| | / /                     | |              
| |/ /  ___  _ __  _   _ ___| | ____ _ _ __  
|    \ / _ \| '_ \| | | / __| |/ / _` | '_ \ 
| |\  \ (_) | | | | |_| \__ \   < (_| | | | |
\_| \_/\___/|_| |_|\__,_|___/_|\_\__,_|_| |_|
\033[0m'''
        print '\033[92mMerhaba, ben Konuşkan. Özelliklerim hakkında bilgi almak için \'bilgi\' yaz.\033[0m'
        sys.stdout.write('[Ben] '); sys.stdout.flush()
        while 1:
            giris = sys.stdin.readline().replace('\n', '')
            cikis = zeka.__init__(giris)
            if cikis:
                print '\033[94m[Konuşkan] ' + cikis + '\033[0m'
            sys.stdout.write('[Ben] ') 
            sys.stdout.flush()
        
if __name__ == "__main__":
    konuskan()