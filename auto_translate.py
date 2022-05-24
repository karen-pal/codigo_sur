from languages import LANGUAGES

from googletrans import Translator, constants
import random
#phrase = "If you know how to use it!"
#to_trans = phrase
phrases = ["Vast Amounts Of Information", "Available To Everyone Worldwide","If You Know How To Use It!"]
for phrase in phrases:
    print("/"*60)
    to_trans = phrase
    langlist = random.sample(LANGUAGES.keys(),50)
    for lang in langlist:
        try:
            trans = Translator().translate(to_trans, dest=lang).text
            print(trans)
            to_trans = trans
            #sleep(1)
        except:
            pass
