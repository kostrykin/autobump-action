from datetime import datetime


year = datetime.now().year

with open('.github/test.txt', 'w') as file:
    file.write(f'Test {year - 1} Test')

with open('.github/test.md', 'w') as file:
    file.write(f'Test {year - 1} Test')