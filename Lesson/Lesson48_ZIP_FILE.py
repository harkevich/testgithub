# import zipfile
# import os
#
# # zip = input("Введите название папки(Путь к папке): ")
# z = zipfile.ZipFile("folder.zip")
# for root, dirs, files in os.walk('folder'):
#     for file in files:
#         z.write(os.path.join(root,  files))
# z.close()
#------------------------------------------------------
import zipfile
import os
forlder_path = 'D:\\Python\\Project2\Folder'
zip_path = 'D:\\Python\\Project2\Folder\\test.zip'
zip_name = 'test.zip'
my_zip  = zipfile.ZipFile(zip_path, 'w')

for folder, subfolder, files in os.walk(forlder_path):
    for file in files:
        if file == zip_name:
            continue
        my_zip.write(os.path.join(folder, file),
                     os.path.relpath(os.path.join(folder, file), forlder_path),
                     compress_type=zipfile.ZIP_DEFLATED)



my_zip.close()


#------------------------------------------------------
#
# def read_dir(folder):
#     for root, dirs, files in os.walk(folder):
#         # print(root, dirs, files)
#         level = root.count(os.sep)
#         indent = ' ' * 4 * level
#         print(f'{indent}[{os.path.basename(root)}]')
#         sub_indent = ' ' * 4 * (level + 1)
#         # print(root, files, level, indent,sub_indent)
#         for file in files:
#             print(f'{sub_indent} {file}')
#
# read_dir('folder')