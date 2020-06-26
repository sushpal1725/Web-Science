
import sys
def sort_by_value(item):
    return item[-1]

def build_dict(filename):
    f = open(filename, 'rU')
    words = f.read().split()
    count = {}

    for word in words:
        word = word.lower()
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

    f.close()
    return count

def print_words(filename):
    dict = build_dict(filename)

    for word in sorted(dict.keys()):
        print word, dict[word]

def print_top(filename):
    count = build_dict(filename)
    i = 0

    items = sorted(count.items(), key=sort_by_value, reverse=True)
    for item in items[:20]:
        print item[0] + ': ' + str(item[1]) + ' times'
        i += 1

def main():
    if len(sys.argv) != 3:
        print 'usage: ./wordcount.py {--count | --topcount} file'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
      print_words(filename)
    elif option == '--topcount':
      print_top(filename)
    else:
      print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
    main()