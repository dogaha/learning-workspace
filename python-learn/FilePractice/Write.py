characters = ['Mario','Luigi','Peach','Yoshi','Bowser','Toad']

def write_characters_to_file(filename):
    #open file
    file = open(filename, 'w+')

    #write
    for c in characters:
        file.write(c+'\n')

    #read
    file.seek(0,0)
    content = file.read()
    print(content)

    #close
    file.close


def main():
    write_characters_to_file('characters.txt')
    return

if __name__ == "__main__":
    main()