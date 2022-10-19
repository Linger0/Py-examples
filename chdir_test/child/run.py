import argparse
from ast import parse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file",
        type=str,
        nargs="?",
        default="test.txt"
    )

    opt = parser.parse_args()

    with open(opt.file, 'a') as f:
        f.write('new line\n')

if __name__ == '__main__':
    main()
