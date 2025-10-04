sample_input = '''3
1 2 1
3 2 1
1 3 1'''

cleaned_input = list(map(lambda x: list(map(int, x.split())), sample_input.split('\n')))

input_ = cleaned_input[1:]

SHELL_NUM = 3

correct = [0 for i in range(SHELL_NUM)]

for i in range(SHELL_NUM):
    true_shell_placement = [True if a == i else False for a in range(SHELL_NUM)]
    true_shell_placement[i] = True

    for z in input_:
        true_shell_placement[z[0] - 1], true_shell_placement[z[1] - 1] = true_shell_placement[z[1] - 1], true_shell_placement[z[0] - 1]

        if true_shell_placement[z[2] - 1]:
            correct[i] += 1 

print(max(correct))