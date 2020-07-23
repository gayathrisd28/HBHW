def delivery_report(day,str1):
        
    print(day)
    the_file = open(str1)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    the_file.close()
        
                

day = 1
num = 20140519

for x in range(3):   
    str1 = f"um-deliveries-{num}.txt"
    delivery_report(day,str1)
    day += 1
    num += 1


