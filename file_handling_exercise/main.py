from os import walk
files_by_ex = {}
for _, _, files in walk('.'):
    for file in files:
        extension = file.split(".")[-1]
        if extension not in files_by_ex:
            files_by_ex[extension] = []
        files_by_ex[extension].append(file)
with open("result.txt", "w") as output:

    for extension, files in sorted(files_by_ex.items()):
        output.write(f'.{extension}\n')
        for file in sorted(files):
            output.write(f'- - - {file}\n')
# === ALTERNATIVE SOLUTION ===
# from os import listdir, path
#
#
# def traverse_dir(current_path, files_ext):
#     for element in listdir(current_path):
#         if path.isdir(path.join(current_path, element)):
#             traverse_dir(path.join(current_path, element), files_ext)
#         else:
#             extension = element.split(".")[-1]
#             if extension not in files_ext:
#                 files_ext[extension] = []
#             files_ext[extension].append(element)
#
# files_by_ext = {}
# traverse_dir('.', files_by_ext)
#
# for ext, files in sorted(files_by_ext.items()):
#     print(f'.{ext}')
#     for file in sorted(files):
#         print(f'- - - {file}')
