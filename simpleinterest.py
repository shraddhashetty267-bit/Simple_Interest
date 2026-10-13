import sys


def simInt(principal, interest, time):
    return (principal * interest * time) / 100


if __name__ == "__main__":
    # Read command-line arguments and convert them to integers
    p = int(sys.argv[1])
    i = int(sys.argv[2])
    t = int(sys.argv[3])

    # Calculate and print the simple interest
    print("Simple interest: ", simInt(p, i, t))