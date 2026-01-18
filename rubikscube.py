import numpy as np

#all depends the relative front and back, can alsoapply when looking at different sides, since front n back also needto rotate
#need to be careful about the orientation, works for rotation but cube has to stay in the same orientation

"""
bottom could be wrong on the orientation,  bottom is opposit to top so when looking at it from the bottom would be different
could maybe do it as if looking from inside, but that might mess up the logic of actually solving 

need to think about back as well, if needed could do,2 - n giving either 0 or 2
either need to change the orientation of bottom and back, or change the logic used 


also need to think of the orientation of each vector, will be upside down relative to the front once it reaches the back,
cause thats how a cube works so willneed to fip collum from up to back and maybe just keep it from back to bottom. 


"""

def collsup(front, up, down, back, n):


    front[:, [n]], up[:, [n]], back[:,[n]], down[:,[n]] = down[:,[n]], front[:, [n]], up[:, [n]], back[:,[n]]

    return(front, up, down, back)

def collsdown(front, up, down, back, n):

    front[:, [n]], up[:, [n]], back[:,[n]], down[:,[n]] = up[:, [n]], back[:,[n]], down[:,[n]], front[:, [n]],

    return(front, up, down, back)


def rowsACW(front, left, back, right, n):

    front[[n], :], left[[n], :], back[[n], :], right[[n], :] = left[[n], :], back[[n], :], right[[n], :], front[[n], :]

def rowsCW(front, left, back, right, n):

    front[[n], :], left[[n], :], back[[n], :], right[[n], :] = right[[n], :], front[[n], :], left[[n], :], back[[n], :]



def rotateanti(z):

    for i in range(3):
        for j in range(i + 1, 3):
            z[[i],[j]], z[[j],[i]] = z[[j],[i]], z[[i],[j]]

    z = z[::-1]

    print(z)

def rotatewise(z):

    z = z[::-1]


    for i in range(3):
        for j in range(i + 1, 3):
            z[[j],[i]], z[[i],[j]] = z[[i],[j]], z[[j],[i]]

   

    print(z)


front = np.array([[1,2,3],
              [2,2,2],
              [8,8,1]])


up = np.array([[5,6,7],
              [7,8,9],
              [1,3,4]])

back = np.array([[5,4,1],
                 [1,1,6],
                 [4,2,3]])

down = np.array([[1,3,3],
                 [4,1,6],
                 [2,5,5]])

left = np.array([[1,2,5],
                 [4,5,6],
                 [7,8,9]])

right = np.array([[9,2,3],
                  [4,5,6],
                  [9,8,1]])

n = 2
rowsCW(front, left, back, right, n)
print(front)
print(left)
print(back)
print(right)

"""
Possible moves:

leftcol up ->  n = 0, left rotate anticlockwise
left col down -> n = 0, left rotate clockwise

right col up -> n = 2, right rotate clockwise
right col down -> n = 2, right rotate anticlockise

top row clockwise -> n = 0, top rotate clockwise
top row anti clockwise -> n = 0, top rotate anti-clockwise

bottom row clockwise -> n = 2, bottom rotate anti-clockwise
bottom row anti clockwise -> n = 2, bottom rotate clockwise


--need to figure these ones out, could mess up logic if not done carefully 
BE CAREFUL!!
need new logic
assuming we do with everything orintated up
front face clockwise ->  using left col right n =2 , up row 3 n = 2, left col 1, bottom row 
back face ahhhhhh
"""


