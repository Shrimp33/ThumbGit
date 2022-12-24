# if id.txt empty, create new id
# else read id from id.txt
import random

def id():
    with open("id.txt", "r") as f:
        id = f.read()
        if id == "":
            id = "".join([str(random.randint(0, 9)) for i in range(0, 5)])  # Generate 5 digit id
            with open("id.txt", "w") as f:
                f.write(id)
            return id
        else:
            return id