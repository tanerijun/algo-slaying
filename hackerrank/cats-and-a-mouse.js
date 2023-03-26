function catAndMouse(x, y, z) {
    const AToC = Math.abs(x - z)
    const BToC = Math.abs(y - z)
    
    if (AToC === BToC) {
        return "Mouse C"
    } else if (AToC < BToC) {
        return "Cat A"
    } else {
        return "Cat B"
    }
}
