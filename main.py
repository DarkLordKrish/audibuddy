import speechtotext_mod
import texttospeech_mod
def main_code():
    feature_choice = input("What feature do u want? \n speech to text \n text to speech \n :- ")

    # exit = input("exit?(y/n): ")
    if feature_choice == "speech to text":
        speechtotext_mod.Speechtotext()
    elif feature_choice == "text to speech":
        texttospeech_mod.texttospeech()
    else:
        print("Invalid response")
        main_code()
main_code()
exit = input("exit?(y/n): ")
while exit != "y":
    main_code()
    exit = input("exit?(y/n): ")
quit()





