# rubiks-cube-python
Simple Rubiks Cube implementation in python/opengl

## Install
`pip install -r requirements.txt`

## Run
`python ./main_draw_cube.py`

### Key bindings
#### Piece rotation
R: Right rotation

Ri: Right inverted rotation

L: Left rotation

Li: Left inverted rotation

More keys: B,Bi,D,Di,F,Fi

#### Cube rotation/translation
Use the arrows to rotate the cube

Use shift + arrows for translations



## Code hints
### `cube.py`
Class which keeps a 3x3x3 numpy array of pieces as a data structure

### `pieces.py`
There are Middle Pieces, Edge Pieces and Corner Pieces. 
Each piece keeps 6 squares represented as a VBO (Vertex Buffer Object). 
