def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end='\t')
        print()

print(__name__)

if __name__ == "__main__":
    print("Something to run as stand alone script")

