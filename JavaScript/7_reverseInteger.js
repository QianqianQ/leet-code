/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    const INT_MAX = 2**31 - 1;
    const INT_MIN = -(2**31);
    let y = Math.abs(x).toString().split("").reverse().join('');
    const k = x<0 ? -1:1;
    y = y*k;
    if (y >= INT_MAX || y<= INT_MIN){
        return 0;
    }
    return y;
};

const x =-123
const y = reverse(x);
console.log(y);