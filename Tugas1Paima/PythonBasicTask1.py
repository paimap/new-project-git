def find_average(numbers: list): #fungsi mencari nilai rata-raya
    sum = 0
    for num_list in numbers:
        sum += num_list
    average = sum/len(numbers)
    return average

if __name__ == "__main__":
    print(find_average([1,2,3,4,5]))