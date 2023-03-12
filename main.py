from csv_writer import CSVWriter


def find_generator(p):
    # Write your code here
    smallest_prime_number = 2
    for i in range(2,p):
        smallest_prime_number = i;
        set_of_all_generated_numbers = set()
        for j in range(0,p):
            generated_number = pow(i,j,p)
            set_of_all_generated_numbers.add(generated_number)
            if len(set_of_all_generated_numbers)==p-1: # because we have not added 0 here 
                return smallest_prime_number


csv_writer = CSVWriter()
p_values = csv_writer.get_p_values()
g_values = [find_generator(_) for _ in p_values]

csv_writer.write(g_values)