"""
The code for muffin queen first scans the preferences of each judge as separate
lists and stores them in another list without the zeros at the end.
Then the "test" function is called from the main function.
It first tests if there is a muffin that all judges like by checking the 
intersection of set 'shared_muffins', which is enough to return yes. If not, it
iterates over each judge's preferences and looks if the recipe is not in the 
'shared_muffins' set or if the current muffin appears twice in the 'repeats' 
set. If any one of these is true, the answer is no.
"""


def test(n, m, preferences):
    shared_muffins = set(preferences[0])
    for preference in preferences:
        shared_muffins = shared_muffins.intersection(set(preference))
    if shared_muffins:
        return "yes"
    else:
        repeats = set()
        for i in range(len(preferences[0]) - 1):
            for preference in preferences:
                if -preference[i] in repeats:
                    return "no"
                repeats.add(preference[i])
        return "yes"


def main():
    m, n = input().split()
    m = int(m)
    n = int(n)
    preferences = []

    for _ in range(n):
        preference = [int(x) for x in input().split()]
        if preference[-1] == 0:
            preference.pop()
        preferences.append(preference)
    print(test(n, m, preferences))


main()
