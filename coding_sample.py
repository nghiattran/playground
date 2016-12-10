# def solution(arr):
#     dict = {0 : 0}
#
#     for index in range(1, len(arr)):
#         dict[index] = dict[index - 1] + arr[index - 1]
#     total = dict[len(arr) - 1] + arr[index]
#     for index in range(len(arr)):
#         right = total - dict[index] - arr[index]
#         if right == dict[index]:
#             return index
#     return -1
import math

# def solution(X):
#     x_string = str(X)
#     for index in range(len(x_string)):
#         if index == len(x_string) - 2:
#             average = str(int(math.ceil((float(x_string[index]) + float(x_string[index + 1])) / 2)))
#             return int(x_string[: len(x_string ) - 2] + average)
#         elif x_string[index] < x_string[index + 1]:
#             average = str(int(math.ceil((float(x_string[index]) + float(x_string[index + 1])) / 2)))
#             x_string = '{0}{1}{2}'.format(x_string[:index], average, x_string[index + 2:])
#             return  int(x_string)
#         if x_string[index] > x_string[index + 1]:
#             continue
# # 623315
# print(solution(623315))

def solution(S):
    file_name = ''
    stack = [0, 0]
    longest = 0
    level = 1
    for char in S:
        if char == ' ':
            level += 1
        elif char == '\n':
            print(level, stack, level - 1)
            if is_image(file_name):
                longest = max(longest, stack[level - 1])
            if level == len(stack):
                stack[level] = stack[level - 1] + len(file_name)
            elif level - 1 > len(stack):
                stack.append(stack[level - 1] + len(file_name))
            else:
                if level == 1:
                    stack[level] = len(file_name)
                else:
                    stack[level] = stack[level - 1] + len(file_name)

            level = 1
            file_name = ''
        else:
            file_name += char
    return longest

def is_image(filename):
    print(filename)
    return filename.endswith('jpg')

def getLongestPath(filesys):
  list = filesys.splitlines();  # Parse the string into list
  st = [-1]; #-1 to cancel the path separator before root dir
  lastLevel = -1;  # depth of the last item in st
  maxLen = 0;
  for item in list:
    bareName = item.lstrip('\t');	# Strip leading '\t's
    curLevel = len(item)-len(bareName);	# Use number of '\t's to find level
    while (curLevel <= lastLevel): # cd .. to the same level as "item"
      st.pop();
      lastLevel -= 1;
    st.append(len(bareName)+st[-1]+1);	# accumulated lenth, +1 for pathsep
    lastLevel=curLevel;
    if ('.' in item): 	# Only count "files" with an extension
      maxLen = max(maxLen, st[-1]);
  return maxLen;

def check(s):
    files = s.split('\n')
    sum =0
    space = 0
    for index in range(len(files) - 1, 0, -1):
        line = files[index]
        print(line)
        if '.gif' in line or '.jpef' in line:
            space = len(line) - len(line.lstrip())
        if space > len(line) - len(line.lstrip()):
            sum +=  len(line.lstrip()) + 1
            space -= 1
    return sum

string = 'dir1\n' \
         ' dir2\n' \
         '  sad.gif\n' \
         'dir2\n' \
         ' dir213\n' \
         '  hello.giwdhaisi'

print(getLongestPath(string))