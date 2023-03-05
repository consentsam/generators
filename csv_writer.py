import csv


class CSVWriter:
    def __init__(self):
        self.rows = None
        self.file_name = "solution.csv"
        with open(self.file_name, "r") as file:
            file_reader = csv.reader(file)
            self.rows = [_ for _ in file_reader]

    def get_p_values(self):
        return [int(_[0]) for _ in self.rows[1:]]

    def write(self, g_values):
        rows = [self.rows[0]]
        for idx, row in enumerate(self.rows[1:]):
            rows.append([row[0], str(g_values[idx])])

        with open(self.file_name, "w") as file:
            file_writer = csv.writer(file)
            for row in rows:
                file_writer.writerow(row)
