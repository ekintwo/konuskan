# -*- coding: utf-8 -*-

def tr_tarih(isim):
    isim = isim.replace('Monday', 'Pazartesi')
    isim = isim.replace('Tuesday', 'Salı')
    isim = isim.replace('Wednesday', 'Çarşamba')
    isim = isim.replace('Thursday', 'Perşembe')
    isim = isim.replace('Friday', 'Cuma')
    isim = isim.replace('Saturday', 'Cumartesi')
    isim = isim.replace('Sunday', 'Pazar')
    isim = isim.replace('January', 'Ocak')
    isim = isim.replace('February', 'Şubat')
    isim = isim.replace('March', 'Mart')
    isim = isim.replace('April', 'Nisan')
    isim = isim.replace('May', 'Mayıs')
    isim = isim.replace('June', 'Haziran')
    isim = isim.replace('July', 'Temmuz')
    isim = isim.replace('August', 'Ağustos')
    isim = isim.replace('September', 'Eylül')
    isim = isim.replace('October', 'Ekim')
    isim = isim.replace('November', 'Kasım')
    isim = isim.replace('December', 'Aralık')
    return isim