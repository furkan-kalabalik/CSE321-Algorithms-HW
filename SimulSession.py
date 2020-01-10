sessions = {2:[0,6], 4:[5,10], 1:[0,3], 3:[0,15],5:[8,12],6:[11,14],7:[15,17], 8:[16,22]}

def SimulSession(sessions):
    sessions = {k: v for k, v in sorted(sessions.items(), key=lambda item: item[1])}
    print("Sessions sorted by finish time:", end=" ")
    for i in range(1,len(sessions)+1):
        print(i,end=" ")
    print()
    print("Sessions start time:", end="  ")
    for i in range(1,len(sessions)+1):
        print("%2d"%(sessions.get(i)[0]),end=" ")
    print()
    print("Sessions finish time:", end=" ")
    for i in range(1,len(sessions)+1):
        print("%2d"%(sessions.get(i)[1]),end=" ")
    print()
    lastTime = -1
    optimalSession = []
    for i in range(1,len(sessions)+1):
        if(sessions.get(i)[0] > lastTime):
            optimalSession.append(i)
            lastTime = sessions.get(i)[1]
    print("Optimal session with enter order:", end=" ")
    print(*optimalSession)

SimulSession(sessions)

