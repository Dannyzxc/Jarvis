# pickle_module_meaning_saving_data_for_future_use
import pickle

cars = ['bmw','mercedise', 'audi']
fileobj = open('my_cars.pkl' , 'wb')
pickle.dump(cars, fileobj)
fileobj.close()

# rading_pickle_data
file = 'my_cars.pkl'
fileobj = open(file, 'rb')
my_car = pickle.load(fileobj)
print(my_car)