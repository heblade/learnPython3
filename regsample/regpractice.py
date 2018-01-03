import re

class RegPractice(object):
    WORD_REMOVE = ('inc', 'and', 'shares', 'share', 'fund')
    CHAR_REMOVE = ('@', ',', '.', '&', '®')
    WORD_REPLACE = {'admin': 'administrator', 'inst': 'institutional'}
    CHAR_REPLACE = ('-', '/', ':', '—', '–')

    # remove 'inc', 'and', 'shares', 'share'
    def remove_special_word(self, name):
        res = list(filter((lambda x: x not in self.WORD_REMOVE), name.split()))
        return ' '.join(res)

    # remove '@', ',', '.', '()', '&'
    def remove_special_char(self, name):
        res = list(filter((lambda x: x not in self.CHAR_REMOVE), name))
        return ''.join(res)

    @staticmethod
    def clear_brackets(name):
        reg = re.compile('\(.*?\)')
        return reg.sub('', name)

    # replace 'admin','inst'
    def replace_special_word(self, name):
        new_words = list(map(lambda x: self.WORD_REPLACE[x] if x in self.WORD_REPLACE.keys() else x, name.split()))
        return ' '.join(new_words)

    # replace '/','-' with words
    def replace_special_char(self, name):
        r_name = name[:]
        for char in self.CHAR_REPLACE:
            r_name = r_name.replace(char, ' ')
        return r_name

    def dividedBy3(self):
        dataRange = list(filter(lambda n: not (n % 3), range(1, 100)))
        return ','.join(str(number) for number in dataRange)
