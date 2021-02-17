def funWithAnagrams(text):
    # Write your code here
    cs= set()
    ans= []
    for t in text:
        tt=tuple(sorted(list(t)))
        if not tt in cs:
            ans.append(t)
            cs.add(tt)
    return sorted(ans)

if __name__ == '__main__':
    text_count = int(input().strip())

    text = []

    for _ in range(text_count):
        text_item = input()
        text.append(text_item)

    result = funWithAnagrams(text)
