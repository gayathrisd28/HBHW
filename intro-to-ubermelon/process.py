# opening log file details of ubermelon and storing it in variable called ubermelon
log_file = open("um-server-01.txt")

# method called sales_reports which takes in log_file as parameter
def sales_reports(log_file):
    # running a for loop for each line in log_file
    for line in log_file:
        # removing any white space at end of the line
        line = line.rstrip()
        # slicing first 3 chars and storing it in variable day
        day = line[0:3]
        # checking if the day starts with mon to print monday sales report
        if day == "Mon":

            print(line)

# call sales_reports method and passing log_file as input
sales_reports(log_file)
