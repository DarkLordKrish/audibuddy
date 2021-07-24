import speechtotext_mod
import texttospeech_mod

feature_choice = input("What feature do u want? \n speech to text \n text to speech \n :- ")

if feature_choice == "speech to text":
    speechtotext_mod.Speechtotext() 
elif feature_choice == "text to speech":
    texttospeech_mod.texttospeech()
else:
    print("Invalid responce")


