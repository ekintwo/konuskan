# -*- coding: utf-8 -*-

import re, kim, dinle, islem, muhabbet

def __init__(giris):
    pattern_kim = re.match('(.+) ((kim(dir)?)|nedir)(\?)?$', giris, re.IGNORECASE)
    pattern_dinle = re.match('(.+) dinle$', giris, re.IGNORECASE)
    pattern_islem = re.match('^([\d\(\)\-]+(\+|\-|\*|\/)[\d\(\)\+\-\*\/\.]+)(=)?(\?)?$', giris, re.IGNORECASE)
    
    if pattern_kim:
        return kim.__init__(pattern_kim.group(1))
    elif pattern_dinle:
        return dinle.__init__(pattern_dinle.group(1))
    elif pattern_islem:
        return islem.__init__(pattern_islem.group(1))
    else:
        return muhabbet.__init__(giris)