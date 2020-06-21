count = 0
i = 1
CloseStr = "close"
import time
import subprocess
with open('config.cfg', 'r') as f:
    for line in f:
        count += 1
print(""""Number of Games is""", count - 1, '''
Type "close" to close the program''')
def GetNumber():
    G = input("""Type the number of the game you would like.
-->""")
    if G.lower() == CloseStr or G.lower() == "exit" or G.lower() == "quit":
        exit()
    if G.isnumeric():
        game = int(G)
    if not G.isnumeric():
        print("Please enter a number.")
    else:
        try:
            print(content[game])
            print("Loading")
        except:
            print("Please Enter A Valid Number Between 1 and ", count - 1,".", sep='')
            GetNumber()
    try:
        a = content[game].split('=', 1)
        print(a[1])
        b=a[1]
        subprocess.call(b, shell=True)
        time.sleep(1)               
    except:
        GetNumber()    
with open("config.cfg") as f:
    content = f.readlines()
content = [x.strip() for x in content]
while (i < count):
    c = content[i].split('=', 1)
    print(i,c[0])
    i = i + 1
GetNumber()


