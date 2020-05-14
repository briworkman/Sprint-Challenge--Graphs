from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Add opposite directions of each direction so we can move backwarads if we need to.
#   Allows for quickly undoing/reversing moves
# Traverse a map and return the path to traverse the entire map
#   Take in the starting room and a `visited` array to keep track of what rooms we have already visited
#   Define a base pathway with what you start with aka no rooms or possible directions
#   Loop through the exits for the current room
#       Have the player travel in the given directions
#       Check to see if the current room is already in the `visited` array
#           If it is, move the player in the opposite direction, that room has already been visited so we've already checked all possible directions
#              If it is not
#                   Add the current room to the `visited` array
#                   Add that direction to the path array
#                   Let the path equal the current path plus the path we just created
#                   Have the player travel in the opposite direction of the path
#                   Add the opposite directions to the path array


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
