def load_word_list(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"文件 '{filename}' 未找到。请确保文件存在并位于正确的路径。")
        return None

def get_word_info(word, word_list):
    try:
        # 查找单词的编号
        index = word_list.index(word)
        # 将编号转换为11位二进制字符串
        binary_representation = f"{index:011b}"
        # 定义位权列表
        weights = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
        # 计算对应的位权组合
        bit_positions = [weights[i] for i in range(11) if binary_representation[10 - i] == '1']
        return index, bit_positions
    except ValueError:
        return None, None

def main():
    # 加载助记词表
    word_list = load_word_list('english.txt')
    if word_list is None:
        return

    # 提示用户输入单词
    word = input("请输入一个英文单词：").strip()
    if not word:
        print("输入不能为空。")
        return

    # 获取单词信息
    index, bit_positions = get_word_info(word, word_list)
    if index is not None:
        print(f"单词 '{word}' 的编号是 {index}")
        print(f"对应的位权组合是: {bit_positions}")
    else:
        print(f"单词 '{word}' 不在助记词表中")

if __name__ == "__main__":
    main()

