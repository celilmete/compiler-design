def take_param(sys_arg):
    if len(sys_arg) == 2:
        try:
            param = sys_arg[1]
            if param.endswith('.jg'):
                return param
            else:
                print("file must end with .jg")
                exit(0)
        except:
            print("Enter file name correctly")
            exit(0)

    else:
        print("Enter file name")
        exit(0)


def read_file(file_name):
    words = []
    with open(file_name, 'r') as file:
        for line in file:
            for word in line.split():
                words.append(word)
    return words


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
