import random

_1  =  ["abadiy", "mangu", "umrbod", "doimiy", "toabad", "ilalabad", "so‘nmas", "barqaror", "jovidon", "barhayot", "boqiy", "bezavo"] 
_2  =  ["abadiylashtirmoq", "mangulashtirmoq", "barqarorlashtirmoq", "unutilmaydigan qilmoq", "yo‘qolmaydigan qilmoq", "mangu qoldirmoq"] 
_3  =  ["abadiylashmoq", "barqarorlashmoq", "mangulik kasb etmoq" ] 
_4  =  ["abadiylik", "barhayotlik", "barqarorlik", "mangulik", "doimiylik", "cheksizlik", "boqiylik"] 
_5  =  ["doimo", "abadulabad"] 
_6  =  ["abzats", "xatboshi", "satrboshi"] 
_7  =  ["evara", "abira"] 
_8  =  ["nochor", "xarob", "majruh", "afgor", "abgor", "ezilgan", "ozor", "aftoda", "aftodahol", "notavon", "darmonsiz", "sho‘rlik", "g‘arib", "benavo", "boyoqish"] 
_9  =  ["abssess", "chipqon"] 
_10  =  ["bulut", "abr"] 
_11 =  ["pachoq", "abjaq", "yaroqsiz"] 
_12  =  ["avaylamoq", "ayamoq", "ehtiyotlamoq", "ehtiyot qilmoq", "ardoqlamoq", "e’zozlamoq", "e’zoz etmoq", "papalamoq" ,"pupalamoq", "rahmdillik qilmoq"] 
_13  =  ["avval", "ilgari", "oldin", "burun", "qadim", "azal", "boshlab"] 
_14  =  ["avvalgi", "oldingi", "ilgarigi", "burungi", "qadimgi", "sobiq", "azalgi", "almisoqi"] 
_15  =  ["chevara", "avag‘a"] 
_16  =  ["qosh", "abro‘"] 
_17  =  ["mavhum", "abstrakt", "xayoliy", "mujmal"] 
_18  =  ["absolyut", "mutlaq"] 
_19  =  ["sarguzasht", "avantyura"] 
_20  =  ["avtomobil", "mashina", "avtomashina", "avto", "ulov"] 
_21  =  ["advokat", "himoyachi", "oqlovchi"] 
_22  =  ["tartibsizlik", "ajiotaj", "alg‘ov-dalg‘ov", "to‘s-to‘polon", "besaranjomlik", "g‘alayon", "bezovtalik"] 
_23  =  ["absorbsiya", "yutilish", "shimilish", "singish"] 
_23  =  ["husnixat", "sarxat", "kalligrafiya"] 
_25  =  ["avvaldan", "ilgaridan", "oldindan", "burundan", "qadimdan", "azaldan", "boshdan", "avval boshdan"] 
_26  =  ["avtomat", "mashina"] 
_27  =  ["avariya", "falokat"] 
_28  =  ["avtoritet", "prestij"] 
_29  =  ["avvalo", "avval", "avvalambor", "avvalam avvali", "boshi", "boshda", "dastlab", "avvalboshi"] 
_30  =  ["avlod", "bo‘g‘in", "sulola", "zot"] 
_31  =  ["agar", "agarda", "mabodo", "basharti", "bordi-yu", "magar"] 
_32  =  ["agent", "ayg‘oqchi", "josus", "shpion"] 
_33  =  ["bosqinchi", "bosmachi", "agressor", "tajovuzkor", "bandit", "qaroqchi"] 
_34  =  ["agressiv", "bosqinchi", "tajovuzkor"] 
_35  =  ["otdosh", "adash", "ismdosh", "nomdosh"] 
_36  =  ["adolat", "odillik", "adl"] 
_37  =  ["adolatli", "odil", "barhaq"] 
_38  =  ["adolatsizlik", "haqsizlik", "qonunsizlik", "bedodlik"] 
_39  =  ["rahm", "shafqat", "omon", "afv"] 
_40  =  ["ayol", "xotin", "xotin-qiz", "xotin-xalaj", "juvon", "rafiqa", "kelin", "kelinchak", "qiz", "qizaloq", "qizcha", "bo‘yqiz", "bolig‘a" , "qariqiz", "bokira", "bolig‘a"] 
_41  =  ["ajablanmoq", "taajjublanmoq", "hayron" "bo‘lmoq", "hayratlanmoq"] 
_42  =  ["ajin", "tirish", "burish"] 
_43  =  ["ajratmoq", "ayirmoq"] 
_44  =  ["farqlamoq", "ajratmoq", "ayirmoq", "farq qilmoq"] 
_45  =  ["kampir", "momoy", "onaxon", "ajuz", "ajuza"] 
_46  =  ["qaror", "jazm", "azimat", "qasd", "azm"] 
_47  =  ["azobli", "jafoli", "uqubatli", "zahmatli", "alamli", "alamnok", "iztirobli", "g‘amli", "aziyatli", "og‘riqli", "ozorli", "achchiq", "sitamli", "qiynoqli", "alamnok", "g‘am-g‘ussali", "biryon"] 


all_sinonim = [
    _1,
    _2,
    _3,
    _4,
    _5,
    _6,
    _7,
    _8,
    _9,
    _10,
    _11,
    _12,
    _13,
    _14,
    _15,
    _16,
    _17,
    _18,
    _19,
    _20,
    _21,
    _22,
    _23,
    _23,
    _25,
    _26,
    _27,
    _28,
    _29,
    _30,
    _31,
    _32,
    _33,
    _34,
    _35,
    _36,
    _37,
    _38,
    _39,
    _40,
    _41,
    _42,
    _43,
    _44,
    _45,
    _46,
    _47,

]

last_parts = ['dali', 'dasiz','sining', 'ining',  'lari', 'larni', 'larini', 'larining', 'lariga', 'laridan', 'lariga', 'larda','mning','sini', 'ini',  'ni','ning', 'ga', 'da', 'dan', 'ka', 'qa', 'lik', 'lar',  ]


def check_word(word):
    
    for i in all_sinonim:
        if word.lower() in i:
            print(word)
            new_word = random.choice(i)
            return new_word 
    return word 


def check_word_sinonim(word):
    
    for i in last_parts:
        if word.lower().endswith(i):
            word = word.replace(i, '')
            last_p = i
            return check_word(word) + last_p
    return check_word(word)


def change_sinonim(sentence1):
    sentence = sentence1.split()
    new_matn = []

    for soz in sentence:
        new_matn.append(check_word_sinonim(soz))  
                
    return ' '.join(new_matn)
    
    
    

# sentence = "Aslida manguning bulutining xotiralarini abadiylashtirmoq kerak."


# change = change_sinonim(sentence)

# print(change)