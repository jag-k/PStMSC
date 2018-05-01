import json

from VKBotAPI import api
from time import sleep

SCORE_FILE = "old_score.json"

chat_id = 72
old_score = json.load(open(SCORE_FILE))
print("Bot start")

while True:
    try:
        new_score = get_score()
        if new_score > old_score:
            api.message.send(message="ВНИМАНИЕ!!! Обновились баллы для поездки в Моску, теперь они %d" % new_score,
                             chat_id=chat_id)
            old_score = new_score
            json.dump(new_score, open(SCORE_FILE, 'w'))

        sleep(15)
    except Exception as err:
        print("ERROR (%s): %s" % (type(err).__name__, err))
