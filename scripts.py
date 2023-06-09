import random
import uuid
import hashlib
import logging

LEN_WORD = 20


class Id:
    def __init__(self, len_w=LEN_WORD):
        self.len_word = len_w
        self.uuid_dict = dict()

    @staticmethod
    def rand_letter(l_letter, h_letter):
        """Возвращает букву в алфавите между [a, z]"""
        return chr(random.randint(ord(l_letter), ord(h_letter)))

    def random_text(self) -> str:
        """Возвращает случайное слово длинны len_word"""
        word = ''
        for _ in range(self.len_word):
            lower_letter = self.rand_letter('a', 'z')
            high_letter = self.rand_letter('A', 'Z')
            word += (lower_letter, high_letter)[random.randint(0, 1)]
        return word

    def get_uuid(self, values) -> uuid.UUID:
        """Возвращает uuid вместо идентификатора длинной len_text"""
        for value in values:
            in_dict = None
            try:
                in_dict = self.uuid_dict.get(value, None)
                if not in_dict:
                    word = self.random_text()
                    hex_string = hashlib.md5(word.encode("UTF-8")).hexdigest()
                    new_id = uuid.UUID(hex=hex_string)
                    self.uuid_dict[value] = new_id

            except Exception as ex:

                error_msg = f"An error occurred: {ex}"
                logging.error(error_msg)
                with open('error_log.txt', 'a') as file:
                    file.write(error_msg + '\n')


    def show(self):
        print('Количество id: ', len(self.uuid_dict))
