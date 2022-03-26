import random

capitals = {'AndhraPradesh'	:'Amaravati',
'ArunachalPradesh'	: 'Itanagar',
'Assam':'Dispur',
'Bihar':'Patna',
'Chhattisgarh':'Raipur',
'Goa':'Panaji',
'Gujarat':'Gandhinagar',
'Haryana' :'Chandigarh',
'HimachalPradesh' :'Shimla',
'Jharkhand' : 'Ranchi',
'Karnataka'	: 'Bengaluru',
'Kerala': 'Thiruvananthapuram',
'MadhyaPradesh':'Bhopal',
'Maharashtra':'Mumbai',
'Manipur':	'Imphal',
'Meghalaya': 'Shillong',
'Mizoram':'Aizawl',
'Nagaland':'Kohima',
'Odisha':'Bhubaneswar',
'Punjab': 'Chandigarh',
'Rajasthan':'Jaipur',
'Sikkim':'Gangtok',
'TamilNadu':'Chennai',
'Telangana':'Hyderabad',
'Tripura':'Agartala',
'UttarPradesh':'Lucknow',
'Uttarakhand':'Dehradun',
'WestBengal':'Kolkata'}

for Qnum in range(3):
    # Create the quiz and answer key files.
    Quiz_file = open('capitalsquiz%s.txt' % (Qnum + 1), 'w')
    Answer_file = open('capitalsquiz_answers%s.txt' % (Qnum+ 1), 'w')
    # Write out the header for the quiz.
    Quiz_file.write('Name: \n\nDate:  \n\nPeriod:\n\n')
    Quiz_file.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (Qnum + 1))
    Quiz_file.write('\n\n')
    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
    Quiz_file.close()
    Answer_file.close()

    # Loop through all 50 states, making a question for each.
    for questionNum in range(28):
        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
    # Write the question and the answer options to the quiz file.
        Quiz_file = open('capitalsquiz%s.txt' % (Qnum + 1), 'a')
        Quiz_file.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))

        for i in range(4):
            Quiz_file.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        Quiz_file.write('\n')
        # Write the answer key to a file.
        Answer_file = open('capitalsquiz_answers%s.txt' % (Qnum + 1), 'a')
        Answer_file.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    Quiz_file.close()
    Answer_file.close()
