from .uzwords import words
from difflib import get_close_matches
from .translate import to_cyrillic, to_latin

def checkWord(word, words=words):
	word = word.lower()
	matches = set(get_close_matches(word, words, n=3))
	available = False
	# print(matches)

	if word in matches:
		available = True
		matches = word
	elif 'х' in word:
		word = word.replace('х', 'ҳ')
		matches.update(get_close_matches(word, words))
	elif 'ҳ' in word:
		word = word.replace('ҳ', 'х')
		matches.update(get_close_matches(word, words))

	return {'available':available, 'matches':matches}

def check_word(words):
	# words = message.text.split()
	for word in words:
		word1 = word
		matn = word
      
		if matn.isascii():
      
    
		    word1 = to_cyrillic(matn)
		# else:
		#     word = to_latin(matn)


		result = checkWord(word1)
		if result['available']:
			if word.isascii():
				response = [to_latin(word1).lower()]
			else:
				response =[word1.lower()]


		else:
			if word.isascii():
				response = [to_latin(word).lower()]
				for text in result['matches']:
					response.append(to_latin(text).lower())
			else:
				response = [word.lower()]
				for text in result['matches']:
					response.append(text.lower())

		return response



# # men aqshga yashashga ketyapman
# print(check_word(["dunya"]))

# def asos_uchun(matn):
#     sozlar = matn.split()
#     for soz in sozlar:
#         while soz.lower() not in asoslar and len(soz) > 1:
#             soz = soz[:-1]
            
#         if soz.lower() in asoslar:
# 			print(soz)
   
   
# matn = input("Matn kiriting: ")
# asoslar = ['kitob','qalam','ruchka','olma','banan', 'aqsh', 'naqsh']
# asos_uchun(matn)