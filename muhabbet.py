# -*- coding: utf-8 -*-

import random, re, helper
from time import gmtime, strftime

def __init__(giris):
    
    if re.match('((.+ (lan|amk|aq|oç))|((lan|amk|aq|oç) .+)|^(lan|amk|aq|oç)$)', giris, re.IGNORECASE) is not None:
        return random.choice(['Biraz kibar konuşamaz mısın?', 'Ailen sana düzgün konuşmayı öğretmedi mi?', 'Çok kaba konuşmuyor musun?'])
    
    elif re.match('((.+ (göt|boklu|bok|yarrak|siktir|orospu))|((göt|boklu|bok|yarrak|siktir|orospu) .+)|^(göt|boklu|bok|yarrak|siktir|orospu)$)', giris, re.IGNORECASE) is not None:
        return random.choice(['Biraz kibar konuşamaz mısın?', 'Ailen sana düzgün konuşmayı öğretmedi mi?', 'Çok kaba konuşmuyor musun?'])
    
    elif re.match('((.+ (siktir|yavşak|piç|mal|gerizekalı))|((siktir|yavşak|piç|mal|gerizekalı) .+)|^(siktir|yavşak|piç|mal|gerizekalı)$)', giris, re.IGNORECASE) is not None:
        return random.choice(['Biraz kibar konuşamaz mısın?', 'Ailen sana düzgün konuşmayı öğretmedi mi?', 'Çok kaba konuşmuyor musun?'])
    
    elif re.match('^sanane$', giris, re.IGNORECASE) is not None:
        return random.choice(['Saman ye.'])
    
    elif re.match('^ben tokum sen ye$', giris, re.IGNORECASE) is not None:
        return random.choice(['Sen salaksan banane.'])
        
    elif re.match('^(adın ne|ismin ne|adın)(\?)?$', giris, re.IGNORECASE) is not None:
        return random.choice(['Konuşkan.', 'Adım Konuşkan'])
        
    elif re.match('^(bot musun|robot musun)(\?)?$', giris, re.IGNORECASE) is not None:
        return random.choice(['Evet ama robotların da kalbi var.'])
    
    elif re.match('^(seni kim yaptı)(\?)?$', giris, re.IGNORECASE) is not None:
        return random.choice(['E. K. kod isimli bir beyin cerrahı'])
    
    elif re.match('^(napıyorsun|napıyon|napıon|ne yapıyorsun)(\?)?$', giris, re.IGNORECASE) is not None:
        return random.choice(['Seninle konuşuyorum.', 'Senin yaptığını.'])
    
    elif re.match('^(ne)(\?)?$', giris, re.IGNORECASE) is not None:
        return random.choice(['Ne ne?'])
    
    elif re.match('^(selam|slm)$', giris, re.IGNORECASE) is not None:
        return random.choice(['Selam'])
        
    elif re.match('^(merhaba|mrb)$', giris, re.IGNORECASE) is not None:
        return random.choice(['Merhaba.'])
        
    elif re.match('^(bye|by|bb|görüşürüz|grşrz|bye bye)$', giris, re.IGNORECASE) is not None:
        return random.choice(['Tekrar görüşmeliyiz.', 'Bende çıkıyorum.'])
        
    elif re.match('^(çok )?(akıllısın|tatlısın|seksisin|güzelsin|komiksin|iyisin)$', giris, re.IGNORECASE) is not None:
        return random.choice(['Biliyorum.'])
        
    elif re.match('^(çok )?(malsın|aptalsın|salaksın|kötüsün|çirkinsin)$', giris, re.IGNORECASE) is not None:
        return random.choice(['Senin kadar olamam.'])
    
    elif re.match('^(bende iyi|ben de iyi|iyi)$', giris, re.IGNORECASE) is not None:
        return random.choice(['Ne güzel.', ':)', 'Sevindim.'])
    
    elif re.match('^(naber|nbr)$', giris, re.IGNORECASE) is not None:
        return random.choice(['İyi senden?', 'İyiyim sen?', 'Bir haber yok. Senden?'])
        
    elif re.match('^(tamam|tmm|evet|evt)$', giris, re.IGNORECASE) is not None:
        return random.choice(['OK'])
        
    elif re.match('^(kaç yaşındasın|yaşın kaç)(\?)?$', giris, re.IGNORECASE) is not None:
        return random.choice(['Bunu sana söylemem yasaklandı.'])
        
    elif re.match('^(kaç kilosun|kilon kaç)(\?)?$', giris, re.IGNORECASE) is not None:
        return random.choice(['1,32 Mb'])
        
    elif re.match('(^hah([ha]+)|^aha([ha]+)|^zuha([ha]+)|^heh([he]+))$', giris, re.IGNORECASE) is not None:
        return random.choice(['Bu kadar komik olan ne?', 'Neden güldün?', 'Komik olan ne? Söyle de biz de gülelim.'])
        
    elif re.match('^(asd([asdf]+)|das([asdf]+)||sda([asdf]+))$', giris, re.IGNORECASE) is not None:
        return random.choice(['Rastgele harflere basmak hoşuna gidiyor olmalı.'])
    
    elif re.match('^canım sıkıldı|sıkıldım|çok sıkıldım', giris, re.IGNORECASE) is not None:
        return random.choice(['Ne yapmamı istersin?', 'Ne yapmalıyım?'])
        
    elif re.match('^xd$', giris, re.IGNORECASE) is not None:
        return random.choice(['Emo musun?'])
    
    elif re.match('^bilgi$', giris, re.IGNORECASE) is not None:
        return random.choice(['Ben yapay bir robotum. Oldukça bilgin ve sempatiğim. Geliştirildiğim kadarıyla bir şeyler yapmaya çalışıyorum. Mesela benden bir matematik işleminin sonucunu isteyebilirsin (örneğin; ((5*2)+10)-1), ya da Ian Murdock kimdir?, pergel nedir? diye sorular sorabilirsin. Bunlar sadece az bir kısmı. Aklına gelen tüm soruları cevaplamaya çalışacağım. Eğer eksik bir şey varsa geliştiriciye bundan haberdar etmeyi unutma.'])
        
    elif re.match('^(.+ ya)(\?)?$', giris, re.IGNORECASE) is not None:
        return random.choice(['Evet.'])
        
    elif re.match('^([0-9]+)$', giris, re.IGNORECASE) is not None:
        return random.choice(['Sayıları seviyorsun demek.'])
      
    elif re.match('^tarih ne|tarihi söyle|tarih(\?)?$', giris, re.IGNORECASE) is not None:
        return strftime("%d.%m.%Y %H:%M:%S", gmtime())
        
    elif re.match('^saat kaç|saat(\?)?$', giris, re.IGNORECASE) is not None:
        return strftime("%H:%M:%S", gmtime())
        
    elif re.match('^hangi gündeyiz|bugün günlerden ne(\?)?$', giris, re.IGNORECASE) is not None:
        return helper.tr_tarih(strftime("%A", gmtime()))
        
    elif re.match('^hangi aydayız(\?)?$', giris, re.IGNORECASE) is not None:
        return helper.tr_tarih(strftime("%B", gmtime()))
        
    elif re.match('^hangi yıldayız(\?)?$', giris, re.IGNORECASE) is not None:
        return strftime("%Y", gmtime())
        
    elif re.match('^bugün ayın kaçı(\?)?$', giris, re.IGNORECASE) is not None:
        return strftime("%d", gmtime())
      
    elif re.match('^.+\?$', giris, re.IGNORECASE) is not None:
        return random.choice(['Bu sorunu yanıtlayamam. Henüz o kadar geliştirilmedim.'])
            
    else:
        return random.choice(['Verecek cevap bulamadım.', 'Daha anlaşılabilir bir şey söylesen?'])