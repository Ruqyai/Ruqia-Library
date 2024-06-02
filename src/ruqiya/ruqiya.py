import re
import string
from ruqiya.stopwords import stop_words_ar
from ruqiya.replace_words_dict import replace_words_dict

############### initial variables and lists ##################

arabic_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
english_punctuations = string.punctuation
punctuations_list = arabic_punctuations + english_punctuations

arabic_diacritics = re.compile("""
                             ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)
arabic_handles = \
    [
        ('ه', ['ة']),\
        ('ي', ['ى']),\
        ('ا', ['أ','إ','آ']),\
        # ('و', ['ؤ']),\
        ('', ['ّ','‘','ٌ','ُ','ً','َ','ِ','ٍ','ـ','’','ْ','~'])
    ]

############### functions ##################
def clean_text(text):
    """ 
    It includes these functions:
        1-remove_emails
        2-remove_URLs
        3-remove_mentions
        4-hashtags_to_words
        5-remove_punctuations
        6-normalize_arabic
        7-remove_diacritics
        8-remove_repeating_char
        9-remove_stop_words
        10-remove_emojis
    """
    text=remove_emails(text)
    text=remove_URLs(text)
    text=remove_mentions(text)
    text= hashtags_to_words(text)
    #text=remove_hashtags(text)
    text=remove_punctuations(text)
    text=normalize_arabic(text)
    text=remove_diacritics(text)
    text=remove_repeating_char(text)
    text=remove_stop_words(text)
    text=remove_emojis(text)

    return text


def normalize_arabic(text):
    """ normalize the arabic character  ."""
    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "ء", text)
    text = re.sub("ئ", "ء", text)
    text = re.sub("ة", "ه", text)
    text = re.sub("گ", "ك", text)
    return text


def remove_diacritics(text):
    """ remove the `arabic diacritics` from the `text` ."""
    text = re.sub(arabic_diacritics, '', text)
    return text


def remove_punctuations(text):
    """ remove the `punctuations` from the `text` ."""
    translator = str.maketrans('', '', punctuations_list)
    return text.translate(translator)



def remove_repeating_char(text):
    """
    Removes duplicate characters within words and replaces words in the text based on a dictionary.
    
    Args:
    text (str): The input text.

    Returns:
    str: The processed text with duplicate characters removed and words replaced according to the dictionary.
    """
    words = text.split()

    processed_words = []
    for word in words:
        processed_word = re.sub(r'(.)(\1+)', r'\1', word)
        if processed_word in replace_words_dict:
            processed_word = replace_words_dict[processed_word]
        processed_words.append(processed_word)

    processed_text = ' '.join(processed_words)
    return processed_text



def read_stop_words():
    """ read the `stopwords` """
    stop_words = stop_words_ar.split('\n')
    #unify arabic letters
    for key, arr in arabic_handles:
        for a in arr:
            stop_words = [word.replace(a, key) for word in stop_words] 
    return stop_words


def remove_stop_words(text):
    """ remove the `list of Arabic stopwords` from the `text` ."""
    stop_words = read_stop_words()
    lines = text.splitlines()
    new_lines = []
    for line in lines:
        if line.strip():  #if not empty
            words = line.split()
            for w in range(0, len(words)):
                word = words[w]
                if word in stop_words:
                    words[w] = ""
            line = " ".join(words)
            line = line.replace("  "," ")
            new_lines.append(line)
    return '\n'.join(new_lines)

def remove_emojis(text):
    """ remove the `emojis` from the `text` ."""
    emoj = re.compile("["
        u"\U00002700-\U000027BF"  # Dingbats
        u"\U0001F600-\U0001F64F"  # Emoticons
        u"\U00002600-\U000026FF"  # Miscellaneous Symbols
        u"\U0001F300-\U0001F5FF"  # Miscellaneous Symbols And Pictographs
        u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        u"\U0001F680-\U0001F6FF"  # Transport and Map Symbols
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', text)


def remove_URLs(text): 
    """ remove the `URLs` from the `text` ."""
    text =re.sub(r"(?:http?\://|https?\://|www)\S+", "", text)
    return text

def remove_emails(text):
    """ remove the `emails` from the `text` ."""
    text = re.sub(r'[\w\.-]+@[\w\.-]+',"",text)
    return text

def remove_mentions(text):
    """ remove the `mentions` from the `text` ."""
    text = re.sub(r"@([A-Za-z0-9_-]+)", "", text)
    return text

def remove_hashtags(text):
    """ remove the `hashtags` from the `text` ."""
    text = re.sub(r'#\w+ ?', "", text)
    return text

def hashtags_to_words(text):
    """ convert any `hashtags` to  `words` ."""
    text = re.sub(r'#', "", text)
    text = re.sub(r"_", "  ", text)
    return text



