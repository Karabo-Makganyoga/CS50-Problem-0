deep_thought = input("What is the answer to the Great Question of Life, the Universe, and Everything?").lower().strip()

if deep_thought == "42":
    print("Yes")
elif deep_thought == "forty-two":
    print("Yes")
elif deep_thought == "forty two":
    print("Yes")
else:
    print("No")
