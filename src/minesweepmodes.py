import pickle 
emojiList = ["0️⃣","1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟","❗","‼"]
thisdict = {
    "standard": {
        "name": "Vanilla",
        "description": "Standard Minesweeper.",
        "data": [(-1,-1),(0,-1),(1,-1), (-1,0),(1,0), (-1,1),(0,1),(1,1)]},
    "knight": {
        "name": "Knightsweeper",
        "description": "Mines are a knight's move away.",
        "data": [(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-2,1),(-2,-1),(-1,2)]},
    "cross" : {
        "name": "Crossweeper",
        "description": "Mines are in the orthagonally adjacent tiles.",
        "data": [(0,-1),(-1,0),(1,0),(0,1)]},
    "x" : {
        "name": "Xsweeper",
        "description": "Mines are in the diagonally adjacent tiles.",
        "data": [(-1,-1),(1,1),(1,-1),(-1,1)]},
    "carpenter" : {
        "name": "Carpentersweeper",
        "description": "Mines are a knight's move away OR 2 spaces away orthagonally.",
        "data": [(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-2,1),(-2,-1),(-1,2),(0,-2),(-2,0),(2,0),(0,2)]},
    "crossknight" : {
        "name": "CrossKnightsweeper",
        "description": "Mines are a knight's move away OR are in the orthagonally adjacent tiles.",
        "data": [(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-2,1),(-2,-1),(-1,2),(0,-1),(-1,0),(1,0),(0,1)]},
    "xknight" : {
        "name": "X-Knightsweeper",
        "description": "Mines are a knight's move away OR are in the diagonally adjacent tiles.",
        "data": [(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-2,1),(-2,-1),(-1,2),(-1,-1),(1,1),(1,-1),(-1,1)]},
}
minesweep = open(r'src\minesweeper.obj', 'wb') 
pickle.dump(emojiList, minesweep)
pickle.dump(thisdict, minesweep)