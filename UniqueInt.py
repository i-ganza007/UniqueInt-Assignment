def UniqueInt(sample_file: str):
    unique = []
    try:
        with open(sample_file, 'r') as f:
            for line in f:
                line = line.strip()  
                if line == "":
                    continue  
                ind_list = line.split()
                for ind in ind_list:
                    try:
                        num = int(ind)
                        if num not in unique:
                            unique.append(num)
                    except ValueError:
                        
                        continue

        filename = sample_file.split('/')[-1].split('.')[0]
        result_file = f"sample_results/{filename}_results.txt"

        
        unique.sort()

        with open(result_file, "w") as j:
            for num in unique:
                j.write(num + "\n")  

    except FileNotFoundError as e:
        print(f'{sample_file} is not found\n', e)
    except SyntaxError:
        pass




    


