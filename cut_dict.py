import argparse
import json
parser = argparse.ArgumentParser()
parser.add_argument("-count", type=int,
                    help="count words in stack")
parser.add_argument("file", type=str,
                    help="filename dictionary")
args = parser.parse_args()
count_words = args.count
file_ = args.file


# print(count_words)

with open(file_, 'r') as dict:
    count = 0
    dict_list = []
    for _ in range(count_words):
        stack = dict.readline().split(';')
        count += 1
        out_name = 'dict.json'
        with open(out_name, 'w', encoding='utf8') as out:
            dict_list.append(stack[:2])
            json.dump(dict_list, out, ensure_ascii=False)
        for _ in range(count_words):
            stack = dict.readline().split(';')
            count += 1
            with open('count_50' + out_name, 'w+', encoding='utf8') as out:
                dict_list.append(stack[:2])
                json.dump(dict_list, out, ensure_ascii=False)
print(dict_list)