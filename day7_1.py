from collections import Counter
with open("sample.txt", "r") as file:
    lines = file.readlines()
def order(hand):

    # A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
    # 57 = ord("9")
    hand = hand.replace("A", chr(57+10))
    hand = hand.replace("K", chr(57+9))
    hand = hand.replace("Q", chr(57+8))
    hand = hand.replace("J", chr(57+7))
    hand = hand.replace("T", chr(57+6))

    C = sorted(Counter(hand).values())
    if C == [5]:
        return (10, hand)
    elif C == [1,4]:
        return (9, hand)
    elif C == [2,3]:
        return (8, hand)
    elif C == [1,1,3]:
        return (7, hand)
    elif C == [1,2,2]:
        return (6, hand)
    elif C == [1,1,1,2]:
        return (5, hand)
    elif C == [1,1,1,1,1]:
        return (4, hand)

    return 0
net = 0
hand_bid = []
for line in lines:
    hand, bid = line.strip().split()
    hand_bid.append((hand, int(bid)))

hand_bid = sorted(hand_bid, key=lambda x: order(x[0]))
for i,(hand, bid) in enumerate(hand_bid):
    net += (i+1)*bid


print(f"ans = {net}")

