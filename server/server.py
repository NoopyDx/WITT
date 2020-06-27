from bson import ObjectId
import json
from flask import Flask
from flask import jsonify, request
from bson import json_util
import json
import pymongo
from flask_cors import CORS
from datetime import datetime
import random

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


client = pymongo.MongoClient(
    "mongodb+srv://admin:admin@monpremiercluster-d66o9.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")
data = client.whatisthisthing.QA
# print(type(json.dumps(data.find_one(), indent=4,default=json_util.default, ensure_ascii=False)))


def shuffler(data):
    data = eval(data)
    answer = []
    answer.append(data["g_answer"])
    answer.append(data["b_answer1"])
    answer.append(data["b_answer2"])
    answer.append(data["b_answer3"])
    random.shuffle(answer)
    return({"url": data["url"], "answer": answer, "rep": data["g_answer"]})


@app.route('/')
def hello():
    id_value = random.randint(0, 2)
    print(id_value)
    return shuffler(json.dumps(data.find_one({'id': id_value}), indent=4, default=json_util.default, ensure_ascii=False))


@app.route("/test")
def test():
    return "<h1 style='color:blue'>Hello There!</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
