from flask import Flask
from flask_cors import CORS
import requests
import json
import pymongo

conn = '' # collection connection link goes here
app = Flask(__name__)
client = pymongo.MongoClient(conn)

Db = client.get_database('kanji')
kanjiDB = Db.kanji

@app.route('/insert-kanji/', methods=['GET'])
def insertOne():
    num = 1
    for i in kanji:
        res = requests.get('https://kanjiapi.dev/v1/kanji/' + i)
        data = res.json()
        kanji_in = {
            'kanji' : data['kanji'],
            'meanings' : data['meanings'],
            'kunyomi' : data['kun_readings'],
            'onyomi' : data['on_readings'],
            'jlpt' : data['jlpt'],
            'number' : num
        }
        query = kanjiDB.insert_one(kanji_in)
        num = num + 1
    return 'Kanji inserted.'

if __name__ == '__main__':
    # load the list of kanji in a list
    kanji = []
    with open('kanji-list-new.txt') as f:
        kanji = f.read().splitlines()
    app.run(debug=True)