print("Welcome to the Employee Pay program!")
id_num = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010']
hours = ['Mary', 'John', 'Bob', 'Mel', 'Jen', 'Sue', 'Ken', 'Dave', 'Beth', 'Ray']
rate = [15, 22, 35, 43, 17, 29, 40, 20, 37, 16]
hours = [40, 25, 4, 62, 33, 45, 36, 17, 37, 80]
overtime = []

for hour in hours:
        if hour > 40:
                overtimeRate = 1.5 * int(rate)
                overtime = (hour - 40) * overtimeRate
                hours = 40
                print(overtimeRate)
        else:
                print(rate)




