#! python3
# -*- coding:utf-8 -*-
from survey import AnonmyousSurvey

# 定义一个问题，并创建一个表示调查的AnonmyousSurvey对象
question = "What language did you first learn to speak?"
my_survey = AnonmyousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# 显示调查结果
print("\nThank you to everyone who participated in the survey!")

# print(my_survey.responses)
my_survey.show_results()
