import re


act = re.compile(r"^(ACT [IV]+).*")
scene = re.compile(r"(SCENE [IV]+)\. (.*)$")
character = re.compile(r"  ([A-Z ]+)\. *$")
dialog = re.compile(r"    .*$")

def get_scene_data(text, line):
    an, sn, cs, d = "", "", set(), []

    for i in range(line, -1, -1):
        if not d and not dialog.match(text[i]):
            c = character.match(text[i]).group(1)
            j = i + 1
            while dialog.match(text[j]):
                d.append(text[j].rstrip())
                j += 1

        if not sn and scene.match(text[i]):
            sn = scene.match(text[i]).group(1)
            j = i + 1
            while not scene.match(text[j]):
                if character.match(text[j]):
                    cs.add(character.match(text[j]).group(1))
                j += 1

        if act.match(text[i]):
            an = act.match(text[i]).group(1)
            break
    
    return an, sn, cs, c, d

def find_line_number(text, excerpt):
    for i in range(len(text)):
        if text[i].find(excerpt) != -1:
            return i

if __name__ == "__main__":
    text = []
    with open("macbeth.txt") as f:
        text = f.readlines()
    
    s = "rugged Russian bear"

    an, sn, cs, c, d = get_scene_data(text, find_line_number(text, s))
    
    print(an)
    print(sn)
    print("Characters in scene: {}".format(", ".join(cs)))
    print("Spoken by {}:".format(c))
    print("\n".join(d))
