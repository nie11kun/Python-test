class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self
    
    def get_desc(self):
        return self.class_name + "\n" + self.desc
    
class Goblin(GameObject):
    class_name = "goblin"
    desc = "A foul creature"

def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "there is no {}".format(noun)

def say(x):
    return "you said {}".format(x)

goblin = Goblin("Gobbly")

dic = {
    "say": say,
    "examine": examine,
    }

def get_input():
    command = input(": ").split()
    verb_word = command[0]
    if verb_word in dic:
        verb = dic[verb_word]
    else:
        print("unknown verb {}".format(verb_word))
        return
    if len(command) >= 2:
        non_word = command[1]
        print(verb(non_word))
    else:
        print(verb("nothing"))

while True:
    get_input()
