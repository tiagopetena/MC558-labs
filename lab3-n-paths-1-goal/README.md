# Joaozinho life planning

## Variables

s: start vertex
t: target vertex

Vertex $v_{i}$ is the state at time $i$.

Edge $e_{i,j}$ indicates that it is possible to go from
$state i$ to $state j$.

### Colors

<style>
    g { color: Green }
    y { color: Orange }
    r { color: Red }
</style>

- <g>Green</g>
    Joaozinho did good.
- <y>Yellow</y>
    Joaozinho is neutral.
- <r>Red</r>
    Joaozinho screwed up.

### Next actions
Joaozinho must follow these rules when choosing the next path the boy may take in order to succeed in his life:

- if <g>good</g> :arrow_right: <g>Green</g>, <y>Yellow</y>, <r>Red</r>.
- if <y>neutral</y> :arrow_right: <g>Green</g>, <y>Yellow</y>.
- if <r>bad</r> :arrow_right: <g>Green</g>.

## Goal

Count how many ways Joazinho can take that respect his life rules.

## Input
Text file containing at each line:

- $l_{0}$: n m s t
  - n: number of vertices.
  - m: number of edges.
  - s: starting node. $0 \le s$.
  - t: target node. $t \le n - 1$.
- $l_{1}$ to $l_{m}$: x y c.
  - $m$ lines.
  - x: From vertex x. $x \le s$
  - y: To vertex y. $y \le n - 1$
  - c: Color of the edge. $0 \le c \le 2$
    <g>0</g>: Green, <y>1</y>: Yellow, <r>2</r>: Red.

## Output
The number of possible paths.