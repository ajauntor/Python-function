'''User input supplies function parameter'''

def happyBirthday(anyPerson):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear " + anyPerson + ".")
    print("Happy Birthday to you!")

def main():
    mriDul = input("Enter the Birthday person's name: ")
    happyBirthday(mriDul)

main()