# Find all permutations of a text field

def permutation(string, mutation=''):
    if len(string) == 0:
        print(mutation)
    for i in range(len(string)):
        neMutation = mutation + string[i]
        newString = string[0:i] + string[i+1:]
        permutation(newString, neMutation)

text = "deepankar"
print("Permutations of \"" + text + "\" is as below,")
permutation(text)
