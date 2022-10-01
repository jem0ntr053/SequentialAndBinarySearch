# Write a program to search sequentially through a file for a record with a
# particular key value.
def search_for_record_seq():
    print("Problem 4:")
    fname = input("Enter your file name: \n")
    with open(fname, 'r') as f:
        lines = f.readlines()
        print(lines)

    last_name = input("Enter last name: \n")
    first_name = input("Enter first name: \n")

    for line in lines:
        if last_name in line and first_name in line:
            print(f"Found Match: {line}")
            break
    else:
        print("record not found")


# with binary search
def search_for_record_bin():
    fname = input("Enter your file name: \n")
    with open(fname, 'r') as f:
        lines = f.readlines()
        print(lines)

    last_name = input("Enter last name: \n")
    first_name = input("Enter first name: \n")

    def binary_search(names_list, target):
        names_list.sort()
        low = 0
        high = len(names_list) - 1
        while low <= high:
            mid = (low + high) // 2
            midpoint = names_list[mid]
            if midpoint.lower() == target.lower():
                return "Found Match: " + midpoint
            elif target.lower() < midpoint.lower():
                high = mid - 1
            else:
                low = mid + 1
        return 'record not found'

    print(binary_search(lines, first_name + " " + last_name
                                          + "\n"))


if __name__ == '__main__':

    # Please feel free to comment out the function you don't want to run:

    # search_for_record_seq()
    search_for_record_bin()
