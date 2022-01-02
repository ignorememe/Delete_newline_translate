#pip install googletrans==4.0.0-rc1

import googletrans

translator = googletrans.Translator()

with open("before.txt","rt",encoding='UTF8') as f:
    data = f.read()

new_data = data.replace('\n','_')
new_data = new_data.replace('._','.\n\n')
new_data = new_data.replace('_',' ')

kor_ver = translator.translate(new_data, dest='ko')
print(kor_ver.text)
result = open("result.txt","w")
result.write(kor_ver.text)

result.close()
