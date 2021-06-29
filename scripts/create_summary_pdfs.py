import os



data_dir='../data/'
for dir in os.listdir(f'{data_dir}train/'):
    if not dir.startswith('.'):
        os.system(f'cd {data_dir}train/{dir} && convert *.png {dir}_train.pdf && mv {dir}_train.pdf ../')

for dir in os.listdir(f'{data_dir}val/'):
    if not dir.startswith('.'):
        os.system(f'cd {data_dir}val/{dir} && convert *.png {dir}_val.pdf && mv {dir}_val.pdf ../')

for dir in os.listdir(f'{data_dir}label_book/'):
    if not dir.startswith('.'):
        os.system(f'cd {data_dir}label_book/{dir} && convert *.png {dir}_label_book.pdf && mv {dir}_label_book.pdf ../')

