# import os
# import regex as re
# from collections import Counter
# 
# 
# def build_concordance(directory_path, extension=".txt", ignore_case=True, regular_expression=r"[^A-Za-z0-9']*"):
# 	concordance = Counter()
# 
# 	for directory, subdirectories, file_list in os.walk(directory_path):
# 		for file_name in file_list:
# 			full_path = os.path.join(directory, file_name)
# 			root, ext = os.path.splitext(full_path)
# 			if ext == extension:
# 				try:
# 					with open(full_path, 'rt', encoding='utf8') as file_object:
# 						contents = file_object.read()
# 				except UnicodeDecodeError:
# 					print("Could not process {}".format(full_path))
# 					continue
# 				if ignore_case:
# 					word_list = [x.lower() for x in re.split(regular_expression, contents)]
# 				else:
# 					word_list = [x for x in re.split(regular_expression, contents)]
# 				concordance.update(word_list)
# 	return concordance
# 
# def build_Python_concordance(directory_path, extension=".py"):
# 	import symtable
# 	concordance = Counter()
# 
# 	for directory, subdirectories, file_list in os.walk(directory_path, followlinks=True):
# 		for file_name in file_list:
# 			full_path = os.path.join(directory, file_name)
# 			root, ext = os.path.splitext(full_path)
# 			if ext == extension:
# 				try:
# 					with open(full_path, 'rt', encoding='utf8') as file_object:
# 						contents = file_object.read()
# 				except UnicodeDecodeError:
# 					print("Could not process {}".format(full_path))
# 					continue
# 				try:
# 					st = symtable.symtable(contents, full_path, "exec")
# 				except SyntaxError as exception:
# 					print("Could not process {} due to {}".format(full_path, exception))
# 					continue
# 				word_list = symbol_list(st)
# 				concordance.update(word_list)
# 	return concordance
# 
# def symbol_list(symbol_table):
# 	import symtable
# 	sl = []
# 	for symbol in symbol_table.get_symbols():
# 		sl.append(symbol.get_name())
# 	for child in symbol_table.get_children():
# 		if isinstance(child, symtable.SymbolTable):
# 			for item in symbol_list(child):
# 				sl.append(item)
# 	return sl
# 
# # D:\Temp\playlists\music\20181218-153123.m3u
# 
# # re.search(r"(,)(\d{1,3}\. )?(.*?)( - )", ll[12]).groups()
# 
# for x in contents:
# 	if x[0:7] != '#EXTINF':
# 	    continue
# 	m = re.search(r"(,)(\d{1,3}\. )?(.*?)( - )", x)
# 	if m:
# 		y = m.group(3).strip().lower()
# 		if y:
# 			cc[y] += 1
# 
# for directory, subdirectories, file_list in os.walk(directory_path):
#     for file_name in file_list:
#         full_path = os.path.join(directory, file_name)
#         with open(full_path, "rt", encoding="windows-1252") as file_object:
#             contents = file_object.readlines()
#         for x in contents:
#             if x[0:7] != '#EXTINF':
#                 continue
#             m = re.search(r"(,)(\d{1,3}\. )?(.*?)( - )", x)
#             if m:
#                 y = m.group(3).strip().lower()
#                 if y:
#                     cc[y] += 1
# 