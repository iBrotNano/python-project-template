
log_str = '''
46.72.177.4 - - [12/Dec/2015:18:31:08 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
46.72.177.4 - - [12/Dec/2015:18:31:08 +0100] "POST /administrator/index.php HTTP/1.1" 200 4494 "http://almhuette-raith.at/administrator/" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
46.72.177.4 - - [14/Dec/2015:16:39:27 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
46.72.177.4 - - [14/Dec/2015:16:39:28 +0100] "POST /administrator/index.php HTTP/1.1" 200 4494 "http://almhuette-raith.at/administrator/" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" “-
“~
'''
import random 
for i in range(20):
    for j in range(20):
        ip = str(random.randrange(0,128))+'.'+str(random.randrange(0,128))+'.'+str(random.randrange(0,128))+'.'+str(random.randrange(0,128))
        browser = random.choice(['Firefox','Chrome','Safari'])
        mystr = f'''{ip} - - [12/Dec/2015:18:{i}:{j} +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "{browser}/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 {browser}/34.0" "-"'''
        print(mystr)


