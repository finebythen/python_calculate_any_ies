# --> HOW TO CALCULATE ANY PORT ON A IES

# --> Examples:
# --> IES 5112, 12 Slots, 10 Linecards, 20 Ports per Linecard, 2x MGMT-Cards (Slot 06 & 07)
# --> IES 5206, 06 Slots, 04 Linecards, 40 Ports per Linecard, 2x MGMT-Cards (Slot 05 & 06)
# --> IES 6000, 17 Slots, 15 Linecards, 24 Ports per Linecard, 2x MGMT-Cards (Slot 08 & 09)

# --> Testport: 38


class IES:
    def __init__(self, name, slots, lc, portLc, mgmtCards):
        self.name = name
        self.slots = slots
        self.lc = lc
        self.portLc = portLc
        self.mgmtCards = mgmtCards


ies_5112 = IES("IES 5112", 12, 10, 20, [6, 7, 0, 0])
ies_5206 = IES("IES 5206", 6, 4, 40, [5, 6, 0, 0])
ies_6000 = IES("IES 6000", 17, 15, 24, [8, 9, 0, 0])
testport = 38


def CalculateIES(port, slots, lc, portLc, mgmtCards):
    list_cards = list(range(1, slots + 1))
    list_mgmt = [value for value in mgmtCards if value != 0]

    for item in list_mgmt:
        list_cards.remove(item)

    if lc == len(list_cards):
        x = [(port // portLc) + 1 if port % portLc != 0 else port // portLc]
        y = [portLc if port % portLc == 0 else port % portLc]

    return x, y


linecard, port = CalculateIES(testport, ies_6000.slots, ies_6000.lc, ies_6000.portLc, ies_6000.mgmtCards)
