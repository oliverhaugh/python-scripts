answer_choice_one = input("Choose from a, b, or c: ")
if answer_choice_one == "a":
    answer_choice2_a = int(input("What is your age: "))
    answer_choice3_a = int(input("Choose a random number from one to three (it has to be a whole number from one to three): "))
    generate_sentance = "Generating sentance..."
    print("I am ", answer_choice3_a, " Years old, but i think i am ", answer_choice2_a, " Years old!")
if answer_choice_one == "b":
    answer_choice2_b = input("What is your name: ")
    answer_choice3_b = input("What is your enemies name: ")
    generate_sentance = "Generating sentance..."
    print(generate_sentance)
    print("I admit ", answer_choice3_b, " my enemy, is better than me, ", answer_choice2_b)
if answer_choice_one == "c":
    answer_choice2_c = int(input("choose a random number between one and three: "))
    print("Generating binary...")
    see_binary = input("Would you like to see the binary (Respond with y or n): ")
    if see_binary == "y" and answer_choice2_c == 1:
        print("00110010 00110001 00100000 01101000 01100001 01101000 01100001")
    if see_binary == "y" and answer_choice2_c == 2:
        print("01001001 00100000 01100001 01101101 00100000 01110011 01101111 01110010 01110010 01111001 00100000 01100110 01101111 01110010 00100000 01110100 01101000 01101001 01110011 00100000 01110000 01110010 01101111 01100111 01110010 01100001 01101101 00100000 01100101 01110110 01100101 01110010 00100000 01100010 01100101 01101001 01101110 01100111 00100000 01101101 01100001 01100100 01100101 00001010 00101101 00100000 01110100 01101000 01100101 00100000 01100011 01110010 01100101 01100001 01110100 01101111 01110010 00100000 01101111 01100110 00100000 01110100 01101000 01101001 01110011") 
    if see_binary == "y" and answer_choice2_c == 3:
        print("01110100 01101000 01100101 01111001 00100000 01100001 01101100 01101100 00100000 01101000 01100001 01110100 01100101 00100000 01101101 01100101 00100000 01100010 01100101 01100011 01100001 01110101 01110011 01100101 00100000 01101001 00100000 01100001 01101101 00100000 01101100 01100111 01100010 01110100")
    if see_binary == "n":
        print("Goodbye!")
