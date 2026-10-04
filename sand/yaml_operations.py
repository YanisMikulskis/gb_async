import yaml

with open('data_read.yaml', 'r') as new_f:
    new_f_content = yaml.load(new_f, Loader=yaml.SafeLoader)
print(new_f_content)



print(f'-----------')
action_list = ['a', 'b', 'c']
to_list = ['1', '2', '3']

data_to_yaml = {'letters': action_list, 'numbers': to_list}

with open('data_read_2.yaml', 'w') as new_f:
    yaml.dump(data_to_yaml, new_f, default_flow_style=True)

with open('data_read_2.yaml', 'r') as new_f:
    print(new_f.read())
