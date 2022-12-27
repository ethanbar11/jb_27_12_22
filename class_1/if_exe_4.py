gender = input('Please enter y for male, any other character for female: ')
first_name = input('Please enter your first name:  ')
last_name = input('Please enter your last name:  ')
if gender == 'y':
    print('Nice to meet your Mr.', first_name, last_name)
else:
    print('Nice to meet your Mrs.', first_name, last_name)
