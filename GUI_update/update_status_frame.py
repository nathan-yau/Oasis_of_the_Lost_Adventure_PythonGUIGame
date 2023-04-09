def update_status_message(player_info: dict, start_skip: int, end_skip: int) -> str:
    """
    Convert a dictionary that contains the name of a player's attributes as key and their corresponding value into
    an aligned string in multiples lines after excepting name and coordinates of the player.

    :param player_info: a dictionary that generated by create_character(), which produces a dictionary
                        that contain the name of character's attributes as key and their corresponding data as values
    :param start_skip: an integer indicating the starting index of the attributes to skip in the list of attributes
    :param end_skip: an integer indicating the ending index of the attributes to skip in the list of attributes
    :precondition: player_info must be a dictionary that contains the name of a player's attributes as key and their
                   corresponding value
    :precondition: player_info must contain keys named as "Name", "Current HP" and "Current HP"
    :postcondition: convert a dictionary that contains the name of a player's attributes as key and their corresponding
                    value into an aligned string in multiples lines after excepting name and coordinates of the player
    :return: an aligned string in multiples lines after excepting name and coordinates of the player
    :raises TypeError: if start_skip and/or end_skip is not an integer
    :raises KeyError: if player_info does not contain keys named as "Name", "Current HP" and "Current HP"
    :raises AttributeError: if player_info is not a dictionary

    >>> character_dict = {"Name": "Nathan", "Current HP": 100, "Current MP": 200, "Strength": 100}
    >>> update_status_message(character_dict, -1, 4)
    'Current HP               100\\nCurrent MP               200'
    >>> update_status_message(character_dict, 2, 2)
    'Current HP               100\\nCurrent MP               200\\nStrength                 100'
    """
    character_status = ""
    keys_to_skip = set(list(player_info.keys())[start_skip:end_skip])
    for key, value in player_info.items():
        if key in keys_to_skip or key == "Name":
            continue
        if key == "Max HP":
            current_hp = max(player_info["Current HP"], 0)
            value = f"{current_hp}/{value}"
            key = "Current HP"
        elif key == "Max MP":
            current_mp = max(player_info["Current MP"],   0)
            value = f"{current_mp}/{value}"
            key = "Current MP"
        character_status += f"{key:<16}{value:>12}\n"
    return character_status.rstrip()


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()