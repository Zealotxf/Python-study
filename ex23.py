import sys
script, encoding,  error = sys.argv                                             #解码，错误


def main(language_file, encoding, errors):                                      #主函数
    line = language_file.readline()                                             #读取文件中的一行

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding = "utf-8")

main(languages, encoding, error)
