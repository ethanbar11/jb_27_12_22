lst = [1, 9, ['new', 'list', 'here'], -5]

just_a_dict = {'Rotem': 100, ' Omry': 90, 'Shoshi': 30, 'Baruch': 80}
print(just_a_dict['Baruch'])
just_a_dict['Ethan'] = 10
print(just_a_dict['Ethan'])
for key, val in just_a_dict.items():# [['Rotem',100],['Omry',90],['Shoshi',30]...]
    if val >= 90:
        print('The student',key,'got over 90. His grade is',val)
    # print('The key is', key, 'The val is', val)
