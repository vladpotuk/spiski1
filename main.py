def calculate_sum_and_average(list_of_numbers):
    sum=0
    for number in list_of_numbers:
        sum +=number
    average = sum/len(list_of_numbers)
    return sum, average
if __name__ == "__main__":
    list_of_numbers = []
    while True:
        number = input("Введіть число :  ")
        if number == "":
            break
        list_of_numbers.append(int(number))
sum, average = calculate_sum_and_average(list_of_numbers)
print("Сума всіх елементів списку: {}".format(sum))
print("Середньоарифмітичне всіх елементів списку: {}".format(average))
