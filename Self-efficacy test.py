name =(input("Enter your name here:"))

print("Welcome", name,"! you are about to take a General Self-efficacy test.")

print("Input the option that best describes your answer. \na = Not at all true \nb = Hardly true \nc = Moderately true \nd = Exactly true")

print("Please note that there is no right or wrong answer, all options are valid.")



a = 1
b = 2
c = 3
d = 4

score = 0


question1= input("I can always manage to solve difficult problems if I try hard enough. \n")
if(question1 =="a"):
    score = score + 1
elif(question1 =="b"):
    score = score + 2
elif(question1 =="c"):
    score = score + 3
elif(question1 =="d"):
    score = score + 4

question2= input("If someone opposes me, I can find the means and ways to get what I want. \n")
if(question2 =="a"):
    score = score + 1
elif(question2 =="b"):
    score = score + 2
elif(question2 =="c"):
    score = score + 3
elif(question2 =="d"):
    score = score + 4

question3= input("It is easy for me to stick to my aims and accomplish my goals. \n")
if(question3 =="a"):
    score = score + 1
elif(question3 =="b"):
    score = score + 2
elif(question3 =="c"):
    score = score + 3
elif(question3 =="d"):
    score = score + 4

question4= input("I am confident that I could deal efficiently with unexpected events. \n")
if(question4 =="a"):
    score = score + 1
elif(question4 =="b"):
    score = score + 2
elif(question4 =="c"):
    score = score + 3
elif(question4 =="d"):
    score = score + 4

question5= input("Thanks to my resourcefulness, I know how to handle unforeseen situations. \n")
if(question5 =="a"):
    score = score + 1
elif(question5 =="b"):
    score = score + 2
elif(question5 =="c"):
    score = score + 3
elif(question5 =="d"):
    score = score + 4

question6= input("I can solve most problems if I invest the necessary effort. \n")
if(question6 =="a"):
    score = score + 1
elif(question6 =="b"):
    score = score + 2
elif(question6 =="c"):
    score = score + 3
elif(question6 =="d"):
    score = score + 4

question7= input("I can remain calm when facing difficulties because I can rely on my coping abilities. \n")
if(question7 =="a"):
    score = score + 1
elif(question7 =="b"):
    score = score + 2
elif(question7 =="c"):
    score = score + 3
elif(question7 =="d"):
    score = score + 4

question8= input("When I am confronted with a problem, I can usually find several solutions. \n")
if(question8 =="a"):
    score = score + 1
elif(question8 =="b"):
    score = score + 2
elif(question8 =="c"):
    score = score + 3
elif(question8 =="d"):
    score = score + 4

question9= input("If I am in trouble, I can usually think of a solution. \n")
if(question9 =="a"):
    score = score + 1
elif(question9 =="b"):
    score = score + 2
elif(question9 =="c"):
    score = score + 3
elif(question9 =="d"):
    score = score + 4

question10= input("I can usually handle whatever comes my way. \n")
if(question10 =="a"):
    score = score + 1
elif(question10 =="b"):
    score = score + 2
elif(question10 =="c"):
    score = score + 3
elif(question10 =="d"):
    score = score + 4

    
print("You got ", score,".")

if  score>=10 and score<=20:
    print("Dear",name,", the test result indicates that you have a low percieved self-efficacy. However, this can be enhanced by working on self perception and motivation and social influences arounnd you.")
elif score>=21 and score<=27:
    print("Dear",name,", the test results indacates that you have a fair percieved self-efficacy, which can be enhanced by consciously working on social influence and self motivation.")
elif score>=28 and score<=34:
    print("Dear",name,", the test result indicates that you have a good percieved self-efficacy, Weldone! ")
elif score>=35 and score<=40:
    print("Dear",name,", the test result indicates that you have a high perceived self-efficacy, Great!")
                 
        
