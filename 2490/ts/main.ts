

function isCircularSentence(sentence: string): boolean {
    let last: string = sentence[sentence.length-1];
    let words: string[] = sentence.split(' ');
    for (const w of words) {
        if (w[0] !== last) {
            return false;
        }
        last = w[w.length-1];
    }
    return true;
};


(() => {
    let sentence: string = "leetcode exercises sound delightful";
    let res: boolean = isCircularSentence(sentence);
    console.log(res);
})();
