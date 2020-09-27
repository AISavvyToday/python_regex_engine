def input_starting_with_regex(reg, inp):
    escaped = False

    if not reg or reg == "$" and not inp:
        return True

    if reg[0] == "\\":
        escaped = True
        reg = reg[1:]

    if inp and (reg[0] == inp[0] or not escaped and reg[0] == "."):
        if len(reg) >= 2:
            if reg[1] == "+":
                return input_starting_with_regex(reg[0] + "*" + reg[2:], inp[1:])
            if reg[1] == "?":
                return input_starting_with_regex(reg[2:], inp) or input_starting_with_regex(reg[2:], inp[1:])
            if reg[1] == "*":
                return input_starting_with_regex(reg[2:], inp) or input_starting_with_regex(reg, inp[1:])

        return input_starting_with_regex(reg[1:], inp[1:])

    if len(reg) > 1 and (reg[1] == "?" or reg[1] == "*"):
        return input_starting_with_regex(reg[2:], inp)
    return False


def apply_regex(reg, inp):
    if len(reg) > 0 and reg[0] == "^":
        return input_starting_with_regex(reg[1:], inp)
    else:
        return input_starting_with_regex(reg, inp) or bool(inp) and apply_regex(reg, inp[1:])


regex, input_ = input().split('|')

print(apply_regex(regex, input_))
