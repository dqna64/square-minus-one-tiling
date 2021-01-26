class Square {
    constructor(hole, square_size) {
        this.hole = hole
        this.SQUARE_SIZE = square_size
        this.ori = this.generateOri(this.hole, this.SQUARE_SIZE)
    }

    generateOri(hole, square_size) {
        // Exit recursion
        if (square_size == 2) {
            if (arrayEquals(hole, [0, 1])) {  // 1st quad
                return [0, []]
            } else if (arrayEquals(hole, [0, 0])) {  // 2nd quad
                return [1, []]
            } else if (arrayEquals(hole, [1, 0])) {  // 3rd quad
                return [2, []]
            } else if (arrayEquals(hole, [1, 1])) {  // 4th quad
                return [3, []]
            } else {
                console.log(hole)
                return 'No matching holes'
            }
        } else {
            let holeQuad = null
            if (hole[0] < square_size/2 && hole[1] >= square_size/2) { //1st quad
                holeQuad = 0
            } else if (hole[0] < square_size/2 && hole[1] < square_size/2) {  // 2nd quad
                holeQuad = 1
            } else if (hole[0] >= square_size/2 && hole[1] < square_size/2) {  // 3rd quad
                holeQuad = 2
            } else if (hole[0] >= square_size/2 && hole[1] >= square_size/2) {  // 4th quad
                holeQuad = 3
            }

            let subHoleQuads = []
        
            // Continue recursion
            for (let i = 0; i < 4; i++) {  // For each quadrant, in order 0, 1, 2, 3
                let subHole = null
                if (i == holeQuad) {  // If we are in the quad with the hole
                    if (i == 0) {  // 1st quad
                        subHole = [hole[0], hole[1]-int(square_size/2)]
                    } else if (i == 1) {  // 2nd quad
                        subHole = [hole[0], hole[1]]
                    } else if (i == 2) {  // 3rd quad
                        subHole = [hole[0]-int(square_size/2), hole[1]]
                    } else if (i == 3) {  // 4th quad
                        subHole = [hole[0]-int(square_size/2), hole[1]-int(square_size/2)]
                    }
                }
                else {  // Otherwise
                    // The subHole is just a pretend hole in opposite direction
                    if (i == 0) {  // 1st quad
                        subHole = [int(square_size/2)-1, 0]
                    } else if (i == 1) {  // 2nd quad
                        subHole = [int(square_size/2)-1, int(square_size/2)-1]
                    } else if (i == 2) {  // 3rd quad
                        subHole = [0, int(square_size/2)-1]
                    } else if (i == 3) {  // 4th quad
                        subHole = [0, 0]
                    }
                }
                subHoleQuads.push(this.generateOri(subHole, int(square_size/2)))
            }
            return [holeQuad, subHoleQuads]
        }
    }

    updateHole(hole) {
        // Only allow update if hole values are valid indices of the square
        for (let i of hole) {
            if (i < 0 || i >= this.SQUARE_SIZE) {
                return
            }
        }
        this.ori = this.generateOri(hole, this.SQUARE_SIZE);
    }
        
    display() {
        push();
        translate(DIS_WIDTH/2, DIS_HEIGHT/2);
        recursiveDisplay(this.ori, 512);
        pop();
    }
    
    
}

function recursiveDisplay(ori, square_size) {
    let arrow = ori[0];
    let subArrows = ori[1];
    let sub_square_size = square_size / 2;

    // At each recursion step, we always want to draw the tile in the middle
    push()
    if (arrow == 0) {
        console.log('exit: no rotate');
    } else if (arrow == 1) {
        console.log('exit: rotate 90 anti');
        rotate(-PI/2);
    } else if (arrow == 2) {
        console.log('exit: rotate 180');
        rotate(PI);
    } else if (arrow == 3) {
        console.log('exit: rotate 90');
        rotate(PI/2);
    }
    drawTile(TILE_SIZE);
    pop()

    if (subArrows.length != 0) { // Continue recursion
        for (let i = 0; i < subArrows.length; i++) {
            push()
            if (i == 0) { // Translate to centre of each subquadrant
                translate(sub_square_size/2, -sub_square_size/2)
            } else if (i == 1) {
                translate(-sub_square_size/2, -sub_square_size/2)
            } else if (i == 2) {
                translate(-sub_square_size/2, sub_square_size/2)
            } else if (i == 3) {
                translate(sub_square_size/2, sub_square_size/2)
            }
            recursiveDisplay(subArrows[i], sub_square_size);
            pop()
        }
    }
}


function drawTile(tile_size) {
    noStroke();
    fill(29, 166, 245);
    let body_width = tile_size * 7 / 8;
    let gap_width = (tile_size - body_width) / 2;
    beginShape();
    vertex(-gap_width, gap_width);
    vertex(-gap_width, -(body_width+gap_width));
    vertex(-(body_width+gap_width), -(body_width+gap_width));
    vertex(-(body_width+gap_width), (body_width+gap_width));
    vertex((body_width+gap_width), (body_width+gap_width));
    vertex((body_width+gap_width), gap_width);
    endShape(CLOSE);
}

function arrayEquals(a, b) {
    return Array.isArray(a) &&
      Array.isArray(b) &&
      a.length === b.length &&
      a.every((val, index) => val === b[index]);
  }