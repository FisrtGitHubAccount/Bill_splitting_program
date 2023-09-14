# Bill_splitting_program

**Note:** This code was written as my very first Python project. It turns out there is a recentll adopted mobile application called Splitwise that solves the same problem. I guess you can all this work as Python version of Splitwise...

Have you ever experienced difficulties in trasnferring money between a group of friends?

If there is only one person paying, the solution is trivial, which is everyone transferring the appropriate amount to the payer.
However, things get complicated when there is more than one person paying for the shared expenses. The simplest solution will become increasing more inefficent in that everyone is trasnferring money back and forth.

Moreover, some people might not participate in every event so some are supposed to pay less than others. This program was written to overcome the complicated bill splitting problems that are common than you'd think.

# Summary of code

1. Get the number of people and their names
2. Creating a ledger_array to record all the expenses for each individual where negative numbers represent money out and positive for expenses unpaid by the corresponding name
3. Separate inputs into two main categories which are

- "For all" = expenses participated by everyone

- "For some" = expenses participated by only some people (will be asked for more details later)

4. Minimise the number of the total transactions by using the greedy algorithm.
