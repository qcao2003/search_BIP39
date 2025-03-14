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
    # 定义允许的权位集合
    allowed_set = {1, 2, 4, 8, 16, 32, 64, 256, 512, 1024}
    
    # 加载 BIP39 单词表
    wordlist = load_wordlist()
    
    print("请输入一组权位数字（仅允许以下数字：1,2,4,8,16,32,64,256,512,1024），")
    print("数字间以逗号分隔。例如：输入 '1,2,4,8,16' 将得到 1+2+4+8+16=31，对应单词表中索引 31 的单词。")
    print("输入空行退出。")
    
    while True:
        user_input = input("请输入权位数字: ").strip()
        if user_input == "":
            break
        try:
            # 解析输入，转换为整数列表
            weights = [int(x.strip()) for x in user_input.split(",") if x.strip() != ""]
            # 检查输入数字是否都在允许的集合内
            if not all(num in allowed_set for num in weights):
                print("输入的数字必须是以下这些之一：1, 2, 4, 8, 16, 32, 64, 256, 512, 1024")
                continue
            
            total, word = get_word_from_weights(weights, wordlist)
            print(f"权位总和为 {total}，对应的助记词为：{word}")
        except ValueError:
            print("输入格式有误，请确保每个权位都是数字，并使用逗号分隔。")

if __name__ == "__main__":
    main()

