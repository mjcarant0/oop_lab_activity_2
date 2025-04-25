# Open .txt file
numberFile = open("number.txt", "r")
oddFile = open("odd.txt", "w")
evenFile = open("even.txt", "w")

for line in numberFile:
    line = line.strip()
    numbers = line.split()

    for number in numbers:
        num = int(number) 

        if num % 2 == 0:
            print(str(num) + " even") 
            evenFile.write(str(num) + "\n") 
        else: 
            print(str(num) + " odd") 
            oddFile.write(str(num) + "\n")  

numberFile.close()
oddFile.close()
evenFile.close()