# Generators

Every element of a finite field Fp can be used to make a subgroup H under repeated action of multiplication. In other words, for an element g: H = {g, g^2, g^3, ...}

A generator of Fp is an element whose subgroup H = Fp, i.e., every element of Fp, can be written as g^n mod p for some integer n.

**Given a finite field with a prime number `p` find the smallest element generator `g` which is a primitive element of Fp.**

## Steps

* Complete the `find_generator` function. Given a prime number `p`, the function should return the smallest generator element.

## Evaluation

-   Clone this repo.

    ```
    git clone CLONE_URL
    ```
    
-   Create a new branch with your name. You can use the following command

    ```
    git checkout -b my-name
    ```

-   Make changes to the [main.py](main.py) file

-   Run the [main.py](main.py) file. This is required to populate the [solution.csv](solution.csv) file 
    ```
    python3 main.py
    ```

-   Create a pull request from your branch to the main branch of the repo to run the github workflow.
