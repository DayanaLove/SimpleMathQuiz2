import random

class Student:

    def __init__(self, number_of_questions, level):
        self.number_of_questions = number_of_questions
        self.level = level

    def get_level(self):
        return self.level

    def easy_test(self):
        user_answer = 0
        answer = 0
        score = int(0)
        for x in range(int(self.number_of_questions)):
            if int(user_answer) == answer:
                num1 = random.randint(0, 10)
                num2 = random.randint(0, 10)
                answer = int(num1) + int(num2)
                user_answer = input("what is {} + {}".format(num1, num2))
                if int(user_answer) == answer:
                    score += 1
                while int(user_answer) != answer:
                    print("That's not right. Try again")
                    user_answer = input("what is {} + {}".format(num1, num2))
                print("Great Job!")

        print("Amazing Job! Your score is: " + str(score) + "/" + str(self.number_of_questions))

    def medium_test(self):
        user_answer = 0
        answer = 0
        score = int(0)

        for x in range(int(self.number_of_questions)):
            if int(user_answer) == answer:
                num1 = random.randint(0, 40)
                num2 = random.randint(0, 40)
                answer = int(num1) + int(num2)
                user_answer = input("what is {} + {}".format(num1, num2))
                if int(user_answer) == answer:
                    score += 1
                while int(user_answer) != answer:
                    print("That's not right. Try again")
                    user_answer = input("what is {} + {}".format(num1, num2))
                print("Great Job!")

        print("Amazing Job! Your score is: " + str(score) + "/" + str(self.number_of_questions))

    def hard_test(self):
        user_answer = 0
        answer = 0
        score = int(0)
        for x in range(int(self.number_of_questions)):
            if int(user_answer) == answer:
                num1 = random.randint(0, 100)
                num2 = random.randint(0, 100)
                answer = int(num1) + int(num2)
                user_answer = input("what is {} + {}".format(num1, num2))
                if int(user_answer) == answer:
                    score += 1
                while int(user_answer) != answer:
                    print("That's not right. Try again")
                    user_answer = input("what is {} + {}".format(num1, num2))
                print("Great Job!")

        print("Amazing Job! Your score is: " + str(score) + "/" + str(self.number_of_questions))



