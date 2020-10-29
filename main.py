# Alexander Fatjo
def greet(name):
    # The "def" functions marks the start of a header. I learned this at
    # "programiz.com".
    name = input("Your name: ")
    if not name:
        # The "not" functions creates a rule that if the user does not input
        # a name, "Welcome anonymous!" will print.
        return "Welcome anonymous!"
    # The "return" function returns a value from the function. In this case
    # "Welcome anonymous" is returned to "greet".
    return "Welcome " + name + "!"


# The "+" operator adds a parameter or parenthesised text to the print
# statement without additional spaces. I learned this on "07planning.org".
greeting = greet("")
print(greeting)
print(
    "My name is Alex Fatjo.\nIf you have any questions or concerns feel free "
    "to email me.")
print("alexfatjo", "gmail.com", sep='@')
# The "sep='@'" is used to replace any spaces within the print text with
# whatever is in the following quotation marks("@"). I learned how to use
# this on "geeksforgeeks.org".
print("What year were you born? \nEnter year in four digits.")
year_born = int(input("Year: "))
this_year = 1600 // 2 + 2440 / 2
# The "// 2" is used for square rooting a number that comes before
# it.Opposites of the exponential operator, "**". I learned this operation
# on "w3schools.com". The "/" operator is used to divide numbers.
user_age = this_year - year_born
# The line above takes "this_year" and subtracts it by the "year_born"(Year
# born) variable to find user_age. "-" operator subtracts numbers.
print("Your age is:", user_age)
if user_age < 20:
    # This if/else statement declines you from continuing if you are under
    # 20 years old
    print("Your results have arrived: Your not employable...")
elif user_age > 20:
    print(
        "Good, you will need to be. \nWish to find the career path for you? "
        "\nTo continue type yes")
continue_option = input("")
if continue_option == "yes":
    print(
        "Welcome to Fatjo's Career Finder, glad you could make it! \nI will "
        "ask you several questions which will result in the career that best "
        "suits you. \nFirst question: \nWhich do you find more important: "
        "Money or Happiness")
    # I used the "\n" to split the text into different lines rather than
    # printing them merged together.
    money_or_happiness = input("")
    happiness = "happiness"
    money = "money"
    # The two variables above "money" and "happiness were added so that when
    # you type money, all code referring to "happiness" is skipped over.
    if money_or_happiness == happiness:
        # Added the lower case so code doesn't fail because of capitalization.
        print(
            "Which of these do you find the most interest in? \nExploration, "
            "Agriculture or Communication")
        choice_exploration = "Exploration" or "exploration"
        choice_agriculture = "Agriculture" or "agriculture"
        choice_communication = "Communication" or "communication"
        choice_of_expl_ag_comm = input("")
        if choice_of_expl_ag_comm == choice_exploration:
            # The "or" operator creates a rule that the user can input both
            # uppercase and lowercase versions of the same word and get the
            # same result.
            print(
                "We are getting closer! \nWhich sparks your interest more: "
                "\nGeology or Photography?")
            choice_of_geologist_photographer = input("")
            if choice_of_geologist_photographer == "Photography" or "photography":
                print(
                    "Your results are Here! \nThe career which best suits "
                    "you, includes: \nFreelance Photographer \nCommercial "
                    "Photographer \nFine Art Photographer")
            if choice_of_geologist_photographer == "Geology" or "geology":
                print(
                    "Your results are Here! \nThe career which best suits "
                    "you includes: \nEnvironmental Geologist \nGlacial "
                    "Geologist")
            else:
                print(
                    "Apologies, that is not one of the options. Please try "
                    "again.")
        # "Else" creates a rule where the print command below it will run if
        # none of the "if" conditions are met by the user.
        if choice_of_expl_ag_comm == choice_agriculture:
            print(
                "We are getting closer! \nWhich sparks your interest more: "
                "\nAquatic Ecologist or Farmer?")
            choice_of_aquatic_farmer = input("")
            if choice_of_aquatic_farmer == "Aquatic Ecologist" or "aquatic " \
                                                                  "Ecologist":
                print(
                    "Your results are Here! \nThe career which best suits "
                    "you includes: \nAquatic Ecologist \nRestoration "
                    "Ecologist \nEnvironmental Consultant")
            if choice_of_aquatic_farmer == "Farmer" or "farmer":
                print(
                    "Your results are Here! \nThe career which best suits "
                    "you includes: \nFarmer \nAgronomist \nAgricultural "
                    "Specialist")
            else:
                print(
                    "Apologies, that is not one of the options. Please try "
                    "again.")
        if choice_of_expl_ag_comm == choice_communication:
            print(
                "We are getting closer! \nWhich sparks your interest more: "
                "\nJournalist or Therapist?")
            choice_of_journalism_therapist = input("")
            if choice_of_journalism_therapist == "Journalism" or "journalism":
                print(
                    "Your results are Here! \nThe career which best suit you "
                    "includes: \nJournalist \nAuthor \nNews Editor")
            if choice_of_journalism_therapist == "Therapist" or "therapist":
                print(
                    "Your results are Here! \nThe career which best suits "
                    "you includes: \nTherapist \nPsychiatrist "
                    "\nNeuropsychologist")
            else:
                print(
                    "Apologies, that is not one of the options. Please try "
                    "again.")
    if money_or_happiness == money:
        # "elif" is added to separate the choice of "Happiness"
        # and "Money" into separate paths.
        print(
            "Which of these do you find the most interest in: \nMathematics "
            "or Biology?")
        choice_biology = "biology" or "Biology"
        choice_mathematics = "mathematics" or "Mathematics"
        choice_analyst = "analyst" or "Analyst"
        choice_of_math_bio = input("")
        if choice_of_math_bio == choice_biology:
            print(
                "We are getting closer! \nSelect which pay range accompanied "
                "by difficulty level best suits you. \n1: $200,"
                "000  Difficulty Level: 10 \n2: $150,000  Difficulty Level: "
                "8 \n3: $100,000  Difficulty Level: 7")
            for i in range(1, 11):
                # The "range" function creates a range from 1-10.
                print("Level:", i, end=', ')
            # The "level:, " in the line above print before each number
            # which is the "i". The "end=" operator combines all levels
            # instead of placing each level on a different line. I used
            # "geeksforgeeks.org" to use this operator properly.
            difficulty_level = int(input("Your Level: "))
            multiplied_difficulty_level = (difficulty_level * 2)
            if 14 >= multiplied_difficulty_level >= 8 and difficulty_level != 16:
                # The "and" operator adds an additional rule so that the
                # print statement below will only print when the user's
                # input is less than or equal to 14 AND greater than or
                # equal to 8, the "!=" create a rule that the user's input
                # cannot equal 16 to print.
                print(
                    "Your results have arrived! \n The career that best "
                    "suits you is: \nBiochemist")
            elif multiplied_difficulty_level == 16:
                # "elif" is similar to "if", except it allows for
                # combination of conditions. The "==" is an equal-to sign.So
                # the statement below only prints when the user's input is
                # equal to 16.
                print(
                    "Your results have arrived! \nThe career that best suits "
                    "you is: \nDentist")
            elif multiplied_difficulty_level >= 18:
                print(
                    "Your results have arrived! \nThe career that best suits "
                    "you is: \nPhysician")
            elif multiplied_difficulty_level <= 6:
                print(
                    "Your results have arrived! \nThe career that best suits "
                    "you is: \nHealth communications specialist "
                    "\nPharmaceutical Sales Representative")
            else:
                print(
                    "Apologies, that is not one of the options. Please try "
                    "again.")
        if choice_of_math_bio == choice_mathematics:
            print(
                "We are getting closer! \nWhich sparks your interest more: "
                "\nAnalyst or Mathematician?")
            choice_of_analyst_math = input("")
            if choice_of_analyst_math == choice_analyst:
                print(
                    "What would you rate your analytical skills on a scale "
                    "of 1-10")
                analyst_skill_rating = int(input(""))
                analyst_skill_rating_squared = (analyst_skill_rating ** 2)
                # The "** 2" exponentiates the user's input(
                # analyst_skill_rating) by 2(squaring) which is then assessed
                # in the lines below.
                if analyst_skill_rating_squared < 40:
                    # If the user believe their skill level is below a 6
                    # from 1-10, lower skill level careers are chosen.
                    print(
                        "Your results have arrived! \nThe career that best "
                        "suits you is: \nOperations Analyst \nMarketing "
                        "Analyst \nIT Systems Analyst")
                # "break" makes the program stop running, if not it would
                # continue in a loop.
                elif analyst_skill_rating_squared > 40:
                    print(
                        "Your results are Here! \nThe career which best "
                        "suits you includes: \nData Scientist \nBusiness "
                        "Intelligence Analyst \nQuantitative Analyst")
                else:
                    print(
                        "What you typed was incorrect. Be a little more "
                        "careful")
# "else" statement added so that when user inputs incorrectly, there is
# feedback.
# Example for "while" function below.
# Example:   i = 1
#           while i < 2:
#               print(i)
#               i += 1
#           else:
#               print("i is less than 3")
# The "while" statement creates a loop that executes a specified statement if
# the condition stated is true. I learned this information from
# "developer.mozilla.org."
# The "+=" function adds 1 to the variable, "i".
# Example for the "%"(modulus) operator shown below.
# Example:       18 % 4
# The "%"(modulus) operator devides left hand operand by right hand operand
# and returns the remainder. The remainder of 18 / 4 is 2.
