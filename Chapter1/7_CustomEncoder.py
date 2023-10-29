def custom_encoder(word):
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    position_list = []
    for char in word:
        loop_char = char.lower()
        if loop_char in reference_string:
            position = reference_string.index(loop_char)
        else:
            position = -1
        position_list.append(position)
        
    return position_list