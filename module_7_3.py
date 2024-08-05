class WordsFinder:
    def __init__(self,*file_names:list):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r',encoding='utf-8') as file:
                word = []
                for line in file:
                    line = line.lower()
                    punk = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for i in punk:
                        line = line.replace(i," ")
                    word.extend(line.split())
                all_words[name] = word
        return all_words

    def find(self, word):
        ura_words = {}
        for file_names, words in self.get_all_words().items():
            for i in range(len(words)):
                if words[i] == word.lower():
                    ura_words[file_names] = i
                    break
        return ura_words

    def count(self,word):
        counter = 0
        ura1_word = {}
        for file_names, words in self.get_all_words().items():
            for word1 in words:
                if word1 == word.lower():
                    counter += 1
                    ura1_word[file_names] = counter
        return ura1_word




finder2 = WordsFinder('file_name.txt')
print(finder2.get_all_words()) # Все слова
print()
print(finder2.find('TEXT'))   # 3 слово по счёту
print(finder2.count('teXT'))   # 4 слова teXT в тексте всего




