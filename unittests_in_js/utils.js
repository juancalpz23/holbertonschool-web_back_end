// utils.js
const Utils = {
    calculateNumber: (type, a, b) => {
        if (type === 'SUM') return Math.round(a) + Math.round(b);
        if (type === 'SUBTRACT') return Math.round(a) - Math.round(b);
        if (type === 'DIVIDE') {
            const roundedB = Math.round(b);
            if (roundedB === 0) return 'Error';
            return Math.round(a) / roundedB;
        }
        throw new Error('Invalid operation type');
    },
};

module.exports = Utils;
