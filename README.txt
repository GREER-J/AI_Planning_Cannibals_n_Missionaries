CONTEXT:
 - NUM is looking at using AI Planning for mission Planning.
 - This toy example is to teach myself AI Planning

AIM:
 - Implement AI Planning concepts
 - Code my own basic tools
 - Potentially Implement a factory

Cannibals and missionaries:
SETTING:
 - 2d world with a river going through it
 - On left side are 3 cannibals (c) and 3 missionaries (m)
 - There is a boat that can take 2 people at a time across the river

OBJ:
 - Get all persons to other side of river

CONSTRAINTS:
 - If c > m on any bank, c will eat m = FAIL
 - Boat can only take 2 people at a time

SIMPLIFICATION:
 - Boat must take 2 people at all times

STATES:
 - States will be expressed as the persons on the left and the persons on the right. EG L(#m#c), R(#m#c)

ACTIONS:
 - 1m1c: transport 1 c and 1 m across the river
 - 2c: transport 2 c and 0 m across the river
 - 2m: transport 0 c and 2 m across the river

MVC:
 - Model
    - Representation of the world
       - World States
       - Objects (boat, people ect)
 - View
    - View to user
 - Controller
    - Ties the two together