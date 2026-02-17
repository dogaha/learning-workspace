from pathlib import Path

def open_file():
    path = Path(__file__).parent / 'characters.txt'
    data = ['Mario','Luigi','Peach','Yoshi','Bowser','Toad']

    #context Manager (auto close)
    with path.open("w") as file:
        for c in data:
            file.write(c+'\n')

def main():
    open_file()

if __name__ == "__main__":
    main()