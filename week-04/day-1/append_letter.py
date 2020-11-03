# Create a function called 'create_new_verbs()' which takes a list of verbs and a string as parameters
# The string should be a prefix
# The function appends every verb to the prefix and returns the list of the new verbs

verbs = ["megy", "ver", "kapcsol", "rak", "néz"]
preverb = "be"

# The output should be: "bemegy", "bever", "bekapcsol", "berak", "benéz"
def create_new_verbs(preverb, verbs):
    output = []
    for i in range(len(verbs)):
        output.append(preverb + verbs[i])
    return str(output).strip('[]')

print(create_new_verbs(preverb, verbs))