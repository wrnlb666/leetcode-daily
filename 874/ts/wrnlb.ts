function tupleNize(x: number, y: number): number {
    return (x * 60001) + y
}


function robotSim(commands: number[], obstacles: number[][]): number {
    // convert obstacles to set
    let obsSet: Set<number> = new Set();
    obstacles.forEach(o => obsSet.add(tupleNize(o[0], o[1])))
    
    // simulate behavior
    const dirs: Map<string, [number, number]> = new Map([
        ['north', [0, 1]],
        ['south', [0, -1]],
        ['west', [-1, 0]],
        ['east', [1, 0]]
    ])
    let currDir: string = 'north'
    let pos: [number, number] = [0, 0]
    let furthrest: number = 0
    commands.forEach(c => {
        switch (c) {
            case -1: {
                switch (currDir) {
                    case 'north':
                        currDir = 'east'
                        break
                    case 'east':
                        currDir = 'south'
                        break
                    case 'south':
                        currDir = 'west'
                        break
                    case 'west':
                        currDir = 'north'
                        break
                }
            } break
            case -2: {
                switch (currDir) {
                    case 'north':
                        currDir = 'west'
                        break
                    case 'west':
                        currDir = 'south'
                        break
                    case 'south':
                        currDir = 'east'
                        break
                    case 'east':
                        currDir  = 'north'
                        break
                }
            } break
            default: {
                let [x, y] = dirs.get(currDir)!
                for (let i = 0; i < c; i++) {
                    let newPos: [number, number] = [pos[0] + x, pos[1] + y]
                    if (!obsSet.has(tupleNize(newPos[0], newPos[1]))) {
                        pos = newPos
                    } else {
                        break
                    }
                }
            }
        }
        let dist: number = pos[0] * pos[0] + pos[1] * pos[1]
        if (dist > furthrest) {
            furthrest = dist
        }
    })

    return furthrest
}


(() => {
    const commands: number[] = [4,-1,4,-2,4]
    const obstacles: number[][] = [[2,4]]
    const res: number = robotSim(commands, obstacles)
    console.log(res)
})()
