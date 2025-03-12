def load_wordlist(filepath="english.txt"):
    """
    从文件中加载 BIP39 单词表，返回一个包含 2048 个单词的列表
    """
    with open(filepath, "r", encoding="utf-8") as f:
        words = [line.strip() for line in f if line.strip()]
    return words

def get_word_from_weights(weights, wordlist):
    """
    根据权位数字列表计算总和，并返回该索引对应的助记词单词
    """
    total = sum(weights)
    if 0 <= total < len(wordlist):
        return total, wordlist[total]
    else:
        return total, "[无效权位总和：超出单词表范围]"

def main():
    wordlist = load_wordlist()
    print("请输入一组权位数字（使用逗号分隔），表示各个位的权重相加的值，程序将该总和视作 BIP39 助记词的索引。")
    print("例如：输入 '1,2,4,8,16' 将得到 1+2+4+8+16=31，对应单词表中索引 31 的单词。")
    print("输入空行退出。")
    
    while True:
        user_input = input("请输入权位数字: ").strip()
        if user_input == "":
            break
        try:
            # 解析输入，转换为整数列表
            weights = [int(x.strip()) for x in user_input.split(",") if x.strip() != ""]
            total, word = get_word_from_weights(weights, wordlist)
            print(f"权位总和为 {total}，对应的助记词为：{word}")
        except ValueError:
            print("输入格式有误，请确保每个权位都是数字，并使用逗号分隔。")

if __name__ == "__main__":
    main()

