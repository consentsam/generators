# Do not change the code in this file

import hashlib

correct_solution_hash = "91ef5a137e169353f5894776fd0c8692"
solution_hash = hashlib.md5(open("solution.csv", "r").read().encode()).hexdigest()

assert(solution_hash == correct_solution_hash)
