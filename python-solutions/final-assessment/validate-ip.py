"""4.Read the IP Addresses from the file using regular expression """
import re

read_file = open("ip_address.txt", "r")
file_data = read_file.read()
regex_result = re.findall('[0-2][0-9][0-9]\.[0-2][0-9][0-9]\.[0-2][0-9][0-9]\.[0-2][0-9][0-9]',file_data)
print(regex_result)
read_file.close()
