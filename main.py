from question import question

questions = [
    "In which country can you find the status of liberty? \n(a) USA \n(b) Ghana\n(c) South Korea\n",
    "In which country can you find christ the redeemer status? \n(a) South Africa\n(b) New Zealand\n(c) Brazil",
    "In which country can you find Eiffel Towers? \n(a) Egypt \n(b) France\n(c) South Korea",
    "In which country can you find the Burj Al Arab? \n(a) Morroco \n(b) UAE\n(c) Qatar",
    "The Mount Everest lies between which and which countries? \n(a) China and Russia \n(b) China and Nepal\n(c) Nepal and Russia",
    "In which country can you find golden gate bridge? \n(a) Mexico\n(b) USA\n(c) Canada",

    ]

question_prompt = [
    question(questions[0],"a"),
    question(questions[1],"c"),
    question(questions[3],"b"),
    question(questions[4],"c"),
    question(questions[5],"c")

]
def run_test():
    score = 0
    question_num = 1
    for the_question in question_prompt:
        answer = input(str(question_num)+"). "+the_question.prompt+"\n Enter answer here:")
        if answer == the_question.answer:
            score += 1
            question_num += 1

    print("\n Your score is " + str(score) + "/" + str(len(questions)))

run_test()