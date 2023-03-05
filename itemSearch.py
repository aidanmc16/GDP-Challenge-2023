def itemSearch(cyberItems, itemCounts, fileName):
    with open(fileName, 'r') as file:
        for line in file:
            for item in cyberItems:
                if item in line:
                    itemCounts[item] += 1
    return itemCounts


def main():
    cyberItems=["Virus","Bug", "DDOS", "Patch", "Vulnerabilit", "Threat"]
    itemCounts={item: 0 for item in cyberItems}
    itemCounts=itemSearch(cyberItems,itemCounts,".\data\Secure-file.txt")
    itemCounts=itemSearch(cyberItems, itemCounts, ".\data\DDOS-file.txt") 
    itemCounts=itemSearch(cyberItems, itemCounts, ".\data\online-data.json")
    itemCounts=itemSearch(cyberItems, itemCounts, ".\data\cyber-security.xml")
    print("Virusues:")
    print(itemCounts["Virus"])
    print("Bugs:")
    print(itemCounts["Bug"])
    print("DDOS: ")
    print(itemCounts["DDOS"])
    print("Patches: ")
    print(itemCounts["Patch"])
    print("Vulnerabilities: ")
    print(itemCounts["Vulnerabilit"])
    print("Threats: ")
    print(itemCounts["Threat"])

if __name__ == "__main__":
    main()







             






