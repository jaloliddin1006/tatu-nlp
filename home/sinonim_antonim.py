
sinonims = [
    (["katta", "ulkan", "buyuk", "yirik"], ["kichik", "mayda", "mitti", "xurjinga sig‘adigan"]),
    (["kichik", "mayda", "mitti", "xurjinga sig‘adigan"], ["katta", "ulkan", "buyuk", "yirik"]),
    (["chiroyli", "go‘zal", "latofatli", "nazokatli"], ["nosoz", "abgor", "achinarli", "yomon"]),
    (["tez", "shiddatli", "yashin tezligida", "chaqqon"], ["sekin", "asta-sekin", "ohista", "surunkali"]),
    (["sekin", "asta-sekin", "ohista", "surunkali"], ["tez", "shiddatli", "yashin tezligida", "chaqqon"]),
    (["yaxshi", "a'lo", "zo‘r", "mukammal"], ["yomon", "nosoz", "abgor", "achinarli"]),
    (["yomon", "nosoz", "abgor", "achinarli"], ["yaxshi", "a'lo", "zo‘r", "mukammal"]),
    (["quvonchli", "xursand", "baxtli", "mamnun"], ["qayg‘uli", "g‘amgin", "mahzun", "motamli"]),
    (["qayg‘uli", "g‘amgin", "mahzun", "motamli"], ["quvonchli", "xursand", "baxtli", "mamnun"]),
    (["aqlli", "dono", "farosatli", "zukkoy"], ["nodon", "ahmoq", "tentak", "go‘l"]),
    (["nodon", "ahmoq", "tentak", "go‘l"], ["aqlli", "dono", "farosatli", "zukkoy"]),
    (["qattiq", "mustahkam", "mahkam", "puxta"], ["yumshoq", "mayin", "muloyim", "serlamoq"]),
    (["yumshoq", "mayin", "muloyim", "serlamoq"], ["qattiq", "mustahkam", "mahkam", "puxta"]),
    (["qizil", "alvon", "jigar rang", "qizg‘ish"], ["ko‘k", "zangori", "moviy", "g‘uncha rang"]),
    (["ko‘k", "zangori", "moviy", "g‘uncha rang"], ["qizil", "alvon", "jigar rang", "qizg‘ish"]),
    (["oq", "oppoq", "qaldirg‘och rang", "sutday oq"], ["qora", "tim qora", "qoramtir", "quyuq rang"]),
    (["qora", "tim qora", "qoramtir", "quyuq rang"], ["oq", "oppoq", "qaldirg‘och rang", "sutday oq"]),
    (["yangi", "yangicha", "zamonaviy", "bugungi"], ["eski", "qadimiy", "an'anaviy", "urf-odatga xos"]),
    (["eski", "qadimiy", "an'anaviy", "urf-odatga xos"], ["yangi", "yangicha", "zamonaviy", "bugungi"]),
    (["issiq", "jazirama", "qizg‘in", "issiqcha"], ["sovuq", "qahraton", "zax", "muzday"]),
    (["sovuq", "qahraton", "zax", "muzday"], ["issiq", "jazirama", "qizg‘in", "issiqcha"]),
    (["boy", "boyvachcha", "davlatmand", "badavlat"], ["kambag‘al", "nochor", "faqir", "muhtoj"]),
    (["kambag‘al", "nochor", "faqir", "muhtoj"], ["boy", "boyvachcha", "davlatmand", "badavlat"]),
    (["uzoq", "olis", "yiroq", "uzoqroqda"], ["yaqin", "tig‘iz", "tutash", "qo‘shni"]),
    (["yaqin", "tig‘iz", "tutash", "qo‘shni"], ["uzoq", "olis", "yiroq", "uzoqroqda"]),
    (["baquvvat", "kuchli", "polvon", "tog‘dek"], ["zaif", "ojiz", "lolu", "nochor"]),
    (["zaif", "ojiz", "lolu", "nochor"], ["baquvvat", "kuchli", "polvon", "tog‘dek"]),
    (["hozirgi", "ayni damdagi", "bugungi", "zamonaviy"], ["o'tmish", "qadimiy", "tarixiy", "avvalgi"]),
    (["o'tmish", "qadimiy", "tarixiy", "avvalgi"], ["hozirgi", "ayni damdagi", "bugungi", "zamonaviy"]),
    (["kelajak", "istiqbol", "oldindagi", "keyingi"], ["boylik", "davlat", "badavlatlik", "farovonlik"]),
    (["boylik", "davlat", "badavlatlik", "farovonlik"], ["kelajak", "istiqbol", "oldindagi", "keyingi"]),
    (["ehtiyoj", "talab", "hojat", "zarurat"], ["xizmat", "ish", "mehnat", "faoliyat"]),
    (["xizmat", "ish", "mehnat", "faoliyat"], ["ehtiyoj", "talab", "hojat", "zarurat"]),
    (["tinchlik", "osoyishtalik", "osoyishta hayot", "xotirjamlik"], ["urush", "jang", "nizoli holat", "adovat"]),
    (["urush", "jang", "nizoli holat", "adovat"], ["tinchlik", "osoyishtalik", "osoyishta hayot", "xotirjamlik"]),
    ([ "qo‘rqinchli", "qo‘rqoqli", "qo‘rqoq", "qo‘rqinchoq"], ["qo‘rqmas", "qo‘rqinmas", "qo‘rqinchoqmas", "qo‘rqinchoq"]),
    ([ "qo‘rqmas", "qo‘rqinmas", "qo‘rqinchoqmas", "qo‘rqinchoq"], ["qo‘rqinchli", "qo‘rqoqli", "qo‘rqoq", "qo‘rqinchoq"]),
   
]

import random

def change_antonim(matn):
    anonims = []
    for first, second in sinonims:
        for word in first:
            if word in matn:
                anonims.append((word, random.choice(second)))
    for word, new_word in anonims:
        matn = matn.replace(word, new_word)
    return matn
