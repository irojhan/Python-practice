from collections import OrderedDict

def translate_sentence():
    # تعداد کلمات در دیکشنری
    n = int(input())
    translation_dict = OrderedDict()

    # خواندن دیکشنری
    for _ in range(n):
        EN, FA = input().split(' ')
        translation_dict[EN] = FA

    # جمله‌ای که باید ترجمه شود
    sentence = input().strip()

    # ترجمه‌ی جمله
    translated_sentence = []
    for word in sentence.split(' '):
        if word in translation_dict:
            translated_sentence.append(translation_dict[word])
        else:
            translated_sentence.append(word)

    # خروجی جمله‌ی ترجمه شده
    print(' '.join(translated_sentence))

# اجرای برنامه
translate_sentence()
