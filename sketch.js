let DIS_WIDTH = 1280;
let DIS_HEIGHT = 720;
let FPS = 24;
let debug = true;
let aesthetics = true;

let SQUARE_SIZE = 16;
let TILE_SIZE = 512 / SQUARE_SIZE;
let hole = [6,6];
let square;


function setup() {
  createCanvas(DIS_WIDTH, DIS_HEIGHT);
  frameRate(FPS);
  square = new Square(hole, SQUARE_SIZE)
  console.log(square.ori)

}

function draw() {
  background(20);
  hole = getHoleLoc(mouseX, mouseY);
  square.updateHole(hole);
  square.display();

}

function getHoleLoc(x, y) {
  // Dist from screen centre
  x -= DIS_WIDTH/2;
  y -= DIS_HEIGHT/2;
  // Tile from square centre
  tileY = Math.floor(x / TILE_SIZE);
  tileX = Math.floor(y / TILE_SIZE);
  // Tile indices, may be out of range of the square
  return [int(tileX + SQUARE_SIZE/2), int(tileY + SQUARE_SIZE/2)]

}

loopBool = true;
function keyPressed() {
  if (key == " ") {
    if (loopBool) {
      noLoop();
      loopBool = !loopBool;
    } else {
      loop();
      loopBool = !loopBool;
    }
  } else if (key == 'd') {
    debug = !debug;
  } else if (key == 'a') {
    aesthetics = !aesthetics;
  }
}
