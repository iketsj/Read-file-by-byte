import argparse


def main():
    args = parse_args()
    read_file_and_print_contents(args.input)


def parse_args():
    parser = argparse.ArgumentParser(description="Read a file byte by byte")
    parser.add_argument("-i", "--input", metavar="filename", required=True, help="File to be read")
    args = parser.parse_args()

    return args


def read_file_and_print_contents(fileName):
    file = open(fileName, "rb")
    fileSize = file.seek(0, 2)
    file.seek(0, 0)
    contents = file.read(fileSize)

    for i, value in enumerate(contents):
        if (i != (fileSize - 1)):
            print("{0}, ".format(value), end="")
        else:
            print("{0}".format(value))

        if ((i + 1) % 32) == 0:
            print("")


if __name__ == "__main__":
    main()