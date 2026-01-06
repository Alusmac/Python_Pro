def main():
    """ Зчитує числа з файлу 'nums.txt', обчислює і виводить їхнє середнє арифметичне.

    """
    filename = "nums.txt"

    try:
        with open(filename) as file:
            nums = [float(line.strip()) for line in file if line.strip()]
        if nums:
            print("Arithmetic mean:", sum(nums) / len(nums))
        else:
            print("There is nothing inside.")
    except FileNotFoundError:
        print(f"I cannot found this '{filename}' file.")
    except ValueError:
        print("In this file I see not only numbers.")


if __name__ == "__main__":
    main()
