t = int(input())

while t > 0:
    t -= 1

    n = int(input())
    s = input()

    seen = []
    for ch in s:
        if ch not in seen:
            seen.append(ch)
            
    if len(seen) < 2:
        print(s)
        continue


    max_freq = s.count(seen[0])
    max_index = 0

    min_freq = s.count(seen[1])
    min_index = s.find(seen[1])


    for i in range(n):
        current_freq = s.count(s[i])

        if current_freq > max_freq:
            max_freq = current_freq
            max_index = i

        if current_freq < min_freq:
            min_freq = current_freq
            min_index = i
    s = list(s)
    max_frq_character = s[max_index]
    s[min_index] = max_frq_character

    print("".join(s))
