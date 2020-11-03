dict = {"William A. Lathan" : "405-709-1865", "John K. Miller" : "402-247-8568", "Hortensia E. Foster":
"606-481-6467", "Amanda D. Newland" : "319-243-5613", "Brooke P. Askew" : "307-687-2982"}

#What is John K. Miller's phone number?

print(dict["John K. Miller"])
#Whose phone number is 307-687-2982?
for k, v in dict.items():
    if v == "307-687-2982":
        print(k)
#Do we know Chris E. Myers' phone number?


if  "Chris E. Myers" in dict.keys():
        print(dict["Chris E. Myers"])
else:
        print("No such phone number exist in the telephone book")