# Ruqia Library
This library used for Arabic NLP to process, prepare and clean the Arabic text   


مكتبة مخصصة لخدمة معالجة اللغة العربية وتشمل عدد من الوظائف لتنظيف النصوص وغيرها

## Install
```
pip install ruqia
```
## Use
```
from ruqiya import ruqiya
```
## Example: Apply a Function to Pandas Single Column

```
from ruqiya.ruqiya import clean_text

# Often df['text'] be Object not String, so we need to apply str 
df['text']=df['text'].apply(str)
# Now apply our function
df['cleaned_text']=df['text'].apply(clean_text)
# Show the result
df['cleaned_text']
```

## All Functions

## Clean the text 
`clean_text` function includes all these functions:   
  >      1. remove_emails  
  >      2. remove_URLs  
  >      3. remove_mentions   
  >      4. hashtags_to_words     
  >      5. remove_punctuations  
  >      6. normalize_arabic   
  >      7. remove_diacritics   
  >      8. remove_repeating_char   
  >      9. remove_stop_words   
  >      10. remove_emojis

 In other words, `clean_text` includes all functions except `remove_hashtags` 
```
text_cleaned1=ruqiya.clean_text(text)
print(text_cleaned1)
```
## Remove repeating character
`remove_repeating_char` function
```
text_cleaned2=ruqiya.remove_repeating_char(text)
print(text_cleaned2)
```
## Remove punctuations
`remove_punctuations` function
```
text_cleaned3=ruqiya.remove_punctuations(text)
print(text_cleaned3)
```
## Normalize Arabic
`normalize_arabic` function

```
text_cleaned4=ruqiya.normalize_arabic(text)
print(text_cleaned4)
```
## Remove diacritics
`remove_diacritics` function
```
text_cleaned5=ruqiya.remove_diacritics(text)
print(text_cleaned5)
```
## Remove stop words
`remove_stop_words` function
```
text_cleaned6=ruqiya.remove_stop_words(text)
print(text_cleaned6)
```
## Remove emojis
`remove_emojis` function
```
text_cleaned7=ruqiya.remove_emojis(text)
print(text_cleaned7)
```

## Remove mentions
`remove_mentions` function
```
text_cleaned8=ruqiya.remove_mentions(text)
print(text_cleaned8)
```
## Convert any hashtags to words
`hashtags_to_words` function
```
text_cleaned9=ruqiya.hashtags_to_words(text)
print(text_cleaned9)
```

## Remove hashtags
`remove_hashtags` function
```
text_cleaned10=ruqiya.remove_hashtags(text)
print(text_cleaned10)
```
## Remove emails
`remove_emails` function
```
text_cleaned11=ruqiya.remove_emails(text)
print(text_cleaned11)
```
## Remove URLs
`remove_URLs` function
```
text_cleaned12=ruqiya.remove_URLs(text)
print(text_cleaned12)
```
#
## Example
```
from ruqiya import ruqiya

text="""
!!أهلًا وسهلًا بك 👋 في الإصدارِ الأولِ من مكتبة رقيا
هل هذه هي المرة الأولى التي تستخدم فيها المكتبة😀؟!!
معلومات التواصل 
ايميل
example@email.com
الموقع
https://pypi.org/project/ruqia/
تويتر
@Ru0Sa
وسم
#معالجة_العربية
"""

print('===========clean_text===========')
text_cleaned1=ruqiya.clean_text(text)
print(text_cleaned1)
print('===========remove_repeating_char===========')
text_cleaned2=ruqiya.remove_repeating_char(text)
print(text_cleaned2)
print('===========remove_punctuations===========')
text_cleaned3=ruqiya.remove_punctuations(text)
print(text_cleaned3)
print('===========normalize_arabic===========')
text_cleaned4=ruqiya.normalize_arabic(text)
print(text_cleaned4)
print('===========remove_diacritics===========')
text_cleaned5=ruqiya.remove_diacritics(text)
print(text_cleaned5)
print('===========remove_stop_words===========')
text_cleaned6=ruqiya.remove_stop_words(text)
print(text_cleaned6)
print('===========remove_emojis===========')
text_cleaned7=ruqiya.remove_emojis(text)
print(text_cleaned7)
print('===========remove_mentions===========')
text_cleaned8=ruqiya.remove_mentions(text)
print(text_cleaned8)
print('===========hashtags_to_words===========')
text_cleaned9=ruqiya.hashtags_to_words(text)
print(text_cleaned9)
print('===========remove_hashtags===========')
text_cleaned10=ruqiya.remove_hashtags(text)
print(text_cleaned10)
print('===========remove_emails===========')
text_cleaned11=ruqiya.remove_emails(text)
print(text_cleaned11)
print('===========remove_URLs===========')
text_cleaned12=ruqiya.remove_URLs(text)
print(text_cleaned12)

```

## Example 2: Apply a Function to Pandas DataFrame (Single Column)

```
from ruqiya.ruqiya import clean_text
import pandas as pd

data="https://raw.githubusercontent.com/Ruqyai/data4test/main/test_with_lables.csv"
df=pd.read_csv(data)
df['text']=df['poem_text']

#--------------------
# Often df['text'] be Object not String, so we need to apply str 
df['text']=df['text'].apply(str)
# Now apply our function
df['cleaned_text']=df['text'].apply(clean_text)
#--------------------

# Show the result
df['cleaned_text']
```
# Citing Ruqia
If Ruqia helps your research, we appreciate your citations. Here is the BibTeX entry:   
```
@misc{Ruqia2022,
  title={Ruqia-Library},
  author={Ruqiya Bin Safi},
  year={2022},
  howpublished={\url{https://github.com/Ruqyai/Ruqia-Library}},
}
```
