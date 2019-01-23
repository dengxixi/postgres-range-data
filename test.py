import psycopg2
import random
import string
import time
import random
conn = psycopg2.connect(database="dump", user="peter", password="53a98wo", host="127.0.0.1", port="5432")
cur = conn.cursor()

'''
cur.execute(
    
    CREATE TABLE dna_app_mapping (
    id bigint NOT NULL,
    source_app_id bigint NOT NULL,
    target_app_id bigint NOT NULL,
    source_market character varying(256) NOT NULL,
    target_market character varying(256) NOT NULL,
    cleaned_name text NOT NULL,
    source_release_date date,
    target_release_date date,
    created_time timestamp without time zone DEFAULT now(),
    last_updated_time timestamp without time zone DEFAULT now()
);

    
    )
'''

a1 = (2000, 1, 1, 0, 0, 0, 0, 0, 0)
a2 = (2019, 1, 20, 23, 59, 59, 0, 0, 0)

start = time.mktime(a1)
end = time.mktime(a2)
date = []



for u in range(10000):

    for i in range(2):
        t = random.randint(start, end)

        date_touple = time.localtime(t)

        date.append(time.strftime("%Y-%m-%d", date_touple))
    if date[0] > date[1]:
        date[0], date[1] = date[1], date[0]

    char_source_market = ''.join(random.sample(string.ascii_letters + string.digits, 25))
    char_target_market = ''.join(random.sample(string.ascii_letters + string.digits, 25))
    text_clean_name = ''.join(random.sample(string.ascii_letters + string.digits, 25))

    num = random.sample(xrange(10000000000000), 3)
    for item in num:
        item = long(item)

    cur.execute(
    '''
    
        insert into dna_app_mapping (
        id, source_app_id, target_app_id, source_market, 
        target_market,cleaned_name,
        source_release_date, target_release_date )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        
    '''
      ,
        (num[0],num[1],num[2], char_source_market, char_target_market, text_clean_name, date[0], date[1])
    )

    date = []

conn.commit()
