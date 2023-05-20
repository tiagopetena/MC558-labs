# Advenventure world

Test some games. Decide which are possible to win or not.

## Input

Starting Points: 100
Room Points ($w_i$): $-100 \le w_i \le 100$

Rooms($0 \le n \le n-1$)
Spawn Room: $0$
Final Room: $n - 1$
$w_0=w_{n-1}=0$

### 1st Line

n: number of rooms

### 2nd Line

n integers($w_0, ... ,w_{n-1}$): $w_i$ energy of room $i$. $-100 \le w_i \le 100$.

### 3rd Line

m number of doors.

### m Lines

u v: door from u to v.

## Goal

Decide if you can reach target room without dying(reaching 0 energy).
CAN REPEAT ROOMS.

## Output

possible or impossible.
