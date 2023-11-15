all_tickets = [x.strip() for x in input().split(", ")]
ticket_state = []
def winning_ticket(ticket):

    if len(ticket) != 20:
        return "invalid ticket"
    first_half = ticket[0:10]
    second_half = ticket[10:]
    winning_symbols = ['@', '#', '$', '^']
    for sym in winning_symbols:
        for repetition in range (10, 5, -1):
            char_repetition = sym * repetition
            if char_repetition in first_half and char_repetition in second_half:
                if repetition == 10:
                    return f"ticket \"{ticket}\" - {repetition}{sym} Jackpot!"
                elif 6<=repetition <=9:
                    return f"ticket \"{ticket}\" - {repetition}{sym}"
    return f"ticket \"{ticket}\" - no match"

for ticket in all_tickets:
    ticket_state.append(winning_ticket(ticket))

for states  in ticket_state:
    print(states)
