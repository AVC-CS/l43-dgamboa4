def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    total = 0
    i = 0 
    while (i < 5):
        user_num = int(input('Enter your num '))
        total += user_num
        i += 1
    print("Total: ", total)

    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
