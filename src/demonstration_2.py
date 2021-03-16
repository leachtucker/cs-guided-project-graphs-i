"""
In a town, there are `N` people labelled from `1` to `N`.  There is a rumor
that one of these people is secretly the town judge.

If the town judge exists, then:

1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.

You are given `trust`, an array of pairs `trust[i] = [a, b]` representing that
the person labelled a trusts the person labelled `b`.

If the town judge exists and can be identified, return the label of the town
judge.  Otherwise, return `-1`.

Example 1:

```plaintext
Input: N = 2, trust = [[1,2]]
Output: 2
```

Example 2:

```plaintext
Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
```

Example 3:

```plaintext
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
```

Example 4:

```plaintext
Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
```

Example 5:

```plaintext
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
```

Constraints:

- `1 <= N <= 1000`
- `0 <= trust.length <= 10^4`
- `trust[i].length == 2`
- `trust[i]` are all different
- `trust[i][0] != trust[i][1]`
- `1 <= trust[i][0], trust[i][1] <= N`
"""
def find_judge(N, trust):
    """
    Inputs:
    N -> int
    trust -> List[List[int]]

    Output:
    int
    """
    # Your code here
    # N people in the town. Labeled from 1-N
    trustedPeople = [[0]*N for _ in range(N)]

    for relationship in trust:
        personA = relationship[0]
        personB = relationship[1]

        # update trustedPeople matrix
        trustedPeople[personA-1][personB-1] = 1

    for i in range(len(trustedPeople)):
        person = trustedPeople[i]

        print(f'Person: {i+1}. Trusted: {person}')

        counter = 0
        for personB in trustedPeople:
            if personB[i] == 1:
                counter += 1


        if person.count(0) == N and counter == N-1:
            return i+1

    return -1




print(find_judge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))

print(find_judge(3, [[1,2],[2,3]]))

print(find_judge(3, [[1,3],[2,3],[3,1]]))

print(find_judge(3, [[1,3],[2,3]]))

print(find_judge(2, [[1,2]]))


