# Reading and Opening Filess
def read_file():
    #open file
    file = open("characters.txt",'r')
    #read
    print("Method 1")
    content = file.read()
    print(content)

    file.seek(0) #reset pointer to begining

    print("Method 2")
    lines = file.readlines()
    for line in lines:
        print(line)
    
    #close
    file.close()

def main():
    read_file()
    return

if __name__ == "__main__":
    main()