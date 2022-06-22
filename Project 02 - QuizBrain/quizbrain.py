DELIMITADOR = "=========================================================="

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_questions(self):
        if(self.question_number < len(self.questions_list)):
            return True
        else:
            print(f"Você completou o quiz!")
            print(f"O placar final é:  {self.score}/{self.question_number}")
            return False

    def next_question(self):
        text = self.questions_list[self.question_number].text
        answer = self.questions_list[self.question_number].answer
        options = self.questions_list[self.question_number].options

        self.question_number = self.question_number + 1
        user_answer = input(
            f'Q.{self.question_number}: {text} \n A){options[0]} \n B){options[1]} \n C){options[2]} \n D){options[3]} \n E){options[4]} \n')

        if(user_answer.casefold() == "a".casefold()):
            user_answer = options[0]
        elif(user_answer.casefold() == "b".casefold()):
            user_answer = options[1]
        elif(user_answer.casefold() == "c".casefold()):
            user_answer = options[2]
        elif(user_answer.casefold() == "d".casefold()):
            user_answer = options[3]
        elif(user_answer.casefold() == "e".casefold()):
            user_answer = options[4]

        self.check_answer(user_answer, answer)

    def check_answer(self, user_answer, answer):
        if(user_answer == answer):
            self.score = self.score + 1
            print("Você acertou! :)")
        else:
            print("Você errou!  :(")
        print(DELIMITADOR)
        print(f"A resposta correta é: {answer}")
        print(f"Seu placar no momento é:  {self.score}/{self.question_number}")
        print(f"{DELIMITADOR}\n")



