#pathlib module
from pathlib import Path


def create_path():
    #Create a new Directory
    script_dir = Path(__file__).parent
    path = script_dir / 'characters'
    
    path.mkdir(parents=True, exist_ok=True)
    #parents=True; If path is missing parts, create it
    #exists_ok: dont throw error if exists

    path = path/'zelda.txt'

    file = path.open('w')
    file.write('Ganon')
    file.close()

    file = path.open('a')
    file.write("\nLink")
    file.close()
    
    print('Read 1')
    file = path.open('r')
    print(file.read())
    file.close()
    
    #truncate file and write
    path.write_text('Epona')

    #Read File
    print('Read 2')
    print(path.read_text())
    return

def main():
    create_path()

if __name__ == "__main__":
    main()