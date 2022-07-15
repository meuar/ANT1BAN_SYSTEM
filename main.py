import os; import amino; import time; from sys import stdout; import heroku3
try:
    import requests
    from flask import Flask
    from json_minify import json_minify
except:
    os.system("pip3 install requests flask json_minify")

com_id = "52368421"

def restart():
    heroku_conn = heroku3.from_key(key); botapp= heroku_conn.apps()[app_name]; botapp.restart()

ts=time.sleep; t=1; pvs=0; pnvs=0; msgtm = ("   подожди 10 секунд")
client = amino.Client(); client.login(email="zeliht2@1secmail.com", password="987123987123"); print("   ура login!\n\n\n"); sub_client = amino.SubClient(comId=com_id,profile=client.profile);com_info = client.get_community_info(comId=com_id); choice = '1'
while True:
    if choice == '1':
        users_count = sub_client.get_online_users(size=1).userProfileCount;users_count = users_count - (users_count % 100 - 1)
        for i in range(0, users_count, 100):
            os.system("clear"); users = sub_client.get_online_users(start=i, size=100).profile; print("   ищем пидора в сети...\n");ts(1); t=1
            for nickname, uid, content in zip(users.nickname, users.userId, users.content):
                if content is None: continue
                if '_(.a={}{}{}' in content:
                    sub_client.ban(userId=uid, reason='подозрение в нелегальной деятельности'); print(f'   попуск {nickname} да он');pvs=1; ts(5)

    if pvs == 0:
    	print("   (пидор в сети не найден :< го офлайн чекним)\n\n\n");choice = '2';ts(2)
    if pvs == 1:
    	print("   (пидор в сети найден :> и устранен)\n\n\n"); pvs = 0

    if choice == '2':
        users_count = 9901 if com_info.usersCount > 10000 else com_info.usersCount - (com_info.usersCount % 100 - 1); choice = '1'
        for i in range(0, users_count, 100):
            users = sub_client.get_all_users(start=i, size=100).profile;print("   ищем пидора офлайн...\n");ts(1); 
            for nickname, uid, content in zip(users.nickname, users.userId, users.content):
            	if content is None: continue
            	if '_(.a={}{}{}' in content:
            		sub_client.ban(userId=uid, reason='подозрение в нелегальной деятельности'); print(f'   попуск {nickname} да он'); ts(5)

    if pnvs == 0:
    	print("   (пидор офлайн не найден :< давай по новой)\n\n\n");choice = '1';ts(2)
    if pnvs == 1:
    	print("   (пидор офлайн найден :> и устранен)\n\n\n"); pnvs = 0
    print(msgtm)
    ts(10)

    restart()
