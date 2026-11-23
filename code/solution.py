# Sinthia Ledezma - Assignment 5

def sanitize_ip_list(ip_list, blocked_ip):
    """
    Cleans up the IP list by removing occurrences of blocked_ip
    and replacing any IP string containing 'invalid' with '0.0.0.0'.
    """
    clean_list = []
    for ip in ip_list:
        if ip == blocked_ip:
            # Skip the blocked IP entirely (do not add to clean_list)
            continue
        elif "invalid" in ip:
            # Replace invalid IP strings with '0.0.0.0'
            clean_list.append("0.0.0.0")
        else:
            clean_list.append(ip)
    return clean_list
