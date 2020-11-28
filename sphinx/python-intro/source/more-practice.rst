Practice, Practice, Practice
============================

Here are some more exercises for you to solve to practice your Python skills.

Similarity
----------

A ``bitstring`` is a string with only *1* and *0* values. Here are some examples.

- 1000100
- 0011101
- 1111000

We can compute the ``similarity`` of two bitstrings by comparing all the corresponding characters. For any two bitstrings, denote the following.

- Let ``n_11`` or ``a`` be the number of times two corresponding characters are both *1* and *1*.
- Let ``n_10`` or ``b`` be the number of times two corresponding characters are *1* and *0*.
- Let ``n_01`` or ``c`` be the number of times two corresponding characters are *0* and *1*.
- Let ``n_00`` or ``d`` be the number of times two corresponding characters are *0* and *0*.

The similarity score, :math:`s(x_1, x_2)`, of two bitstrings, :math:`x_1` and :math:`x_2`, is defined as follows.

:math:`s(x_1, x_2) = \frac{a}{a + b + c}`

Below, we show how to calculate the similarity of two bitstrings.

- :math:`x_1`: 1000100
- :math:`x_2`: 0011101

.. list-table:: Similarity Calcuation Example
    :header-rows: 1

    * - Character Index
      - :math:`x_1`
      - :math:`x_2`
      - :math:`a`
      - :math:`b`
      - :math:`c`
      - :math:`d`
    * - 0
      - 1
      - 0
      - 0
      - 1
      - 0
      - 0
    * - 1
      - 0
      - 0
      - 0
      - 0
      - 0
      - 1
    * - 2
      - 0
      - 1
      - 0
      - 0
      - 1
      - 0
    * - 3
      - 0
      - 1
      - 0
      - 0
      - 1
      - 0
    * - 4
      - 1
      - 1
      - 1
      - 0
      - 0
      - 0
    * - 5
      - 0
      - 0
      - 0
      - 0
      - 0
      - 1
    * - 6
      - 0
      - 1
      - 0
      - 0
      - 1
      - 0
    * - Total
      - 
      - 
      - 1
      - 1
      - 3
      - 2

With :math:`a=1, b=1, c=3, d=4`, the similarity of these two bitstrings are :math:`s(x_1, x_2) = \frac{1}{1 + 1 + 3} = \frac{1}{5} = 0.2`.

Why are bitstrings important? What are their industrial utilities? Let's look at a seemingly simple use. Imagine that a bitstring represents the collection of books that a person has read; each position in this bitstring corresponds to a book. Let's say we have 5 people and we know which books they have read; we can represent the books read by each person as a bitstring. 

.. list-table:: Bitstring Representation of Books Read
    :header-rows: 1

    * - Name
      - bitstring
    * - John
      - 1000100
    * - Jack
      - 0011101
    * - Mary
      - 1111000
    * - Cindy
      - 1100100
    * - Mariah
      - 1000111

If we have a new person, Abdul, and we know which books he has read, we can recommend other books to him based on similarity. First, we would calculate how similar Abdul is to each of the other users and sort the result descendingly. Then, starting with the first person most similar to Abdul, we would see which books Abdul has not read in that person's collection of read books, and recommend those books to Abdul.

Exercise 1
^^^^^^^^^^

Write a function to compute the similarity between two bitstrings. Compute the pairwise similarities for the following bitstrings.

.. code:: python

    john = '1000100'
    jack = '0011101'
    mary = '1111000'
    cindy = '1100100'
    maria = '1000111'

You should have a total of :math:`{{5}\choose{2}}=10` similarities computed. Which two pair of readers are most similar? Which two pair of readers are least similar? 

Exercise 2
^^^^^^^^^^

Let's say Abdul has the following bitstring representation for the books he has read.

.. code:: python 

    abdul = '0100001'

Which person (from above) is Abdul most similar to in terms of books read? Which person is Abdul least similar to?

Exercise 3
^^^^^^^^^^

Each bitstring is only 7 characters long and each position in the bitstring represents the following books.

.. list-table:: Bitstring Representation of Books Read
    :header-rows: 1

    * - Position
      - Title
    * - 0
      - For Whom the Bell Tolls
    * - 1
      - The Great Gatsby
    * - 2
      - A Tale of Two Cities
    * - 3
      - To Kill a Mockingbird
    * - 4
      - The Catcher in the Rye
    * - 5
      - Of Mice and Men
    * - 6
      - Pride and Prejudice

Which books would you recommend to Abdul to read based on what he has read in the past and his similarity to other readers?

Rock Paper Scissor
------------------

The class game of Rock Paper Scissor ``RPS`` is played between two people. Each round, each of the players picks either rock, paper or scissor. The rules for win, lose or tie is as follows.

- If both players pick the same item (e.g. rock and rock), then the outcome is a tie.
- Rock always beats scissor.
- Scissor always beats paper.
- Paper always beats rock.

Write a terminal-based game of ``RPS`` where a user gets to challenge the computer. The game should loop endlessly and handle the situation when a user wants to quit. Before the game ends, the user should have information of the number of times they have won, total games played and percentage of wins. On each round, let the user pick rock, paper or scissor, and then randomly let the computer pick as well. Compute the result for the user (win, lose or tie). Always show what the user and computer picked as well as the result each time.