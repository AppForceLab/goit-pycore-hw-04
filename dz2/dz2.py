def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_info = {
                        'id': parts[0],
                        'name': parts[1],
                        'age': parts[2]
                    }
                    cats.append(cat_info)
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return cats

cats_info = get_cats_info("dz2/cats.txt")
print(cats_info)
