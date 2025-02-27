from mnemonic import Mnemonic

def find_word_index(word):
    # 创建BIP-39助记词对象
    mnemo = Mnemonic("english")
    
    # 获取BIP-39字典
    word_list = mnemo.wordlist
    
    # 查找单词的索引
    if word in word_list:
        return word_list.index(word)
    else:
        raise ValueError(f"单词 '{word}' 不在BIP-39字典中")

def main():
    word = input("请输入一个助记词单词: ")
    
    try:
        # 查找助记词的索引
        index = find_word_index(word)
        print(f"单词 '{word}' 在BIP-39字典中的序列号是: {index}")
    
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

