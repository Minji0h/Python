import json
from re import A
from question_model import Question
from quizbrain import QuizBrain

DATASET = open("data.json","r")
DATASET = json.load(DATASET)

question_bank = []

for data in DATASET:
    options = data['Options']
    asnwer = data["Asnwer"]
    question = data["Question"]
    question_bank.append(Question(q_text=question, q_asnwer=asnwer, q_options=options))

quizbrain = QuizBrain(question_bank)

while quizbrain.still_has_questions():
    quizbrain.next_question()