def get_ip(addr):
    ip_addresses = []
    count = 0
    if len(addr) < 4:
        print(addr + " is too short to be a proper IP address")
        return
    if len(addr) > 12:
        print(addr + " is too long to be a proper IP address")
        return
    for i in range(0, len(addr)-3):
        for j in range(i+1, len(addr)-2):
            for k in range(j+1, len(addr)-1):
                for l in range(k+1, len(addr)):
                    isValid = True                  
                    groups = [addr[:j], addr[j:k], addr[k:l], addr[l:]]
                    for element in groups:
                        if element == "":
                            isValid = False
                        elif int(element) > 255:
                            isValid = False
                    if isValid:
                        temp = groups[0] + "." + groups[1] + "." + groups[2] + "." + groups[3]
                        if len(ip_addresses) == 0:
                            ip_addresses.append(temp)
                        else:
                            for element in ip_addresses:
                                if element == temp:
                                    count += 1
                                    print(count)
                                    print("dupe " + temp)
                                    isValid = False
                            if isValid:
                                ip_addresses.append(temp)
                    
    if len(ip_addresses) == 0:
        print(addr + " is not a valid IP Address")
    else:
        print("IP address " + addr)
        print(ip_addresses)
        print(str(len(ip_addresses)) + " valid IPs")

get_ip("1962138")
get_ip("123456")
get_ip("1111111111")
get_ip("111111111111")
get_ip("123456789")
get_ip("12345678901")
get_ip("1111111111111")
get_ip("1234")
get_ip("123")
