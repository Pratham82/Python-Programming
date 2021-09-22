def wrap(string, max_width):
    words = list(string)
    start = 0
    end = max_width
    joined = ""
    for i in range(len(words)):
        if words[start:end] == []:
            break
        joined += "".join(words[start:end]) +'\n'
        start+= max_width
        end+= max_width
    return joined
    

print(wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 3))