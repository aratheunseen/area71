prompt = "Throw the coin and enter head and tail here: "

head = tail = 0

while True:

    flip_result = input("Throw the coin and enter head and tail here: ").lower()

    match flip_result:
        case 'head':
            head += 1
            probability = float(100/(head+tail)*head)
            print(f"Heads: {probability}%")

        case 'tail':
            tail += 1
            probability = float(100/(head+tail)*tail)
            print(f"Heads: {probability}%")