name = input("your name:")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are in a pitch black room. You can feel a door in front of you. You can open the door or turn around and walk forward."
).lower()
# could replace this with buttons instead.

if answer == "open":
    print(answer)
    answer = input(
        "Clouds hide the moon and stars. There is a dirt path in front of you that is perpendicular. The only light around is a small flickering lantern hanging by a branch at the intersection. You can go left or right."
    ).lower()
    if answer == "right":
        print(answer)
        answer = input(
            "You are surrounded by a dense forest. As you get further from the lantern it gets darker, and you can make out what you think are faces hidden in bushes and branches above you. You don't know. It's dark. You feel a small hand press against your back. You can turn or run."
        ).lower()
    else:
        print("Too much to keep going. I'll just end you here.")


elif answer == "turn":
    print("While walking back you bump into something and then screams and agony.")

else:
    print("While walking you bump into something and then nothing...")
