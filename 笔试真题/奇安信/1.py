def solve(string):
    input_str = string
    word_list = input_str.strip().split()
    print(word_list)
    ans = []
    delete_words = []
    for word in word_list:
        if word == 'undo':
            if ans:
                delete_words.append(ans.pop())
        elif word == 'redo':
            if delete_words:
                ans.append(delete_words.pop())
        else:
            ans.append(word)

    print(' '.join(ans))

if __name__ == "__main__":
    solve("undo undo hello world redo redo")