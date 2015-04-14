#Description

One of the most fundamental tools in graphic design is the "gradient": a smooth
transtion from one color to another. They are remarkably useful and are
available in virtually every graphic design program and programming library.
They're even part of CSS nowadays.

Your task today is to draw one of these wonderful gradients. You are to
calculate and draw a gradient and then either draw it to the screen or save it
as an image file. 

**NOTE:** As I said, there are many imaging libraries that provide this
functionality for you, usually in some function called `drawGradient()` or the
like. You are *strongly encouraged* not to use functions like that, the spirit
of this challenge is that you should calculate the gradient (and thus the
individual pixel colors) yourself. This isn't an ironclad rule, though, and if
you really can't think of any way to do this yourself, then it's fine to submit
your solution anyway. I encourage you to try, though. 

It is, however, perfectly acceptable to use a library to create the image and
then saving it as an image file.

#Formal Inputs &amp; Outputs

##Input description

Your input will consist of three lines. The first line contains two numbers
which is the width and the height of the resulting gradient. The other two
lines consist of three numbers between 0 and 255 representing the colors that
the gradient should transition between. The first color should be on the left
edge of the image, the second color should be on the right edge of the image.
So, for instance, the input

    500 100 255 255 0 0 0 255

means that you should draw a 500x100 image that transitions from yellow on the
left side to blue on the right side.

##Output description

You can either choose to draw your gradient to the screen or save it as an
image file. You can choose whatever image format you want, though it should
preferably a loss-less format like PNG. 

If you don't wish to tangle with libraries that output PNG images, I recommend
checking out the [Netpbm](http://en.wikipedia.org/wiki/Netpbm) format, which is
a very easy format to output images in. There's even a [dailyprogrammer
challenge](https://www.reddit.com/r/dailyprogrammer/comments/2ba3g3/7212014_challenge_172_easy/)
that can help you out. 

Regardless of your chosen method of output, I highly encourage you to upload
your resulting images to [imgur](http://imgur.com) so that the rest of us can
see the product of your hard work! If you chose to output your image to the
screen, lets see a (possibly cropped) screenshot!

#Example inputs & outputs

#Input 
    500 100 
    255 255 0 
    0 0 255

#Output

[This image](http://i.imgur.com/LNBRYhr.png)

#Challenge inputs

    1000 100 
    204 119 34 
    1 66 37

Those two colors are Red Ochre and British Racing Green, my personally two
favorite colors. Use those as a challenge input, or pick your own two favorite
colors!

#Bonus

Write a program in brainfuck that produces a 1000x100 sized gradient from Red
Ochre to British Racing Green. You can hardcode the input values in the code if
you wish, and you can output the image in whatever format you like (though I
imagine that using one of the binary Netpbm formats would be the easiest). 

#Finally

Have a good challenge idea?

Consider submitting it to /r/dailyprogrammer_ideas
