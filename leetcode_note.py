# 用户输入 文件名 创建 文件名.md 文件并且保存在对应标签文件夹下
# e.g. python leecode_node.py list_001 
# 在 /home/solejay/program/algorithm_leetcode/list 文件夹下创建 list_001.md 文件
import os
import sys

# 将标题换成 h4 标题
def h4_title(title):
    for i in range(len(title)):
        title[i] = '#### ' + title[i]
    return title

# 给每行末尾添加换行符
def br(write_content):
    for i in range(len(write_content)):
        write_content[i] = write_content[i] + '\n'
    return write_content


if __name__ == '__main__':
    tag_dir = sys.argv[1].split('_')[0]
    filename = sys.argv[1] + '.md'

    # 不存在 tag_dir 时创建
    dir_path = '/home/solejay/program/algorithm_leetcode/' + tag_dir
    if os.path.exists(dir_path):
        pass
    else:
        os.makedirs(dir_path)

    # 进入 tag_dir 文件夹创建文件
    os.chdir(dir_path)

    # try catch 判断文件是否已经存在,不存在时生成 md 文件
    try:
        os.mknod(filename)
    except FileExistsError:
        print('文件已存在！')
    else:
        step = ['原题目', '思路', '第一遍解法', '网上好的解法',
                '自己可以改进的地方', '最简代码', '获得的思考']
        step = h4_title(step)
        problem_type = '**难度**'
        code_input = '```python\n```'
        
        write_content = [step[0], problem_type, step[1], 
                        step[2], code_input, step[3], code_input, 
                        step[4], code_input, step[5], code_input, step[6]]

        write_content = br(write_content)

        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(write_content)






    