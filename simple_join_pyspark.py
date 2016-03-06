
def split_fileA(line):
    line = line.strip()
    word_count = line.split(',')
    return (word_count[0], int(word_count[1]))


def split_fileB(line):
    # split the input line into word, date and count_string
    line = line.strip()
    key_value = line.split(',')
    date_word = key_value[0].split(' ')
    word = date_word[1]
    date = date_word[0]
    count_string = key_value[1]
    return (word, date + " " + count_string)


if __name__ == '__main__':
    test_line = "able,991"
    print split_fileA(test_line)

    test_line = 'Jan-01 able,5'
    print split_fileB(test_line)

