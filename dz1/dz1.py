def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                _, salary = line.strip().split(',')
                salaries.append(float(salary))

        total = sum(salaries)
        average = total / len(salaries) if salaries else 0
        return total, average

    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None


path_to_file = 'dz1/salaries.txt'
result = total_salary(path_to_file)
print(f"Total Salary: {result[0]}, Average Salary: {result[1]}")
