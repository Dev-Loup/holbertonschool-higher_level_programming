# Hello World: python project

Hello world python introduces basic concepts of python and python scripting 

## Topics
* What is python?
* Zen of Python
* Python interpreter
* `print()` function in python
* python strings
* Indexing and slicing
* `pep8` code style.
## Recomendations

### About C Coding

* Projects were checked with gcc 4.8.4 using -Werror -Wall -Wextra -pedantic even if it´s not necessary using the flags test your code is correctly written and there are no potencial mistakes
* Betty code style is the standard code style, you can get [the betty checker here](https://github.com/holbertonschool/Betty/wiki) and documentation about using it in different text editors
* All your files must end with a new line
### About Python scripting
* Projects are checked with `python3`
* All your files must end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* Code style is checked using `pep8 1.7`
### General
* while working in your own repo remember to write a README.md, more information about [writting README's is here](https://www.makeareadme.com/)
* Using global variables is not allowed
## Tasks
### 0. Run Python file
Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable `$PYFILE`
```shell
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Holberton School")

user@ubuntu:~/py/0x00$ export PYFILE=main.py
user@ubuntu:~/py/0x00$ ./0-run
Holberton School
user@ubuntu:~/py/0x00$
```
### 1. Run inline
Write a Shell script that runs a Python script.

The Python code will be saved in the environment variable `$PYCODE` 
```shell
guillaume@ubuntu:~/py/0x00$ export PYCODE='print("Holberton School: {}".format(88+10))'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Holberton School: 98
guillaume@ubuntu:~/py/0x00$
```
### 2. Hello, print

Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.

* Use the function `print`
### 3. Print integer

Complete the source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

* You can find the source code here
```shell
#!/usr/bin/python3
number = 98
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
```
* The output of the script should be:
* __the number, followed by `Battery street`,
* __followed by a new line
* You are not allowed to cast the variable `number` into a string
* Your code must be 3 lines long
* You have to use the new print numbers [tips](https://pyformat.info/#number) (with `.format(...)`)
### 4. Print float
Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

* You can find the source code here
```shell
#!/usr/bin/python3
number = 3.14159
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
```
* The output of the program should be:
* __`Float:`, followed by the float with only 2 digits
* __followed by a new line
* You are not allowed to cast `number` to string
* You have to use the new print numbers [tips](https://pyformat.info/#number) (with `.format(...)`)
### 5. Print string

Complete the source code in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.

* You can find the source code here
```shell
#!/usr/bin/python3
str = "Holberton School"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
```
* The output of the program should be:
* __3 times the value of `str`
* __followed by a new line
* __followed by the 9 first characters of `str`
* __followed by a new line
* You are not allowed to use any loops or conditional statement
* Your program should be maximum 5 lines long

### 6. Play with strings

Complete the source code to print Welcome to Holberton School!

* You can find the source code here
```shell
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print("Welcome to {}!".format(str1))
```
* You are not allowed to use any loops or conditional statements.
* You have to use the variables `str1` and `str2` in your new line of code
* Your program should be exactly 5 lines long

### 7. Copy - Cut - Paste

Complete this source code

* You can find the source code here
```shell
#!/usr/bin/python3
word = "Holberton"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))
```
* You are not allowed to use any loops or conditional statements
* Your program should be exactly 8 lines long
* `word_first_3` should contain the first 3 letters of the variable `word`
* `word_last_2` should contain the last 2 letters of the variable `word`
* `middle_word` should contain the value of the variable `word` without the first and last letters

### 8. Create a new sentence

Complete the source code to print object-oriented programming with Python, followed by a new line.

* You can find the source code here
```shell
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(str)
```
* You are not allowed to use any loops or conditional statements
* Your program should be exactly 5 lines long
* You are not allowed to create new variables
* You are not allowed to use string literals

### 9. Easter Egg

Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

* Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)

### 10. Linked list cycle
Write a function in C that checks if a singly linked list has a cycle in it.

* Prototype: int check_cycle(listint_t *list);
* Return: 0 if there is no cycle, 1 if there is a cycle
Requirements:
* Only these functions are allowed: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`

* files needed:
lists.h

```c
#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
```
10-linked_lists.c
```c
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = *head;
    *head = new;

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
```
main.c
```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;
    listint_t *current;
    listint_t *temp;
    int i;

    head = NULL;
    add_nodeint(&head, 0);
    add_nodeint(&head, 1);
    add_nodeint(&head, 2);
    add_nodeint(&head, 3);
    add_nodeint(&head, 4);
    add_nodeint(&head, 98);
    add_nodeint(&head, 402);
    add_nodeint(&head, 1024);
    print_listint(head);

    if (check_cycle(head) == 0)
        printf("Linked list has no cycle\n");
    else if (check_cycle(head) == 1)
        printf("Linked list has a cycle\n");

    current = head;
    for (i = 0; i < 4; i++)
        current = current->next;
    temp = current->next;
    current->next = head;

    if (check_cycle(head) == 0)
        printf("Linked list has no cycle\n");
    else if (check_cycle(head) == 1)
        printf("Linked list has a cycle\n");

    current = head;
    for (i = 0; i < 4; i++)
        current = current->next;
    current->next = temp;

    free_listint(head);

    return (0);
}
```
### 100. Hello, write (Advanced task)
Write a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.

* Use the function `write` from the `sys` module
* You are not allowed to use `print`
* Your script should print to `stderr`
* Your script should exit with the status code `1`
* (Dora Korpar was a Holberton student in Cohort 0 of San Francisco)

### 101. compile

Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable `$PYFILE`

The output filename has to be `$PYFILEc` (ex: `export PYFILE=my_main.py` => output filename: `my_main.pyc`)

### 102. ByteCode -> Python #1 (Advanced Task)
**THIS TASK IS IN DEVELOPMENT**

## License
All exercises were designed by [holberton School](https://holbertonschool.com/)
