#Lists
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[2])
print(bicycles[2].title())
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove('yamaha')
print(motorcycles)

#organizing a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

#prints the number of items in the list
print(len(cars))
#prints the original list after being sorted
print(sorted(cars))

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])
#example of index error
empty_list = []
print(empty_list[-1])


#Chapter 4 - working with lists





