function rotateString(s: string, goal: string): boolean {
    if (s.length !== goal.length) {
        return false;
    }
    s += s;
    if (s.includes(goal)) {
        return true;
    }
    return false;
};


(() => {
    let s = "abcde";
    let goal = "abced";
    let res = rotateString(s, goal)
    console.log(res)
})();
