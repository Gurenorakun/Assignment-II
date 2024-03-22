def main():
    total = 0

    while True:
        num = float(input("Enter a number (-1 to stop): "))
        
        if num == -1:
            break
        
        total += num

    print("Sum:", "{:.2f}".format(total))

if __name__ == "__main__":
    main()