import category

class main:
    # create a new tracker
    print(f"Hallo!\n")
    t_name = input("Was möchtest du heute tracken?")
    track = category(t_name)
    print(t_name, track.get_name)
    

    # track something
    track.add_new(2022-11-23)
    print(track)

    # track something yesterday
    track.add_new(2022-11-24)
    print(track)

    # change something you tracked
    track.change(2022-11-24)
    print(track)
    print(track.check(2022-11-24))
    track.change(2022-11-22)
    print(track)

    # delete the whole tracker
    track.clear_tracker