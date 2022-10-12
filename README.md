# Ruqia lib

## Install
```
pip install ruqia
```
## Use
```
from ruqiya.ruqiya import clean_text
from ruqiya import ruqiya

text="""
!!أهلا وسهلا بك في الإصدار الأول من مكتبة رقيا
هل هي المرة الأولى التي تستخدم فيها المكتبة؟!!
"""

text_cleaned1=ruqiya.clean_text(text)
print(text_cleaned1)
text_cleaned2=ruqiya.remove_repeating_char(text)
print(text_cleaned2)
text_cleaned3=ruqiya.remove_punctuations(text)
print(text_cleaned3)
text_cleaned4=ruqiya.normalize_arabic(text)
print(text_cleaned4)
text_cleaned5=ruqiya.remove_diacritics(text)
print(text_cleaned5)
text_cleaned6=ruqiya. remove_stop_words(text)
print(text_cleaned6)

```
