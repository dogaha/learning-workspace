more_characters = ['Diddy Kong','Donkey Kong','Wario']

def write_characters_to_file(filename):
    #open file
    file = open(filename, 'a')

    #write
    for c in more_characters:
        file.write(c+'\n')

    #close
    file.close


def main():
    write_characters_to_file('characters.txt')
    return

if __name__ == "__main__":
    main()