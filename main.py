import speechtotext_mod
import texttospeech_mod

feature_choice = input("What feature do u want?\nspeech to text\ntext to speech")

if feature_choice == "speech to text":
    speechtotext_mod.Speechtotext() 
elif feature_choice == "text to speech":
    texttospeech_mod.texttospeech()
else:
    print("Invalid responce")


