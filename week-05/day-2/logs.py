# Read all data from 'log.txt'.
# Each line represents a log message from a web server
# Write a function that returns an array with the unique IP adresses.
# Write a function that returns the GET / POST request ratio.

def unique(filename):
    unique_ip = []
    try:
        with open(filename,'r') as f:
            f = f.readlines()
            for line in f:
                word =line.split(" ")
                unique_ip.append(word[8])

    except IOError:
        print("Error occurred opening the file")
        sys.exit()
    
    ip = list(set(unique_ip)) 
    print(ip)  

unique("log.txt")

def request_ratio(filename):
    request_method = []
    try:
        with open(filename,'r') as f:
            f = f.readlines()
            for line in f:
                word =line.split(" ")
                request_method.append(word[11])

    except IOError:
        print("Error occurred opening the file")
        sys.exit()
    count_post=0
    for i in request_method:
        if i == "POST":
            count_post+=1
    print(str(round(count_post/len(request_method)*100)) + "% are POST methods")
    print(str(round((1-(count_post/len(request_method)))*100))+ "% are GET methods")

request_ratio("log.txt")