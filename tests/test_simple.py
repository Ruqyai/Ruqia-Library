
import unittest

from ruqiya.ruqiya import clean_text


class TestSimple(unittest.TestCase):


    def test_clean_text(self):

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
        
        expected_text = """
وسهلا  الاصدار  مكتبه رقيا  المره  تستخدم المكتبه معلومات التواصل ايميل الموقع تويتر وسم معالجه العربيه
        """
        
        cleaned_text = clean_text(text)
        
        self.assertEqual(cleaned_text, expected_text.strip())
if __name__ == '__main__':
    unittest.main()
