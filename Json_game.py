print("This is a random Question video game")
import requests
import json
import pprint
import random
import html
corr=0
wro=0
url="https://opentdb.com/api.php?amount=1&category=31&difficulty=easy&type=multiple"


while True:
    r = requests.get(url)
    if r.status_code != 200:
        print("Sorry there was a problem retreiving the data")
    else:     
     n=random.randint(0,4)
     Q_a=json.loads(r.text)
     options=1
     valid_ans=False
     #comment below prints the json string to dictionart for easy understanding/reading
     #pprint.pprint(Q_a)
     question=Q_a["results"][0]["question"]
     print(html.unescape(question))
     ans=Q_a["results"][0]["incorrect_answers"]
     correct_answer=Q_a["results"][0]["correct_answer"]
     ans.insert(n,correct_answer)
     for answer in ans:
        print(str(options)+". "+html.unescape(answer))
        options+=1
     while valid_ans==False:   
            user_ans=input("Enter answer here: ")
            try:
                user_ans=int(user_ans)
                if user_ans > len(ans) or user_ans<=0:
                   print("Invalid answer. Enter a number within the specified range")
                else:
                    valid_ans=True   
            except:
                print("Invalid answer. Please use only numbers")   
     user_ans=ans[int(user_ans)-1]
     otherwhile=False
     breaking=False
     
     if user_ans == correct_answer:
        print("You got it right, congrats!!")
        again=input("Would like to play again (yes/quit): ")
        corr+=1

     else:
        print("Looks like you go it wrong! The correct answer is "+'"'+html.unescape(correct_answer)+'"')
        again=input("Would like to play again (yes/quit): ")
        wro+=1

     while otherwhile==False:
        if again.lower()=="yes":
         break
         otherwhile==True
        elif again.lower()=="quit":
         breaking=True
         break
        else:
            print("Please enter an option from the values above")
            again=input("Would like to play again (yes/quit): ")

     if breaking==True:
       break
    
print("You got " +str(corr)+"/"+str(corr+wro)+ " answers correct")
print("Thanks for playing, please come again!!")            