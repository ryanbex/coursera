function getMinimumDifference(a, b) {
    console.log(a, b)
    if (!(Array.isArray(a) || alength > 0)) return [];
    
    let len = Math.min(a.length, b.length); 
    let differences = []; 

    for (let i=0; i < len; i++) {
        differences.push(getDifference(a[i], b[i]));
    }
    
    return differences;

}

function getDifference(word0, word1) {
    console.log(word0, word1)
    // check if word0 and word1 are same length
    // get difference between teh two words
    if (word0.length != word1.length || word0.length <= 0) return -1;

    let word0Dict = makeWordDict(word0);
    let word1Dict = makeWordDict(word1);
    
    let diffDict = makeDiffDict(word0Dict, word1Dict);    

    let difference = calcDifference(diffDict);
    
    return difference;
}

function makeDiffDict(dict0, dict1) {
    let diffDict = {};
    Object.keys(dict1).forEach((key) => {
        /**
            if abcdeee and abbbfff, then the difference is 5
            {a: 0, b: -2, c: 1, d: 1, e:3, f:-3}
        */
        
        if (key in dict0) {
            let diff = (dict0[key] - dict1[key]);
            dict0[key] =  diff>0? diff:0;    
        }
    })
    Object.keys(dict0).forEach((key) => {
        diffDict[key] = dict0[key];
    })
    return diffDict;
}

function calcDifference(diffDict) {
    let difference = 0;
    Object.keys(diffDict).forEach((key) => {
        difference += diffDict[key];
    })
    return difference;
}

function makeWordDict(word) {
    let wordDict = {}
    for (let i = 0; i < word.length; i++) {
        if (word[i] in wordDict) {
            wordDict[word[i]] += 1;   
        } else {
            wordDict[word[i]] = 1;
        }
    }
    return wordDict;
}
