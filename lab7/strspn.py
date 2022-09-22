def my_strspn(str1, str2):
    count = 0
    for letter in str1:
        i = 0
        while i < len(str2):
            if i == len(str2) - 1 and letter != str2[i]:
                return count
            elif letter == str2[i]:
                count += 1
                i = len(str2)
            else:
                i += 1
    return count

def main():
    user1 = input("Enter string1: ")
    user2 = input("Enter string2: ")
    print("Result: ",my_strspn(user1, user2))


if __name__ == "__main__":
    main()

