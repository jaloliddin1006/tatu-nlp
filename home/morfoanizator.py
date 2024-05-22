# So'zlar va ularning turkumlari lug'ati
"""
So'z turkumlari va belgilar
Ot (N)  (Noun)
Sifat (Adj)  (Adjective)
Fe’l (V) (Verb)
Ravish (Adv)(Adverb)
Son (Num) (Numeral)
Olmosh (Pron)(Pronoun)
Bog'lovchi (Conj) (Conjunction)
Ko'makchi (Part) (Particle)
Yuklama (Part) (Particle)
Modal so'zlar (Mod) (Modal words)
Taqlidlar (Onomat)(Onomatopoeic words)
Undov so'zlar (Interj)(Interjections)

"""

words = {
    "N" : ["kitob", "daraxt", "uy", "o'quvchi", "o'qituvchi", "olma", "maktab", "qalam", "ruchka", "telefon", "komputer", "dastur", "qog'oz", "bog'", "universitet", "ayiq", "odam", "inson", "koptok", "stul", "stol", "parta", "o'rik", "tog'", "xona", ],
    "Adj" : ["katta", "chiroyli", "tez", "qizil", "xursand", "yomon", "qiziq", "qo'rqinchli", "qo'rqoq", "qo'rqoqli", "sariq", "qora", "qizil", "yashil","baland", "past" ],
    "V" : ["o'qi", "yoz", "yur", "bil", "qiyqir", "yubor", "kel", "o'rgan", "yugur", "sakra", "uch", "ich", 'ol', 'ish', "bor"],
    "Adv" : ["tez", "sekin", "yuqori", "past", 'kecha', 'bugun', 'ertaga'],
    "Num" : ["bir", "ikki", "uch", "to'rt", "besh", "olti", "yetti", "sakkiz", "to'qqiz", "o'n", "yigirma", "o'ttiz", "qirq", "ellik", "oltmish", "yetmish", "sakson", "to'qson", "yuz", "ming", "million", "milliard"],
    "Pron" : ["men", "sen", "u", "biz", "kim", "nima", "nima uchun", "qanday", "qaysi", "qancha", "qanchalik", "qaysi", "qanday", "qandaydir", "qandaydir", "kishi"],
    "Conj" : ["va", "lekin", "yoki", "chunki"],
    "Part1" : ["uchun", "bilan", "ga", "dan", "kan", "qan", "gan"], # ko'makchi so'zlar
    # "Part2" : ["chi", "da", "ku", "a"], # yuklama so'zlar
    "Mod" : ["albatta", "ehtimol", "balki", "shubhasiz", "an'anaviy", "sifat", "qo'rqoqli", "qo'rqinchli", "qo'rqoq", "qo'rq"],
    "Onomat" : ["g'uv", "shuv", "tarq", "qars"],
    "Interj" : ["oh", "eh", "afsus", "voy"],
}


base_words = {}


for pos, words_list in words.items():
    for word in words_list:
        base_words[word] = pos



# Har bir turkumga oid so'zlarga ID kod qo'yish
id_counter = 1
word_with_id = {}

for word, pos in base_words.items():
    word_with_id[word] = {"id": id_counter, "pos": pos}
    id_counter += 1

# Grammatik qo'shimchalar lug'ati
suffixes = {
    "bilan": "bilan aff (komitativ)",
    "ingiz": "II shaxs ko'plik egalik aff",
    "yapti": "hozirgi zamon aff",
    "moqda": "hozirgi zamon aff",
    "aylik": "taklif mayli aff",
    "aylar": "hurmat mayli aff (II shaxs ko'plik)",
    "lari": "III shaxs ko'plik egalik aff",
    "imiz": "I shaxs ko'plik egalik aff",
    "ning": "qaratqich kelishigi aff",
    "moq": "harakat nomi aff",
    "lar": "ko'plik aff",
    "ing": "II shaxs birlik egalik aff",
    "dan": "chiqish kelishigi aff",
    "gan": "o'tgan zamon aff",
    "adi": "kelasi zamon aff",
    "man": "I shaxs birlik aff",
    "san": "II shaxs birlik aff",
    "miz": "I shaxs ko'plik aff",
    "siz": "II shaxs hurmat ko'plik aff",
    "lar": "III shaxs ko'plik aff",
    "sin": "buyruq mayli aff (III shaxs)",
    "mas": "inkor aff",
    "may": "inkor aff",
    "dir": "asosiy nisbat aff",
    "dur": "asosiy nisbat aff",
    "tir": "asosiy nisbat aff",
    "tur": "asosiy nisbat aff",
    "chi": "yasovchi aff",
    "lik": "yasovchi aff",
    "kor": "yasovchi aff",
    "dor": "yasovchi aff",
    "ish": "yasovchi aff",
    "siz": "sifatdosh aff",
    "roq": "sifatdosh aff",
    "mi": "so'roq qo'shimchasi",
    "si": "egalik qo'shimchasi",
    "ni": "tushum kelishigi aff",
    "ga": "yo'nalish kelishigi aff",
    "da": "o'rin-payt kelishigi aff",
    "ay": "buyruq mayli aff",
    "da": "kashidali aff",
    "da": "o'rin kelishigi aff",
    "ir": "qaytarmagan nisbat aff",
    "im": "I shaxs birlik egalik aff",
    "ar": "qaytarmagan nisbat aff",
    "di": "o'tgan zamon aff",
    "ib": "ravishdosh aff",
    "uv": "harakat nomi aff",
    "k": "birlik egalik aff",
    "i": "III shaxs birlik egalik aff",
}



# print(suffixes)
# print(dict(sorted(suffixes.items())))
base_words.update(suffixes)


punctluation = {
    ".": "nuqta",
    ",": "vergul",
    "!": "undov",
    "?": "so'roq",
    ":": "ikki nuqta",
    ";": "nuqta va vergul",
    "-": "chiziq",
    "(": "o'chilgan qavs",
    ")": "yo'qilgan qavs",
    "[": "o'chilgan qavs",
    "]": "yo'qilgan qavs",
    "{": "o'chilgan qavs",
    "}": "yo'qilgan qavs",
    "<": "o'chilgan qavs",
    ">": "yo'qilgan qavs",
}

import re

# Funksiya so'zni va uning qo'shimchalarini tahlil qiladi
def analyze_word(word):
    results = []
    while word:
        found = False
        for suffix, description in base_words.items():
            if word.endswith(suffix):
                results.append((suffix, description))
                word = word[:-len(suffix)]
                found = True
                break
                
        if not found:
            results.append((word, "Noma'lum so'z"))
            break

    return list(reversed(results))

# Funksiya matndagi barcha so'zlarni tahlil qiladi
def analyze_text(text):
    for punct, description in punctluation.items():
        text = text.replace(punct, f"")

    words = text.lower().split()
    # print(words)
    analysis = []
    for word in words:
        if word.isdigit():
            analysis.append([(word, "Num")])
            continue
        analysis.append(analyze_word(word))
    return analysis

# # Kiritilgan matn
# text = " Biz 20 Xursandchilikimizdan qiyqirib yubordik."

# # Matnni tahlil qilish
# analysis = analyze_text(text)
# # print(analysis)
# for word_analysis in analysis:
#     for suffix, description in word_analysis:
#         print(f"{suffix} ({description})", end=" ")
#     print()


#son larni tekshiradigan qo'shishim kerak (sonizator bilan birga)