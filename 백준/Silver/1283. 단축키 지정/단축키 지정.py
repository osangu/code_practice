N = int(input())

key_dict = {}
word_list = [input().split() for i in range(N)]

for ind, words in enumerate(word_list):
    retry = True
    reretry = True

    for i in range(len(words)):
        first_alpha = words[i][0]

        if key_dict.get(first_alpha.lower()) is None:
            key_dict[first_alpha.lower()] = True

            word_list[ind][i] = "[" + first_alpha + "]" + words[i][1:]

            print(' '.join(word_list[ind]))
            retry = False
            break

    if not retry:
        continue
    # print(words, 'retry')

    for i in range(len(words)):
        should_break = False
        for j, alphabet in enumerate(words[i]):
            if key_dict.get(alphabet.lower()) is None:
                key_dict[alphabet.lower()] = True

                word_list[ind][i] = words[i][:j]+ "[" + words[i][j] + "]" + words[i][j + 1:]

                print(' '.join(word_list[ind]))

                reretry, should_break = False, True
                break

        if should_break:
            break
    # print(words, 'reretry')
    if not reretry:
        continue

    print(' '.join(words))
