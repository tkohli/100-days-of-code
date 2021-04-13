# Defanging an IP Address
"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".
eg: Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
"""


def defangIPaddr(address):
    """
    :type address: str
    :rtype: str
    """
    out = []
    for add in address:
        if add == '.':
            out.append("[.]")
        else:
            out.append(add)
    return ''.join(map(str, out))