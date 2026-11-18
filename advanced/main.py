mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)

destination = input("Enter the name of a destination: ")

if destination in mission_route:
    position = mission_route.index(destination)

    print(destination, "is part of the mission route.")
    print("Stops from start:", position)
    print("Stops from end:", len(mission_route) - 1 - position)

    if position < len(mission_route) - 1:
        print("Next stop:", mission_route[position + 1])
    else:
        print("This is the final stop of the journey.")
else:
    print(destination, "is not part of the mission route.")