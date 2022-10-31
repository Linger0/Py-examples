import os

def main():
    os.chdir('./child')
    os.system('python run.py --file test2.txt')

if __name__ == "__main__":
    main()