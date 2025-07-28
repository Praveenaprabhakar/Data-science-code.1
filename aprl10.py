import random
import matplotlib.pyplot as plt

def balls():
    if random.randint(0, 1) == 0:
        return "pink balls"
    elif random.randint(0,2)==0:
        return "Green balls"
    elif random.randint(0,3)==0:
        return "yellow balls"
    elif random.randint(0,4)==0:
        return "red balls"
    else:
        return "black balls"

def sim():
    n = 1000
    result = {"pink balls": 0, "Green balls": 0 , "yellow balls": 0,"red balls": 0,"black balls": 0,}
    
    for _ in range(n):
        result[balls()] += 1
    
    print("pink balls : ", result["pink balls"])
    print("Green balls: ", result["Green balls"])
    print("yellow balls: ", result["yellow balls"])
    print("red balls: ", result["red balls"])
    print("black balls: ", result["black balls"])
   
    pink_balls= result["pink balls"] / n
    Green_balls = result["Green balls"] / n
    yellow_balls = result["yellow balls"] / n
    red_balls = result["red balls"] / n
    black_balls = result["black balls"] / n
    

    print("pink balls : ", pink_balls)
    print("Green balls: ", Green_balls)
    print("yellow balls: ", yellow_balls)
    print("red balls: ", red_balls)
    print("black balls: ", black_balls)



    labels = result.keys()
    counts = result.values()
    plt.bar(labels, counts, color=["pink", "Green","yellow","red","black"])
    plt.title("bar plot")
    plt.ylabel("Count")
    plt.show()

sim()
