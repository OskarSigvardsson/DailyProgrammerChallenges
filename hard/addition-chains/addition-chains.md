#Description

A so-called "addition chain" is a sequence of numbers that starts with 1 and where each number is the sum of any two previous numbers (or the same number taken twice) in the sequence, and that ends at some predetermined place. 

An example will make this clearer: the sequence [1, 2, 3, 5, 10, 11, 21, 42, 84] is an addition chain for the number 84. This is because it starts with 1 and ends with 84, and each number is the sum of any two previous numbers. To demonstrate:

                    (chain starts as [1])
    1 + 1   = 2     (chain is now [1, 2]) 
    1 + 2   = 3     (chain is now [1, 2, 3]) 
    2 + 3   = 5     (chain is now [1, 2, 3, 5]) 
    5 + 5   = 10    (chain is now [1, 2, 3, 5, 10]) 
    1 + 10  = 11    (chain is now [1, 2, 3, 5, 10, 11]) 
    10 + 11 = 21    (chain is now [1, 2, 3, 5, 10, 11, 21]) 
    21 + 21 = 42    (chain is now [1, 2, 3, 5, 10, 11, 21, 42]) 
    42 + 42 = 84    (chain is now [1, 2, 3, 5, 10, 11, 21, 42, 84]) 

Notice that the right hand side of the equations make up the chain, and left hand side of all the equations is a sum of two numbers that earlier previous in the chain (sometimes the same number twice).

We say that this chain is of length 8, because it took 8 additions to generate it. It is interesting to note that while there are a number of different addition chains of length 8 for the number 84 (another one is [1, 2, 4, 8, 16, 32, 64, 68, 84], for instance), there are no shorter ones. This is as good as we can get. 

Your task today is to try and generate addition chains of a given length and last number. 

#Formal inputs & outputs

##Input description

You will be given one line with two numbers on it. The first number will be the length of the addition chain you are to generate, and the second the final number. 

It is easy to miss but important to note that the length of the addition chain is **one less** than the number of values in it. That is to say, in my earlier example there was 9 numbers in the addition chain for 84, but we say that is of length 8 because it took 8 additions to generate it. 

##Output description

You will output the entire addition chain, one number per line. Note that while there will be many different addition chains of the given length, you only need to output one of them. 

#Examples

##Input 1

    7 43

##Output 1

(one of several possible outputs)

    1
    2
    3
    5
    10
    20
    40
    43

##Input 2

    9 95

##Output 2

(one of several possible outputs)

    1
    2
    3
    5
    7
    14
    19
    38
    57
    95

#Challenge inputs

##Input 1

    10 127

##Input 2

    13 743

#Bonus

    19 123456

#Notes

I would like to note that while this challenge looks very "mathy", and there has indeed been mathematical research regarding addition chains, you don't need any higher level training in mathematics in order to solve this challenge, at least not any more than is needed to understand the problem. There's not some secret formula that you have to figure out. A good working knowledge of some fundamental programming techniques would be very helpful, though! 

In other words, in order to solve this problem (and especially the bonus), you need to be clever, but you don't need to be a mathematician. 

As always, if you have any suggestions, hop on over to /r/dailyprogrammer_ideas and let us know!
