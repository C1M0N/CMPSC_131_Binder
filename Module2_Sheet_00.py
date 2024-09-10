def convert_speed(kilometers: float) -> float:
    converted_miles = kilometers * 0.6214
    return converted_miles


def distance_traveled(speed_kph: float, traveled_time: float) -> float:
    km_traveled = speed_kph * traveled_time
    miles_traveled = convert_speed(km_traveled)
    return miles_traveled


my_speed = 100
def main():
    my_speed = 86.5
    my_time = 3
    my_distance = distance_traveled(my_speed, my_time)
    print("Traveled distance is:", my_distance, "miles")


if __name__ == "__main__":
        main()
