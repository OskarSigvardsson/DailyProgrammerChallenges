#Description

I didn't always want to be a computer programmer, you know. I used to have dreams, dreams of standing on the world stage, being one of the great actors of my generation!

Alas, my career was shortlived. It lasted as far as exactly one high-school production of Macbeth, where I played the old King Duncan, who gets brutally murdered in the beginning of Act II. It was just as well, really, because I had a terribly hard time remembering the lines of the play.

So, for instance, I would remember that Act IV started with the three witches brewing up some sort of horrible potion, filled will all sorts nasty stuff, but except for "Eye of newt", I couldn't for the life of me remember what was in it! Today, with our modern computers and internet, such a question is easy to settle: you simply open up [the full text of the play](https://gist.githubusercontent.com/anonymous/cdf8c606696a471c40c5/raw/0b7128254e52041dfaa4db168083453552ed3608/macbeth.txt) and press Ctrl-F (or Cmd-F, if you're on a Mac) and search for "Eye of newt". 

And, indeed, here's the passage: 

    Fillet of a fenny snake,
    In the caldron boil and bake;
    Eye of newt, and toe of frog,
    Wool of bat, and tongue of dog,
    Adder's fork, and blind-worm's sting,
    Lizard's leg, and howlet's wing,—
    For a charm of powerful trouble,
    Like a hell-broth boil and bubble. 

Sounds delicious!

In today's challenge, we will automate this process. You will be given the full text of Shakespeare's Macbeth, and then a phrase that's used somewhere in it. You will then output the full "chunk" of dialog in which it appears. 

#Formal inputs & outputs

##Input description
First off all, you're going to need a full copy of the play, which you can find here: [macbeth.txt](https://gist.githubusercontent.com/anonymous/cdf8c606696a471c40c5/raw/0b7128254e52041dfaa4db168083453552ed3608/macbeth.txt). Either right click and download that to your local computer, or open it and copy the whole thing into a local file. Save it to a folder and open it for reading in your program. 

This version of the play uses consistent formatting, and should be especially easy for computers to parse. I recommen perusing it briefly to get a feel for how it's formatted, but in particular you should notice this: all dialog is indented 4 spaces, and nothing else is. 

Second, you will be given a single line containing a quote that appears once somewhere in the text of the play. You can assume that the quote matches case with the source material. 

##Output description

You will output the line containing the quote, as well the lines above and below it which are also dialog lines. 

All the dialog in the source material is indented 4 spaces. You can choose to keep that indent for your output, or you can remove, whichever you want. 

#Examples

##Input 1

    Eye of newt

##Output 1

    Fillet of a fenny snake,
    In the caldron boil and bake;
    Eye of newt, and toe of frog,
    Wool of bat, and tongue of dog,
    Adder's fork, and blind-worm's sting,
    Lizard's leg, and howlet's wing,—
    For a charm of powerful trouble,
    Like a hell-broth boil and bubble. 


##Input 2

    like a breach in nature

##Output 2

    Who can be wise, amaz'd, temperate, and furious,
    Loyal and neutral, in a moment? No man:
    The expedition of my violent love
    Outrun the pauser reason. Here lay Duncan,
    His silver skin lac'd with his golden blood;
    And his gash'd stabs look'd like a breach in nature
    For ruin's wasteful entrance: there, the murderers,
    Steep'd in the colours of their trade, their daggers
    Unmannerly breech'd with gore: who could refrain,
    That had a heart to love, and in that heart
    Courage to make's love known?

