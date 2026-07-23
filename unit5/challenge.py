while True:
    score = input("What is your game score: ")
    
    score = score.strip().lower()
    
    if score == "stop":
        break
    else:
        score = int(score)
        
        if score > 100:
            print("Wow! That’s a new high score!")
        else:
            print("Good try, keep playing!")
 