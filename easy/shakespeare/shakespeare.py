import re
import bs4
import sys

from bs4 import BeautifulSoup

def get_text(filename):
    text = []

    with open(filename) as f:
        soup = BeautifulSoup(f)

        curr = soup.find('div', {'class' : 'toc'})

        while curr.next_sibling:
            curr = curr.next_sibling

            if curr.name == 'h2' or curr.name == 'h3':
                text.append("")
                text.append(curr.find('span', {'class':'mw-headline'}).get_text())

            elif curr.name == 'p':
                t = curr.get_text().strip()
                m = re.match(r"^\[(.*)]$", t)
                if t == "":
                    continue
                elif m:
                    text.append(t)
                else:
                    text.append("")
                    text.append("  " + t) 
            
            elif curr.name == 'dl':
                for line in curr.find_all('dd'):
                    text.append("    " + line.get_text().strip())
            elif type(curr) == bs4.element.Comment:
                break

    return "\n".join(text)

if __name__ == "__main__":
    
    files = ["Act_I.html", "Act_II.html", "Act_III.html", 
    "Act_IV.html", "Act_V.html"]

    sys.stdout.write("\n".join(get_text(f) for f in files))
