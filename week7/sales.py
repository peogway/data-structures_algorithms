def sales(cars, customers):
    sorted_cars = sorted(cars)
    sorted_cus = sorted(customers)
    # print(sorted_cars)
    # print(sorted_cus)
    res = 0
    pos_car = len(sorted_cars) -1
    pos_cus = len(sorted_cus) -1
    while True:
        # print('cus:', sorted_cus[pos_cus], pos_cus, 'car:',sorted_cars[pos_car], pos_car)
        if pos_car<0 or pos_cus<0:
            
            break
        if sorted_cus[pos_cus]>=sorted_cars[pos_car]:
            res+=1
            pos_cus-=1
            pos_car-=1
        else:
            if pos_car<=0: break
            while pos_car>0 and sorted_cus[pos_cus]<sorted_cars[pos_car]:
                pos_car-=1
        
    return res


if __name__ == "__main__":
    print(sales([20, 10, 15], [11, 25, 15]))
    print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))
    print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))
    print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))