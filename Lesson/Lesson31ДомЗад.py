import os
import os.path
# def test(p):
#     for r, d, f in os.walk(p):

# tree = os.walk('Folder')
# for files in tree:
#     print(files)
#

def read_dir(folder):
    for root, dirs, files in os.walk(folder):
        # print(root, dirs, files)
        level = root.count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}[{os.path.basename(root)}]')
        sub_indent = ' ' * 4 * (level + 1)
        # print(root, files, level, indent,sub_indent)
        for file in files:
            print(f'{sub_indent} {file}')

read_dir('folder')