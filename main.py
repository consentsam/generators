from csv_writer import CSVWriter


def find_generator(p):
    # Write your code here
    pass


csv_writer = CSVWriter()
p_values = csv_writer.get_p_values()
g_values = [find_generator(_) for _ in p_values]

csv_writer.write(g_values)
