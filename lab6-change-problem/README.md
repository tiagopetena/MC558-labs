# Change Problem

Coins still exist?

Given exchange value; Give coins with minimum weight.

## Input
n: coin kinds.
$v_i$: value
$p_i$: weight
$q_i$: stock.
$Q$: exchange value.

## Goal

minimize:
$\sum{p_i}{x_i}$

subject to:
$\sum{v_i}{x_i} = Q$
$x_i \in {0,1,..., q_i}\forall i=1,...,n$

## Output

number of coins of each value that sum up to a minimum weight.