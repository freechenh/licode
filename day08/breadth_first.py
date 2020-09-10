from collections import deque

graph = dict(you=['alice', "bob", "claire"], bob=["anuj", "peggy"], alice=["peggy"], claire=['thom', 'jonny'], anuj=[],
             peggy=[], thom=[], jonny=[])


def person_is_seller(person):
    return person[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


if __name__ == '__main__':
    demo = search("you")
    print(demo)
