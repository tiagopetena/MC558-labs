#!/bin/zsh

for input in `ls -1 tests/*in`;
do
    IND=$((IND+1))
    fname=${input/tests/}
    outpa=${fname/in/out}
    python3 lab1.py < "$input" > outputs/"$outpa"
    diff -q outputs"$outpa" tests"$outpa"
done

