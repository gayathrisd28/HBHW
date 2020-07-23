melon_cost = 1.00

def accounting(cus_file):
        the_file = open(cus_file)
        for line in the_file:
                line = line.rstrip()
                words = line.split('|')

                cus_name = words[1]
                count = int(words[2])
                cus_paid =float(words[3])
                
                customer_expected = count * melon_cost
                if customer_expected != cus_paid:
                    print(f"{cus_name} paid ${cus_paid:.2f},",
                        f"expected ${customer_expected:.2f}"
                        )
                if customer_expected > cus_paid:
                    amt = customer_expected - cus_paid
                    print(f"{cus_name} has underpaid and have to pay ${amt:.2f} more")
                elif customer_expected < cus_paid:
                    amt = cus_paid-customer_expected
                    print(f"{cus_name} has overpaid and should get ${amt:.2f} back")



        the_file.close()

accounting("customer-orders.txt")
