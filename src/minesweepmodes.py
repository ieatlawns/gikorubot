import pickle 
emojiList = ["0️⃣","1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟","❗","‼"]
thisdict = {
    "standard": {
        "name": "Minesweeper",
        "description": "Standard Minesweeper.",
        "data": [(-1,-1),(0,-1),(1,-1), (-1,0),(1,0), (-1,1),(0,1),(1,1)]},
    "knight": {
        "name": "Knightsweeper",
        "description": "Uses the knight's movement.",
        "data": [(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-2,1),(-2,-1),(1,1)]},
    "cross" : {
        "name": "Crossweeper",
        "description": "Only Orthagonal.",
        "data": [(0,-1),(-1,0),(1,0),(0,1),]},
    "x" : {
        "name": "Xsweeper",
        "description": "Only Diagonal.",
        "data": [(-1,-1),(1,1),(1,-1),(-1,1),]},
    "carpenter" : {
        "name": "Carpentersweeper",
        "description": "Uses both the Knight and Dabbaba's movement.",
        "data": [(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-2,1),(-2,-1),(1,1)]}
}
minesweep = open(r'src\minesweeper.obj', 'wb') 
pickle.dump(emojiList, minesweep)
pickle.dump(thisdict, minesweep)