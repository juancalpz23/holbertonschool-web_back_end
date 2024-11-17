const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
    describe('SUM', () => {
        it('should return the sum of two rounded numbers', () => {
            assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
            assert.strictEqual(calculateNumber('SUM', -1.4, -4.5), -5); // Expected is -5, not -6
            assert.strictEqual(calculateNumber('SUM', 0, 0), 0);
        });
    });

    describe('SUBTRACT', () => {
        it('should return the difference of two rounded numbers', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
            assert.strictEqual(calculateNumber('SUBTRACT', -1.4, -4.5), 3); // Expected is 3, not 4
            assert.strictEqual(calculateNumber('SUBTRACT', 0, 0), 0);
        });
    });

    describe('DIVIDE', () => {
        it('should return the division of two rounded numbers', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
            assert.strictEqual(calculateNumber('DIVIDE', -1.4, 0.5), -1); // Expected is -1, not -2
        });

        it('should return "Error" when dividing by 0', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
            assert.strictEqual(calculateNumber('DIVIDE', -1.4, 0), 'Error');
        });
    });

    describe('Invalid type', () => {
        it('should throw an error for invalid operation type', () => {
            assert.throws(() => calculateNumber('MULTIPLY', 1.4, 4.5), {
                name: 'Error',
                message: 'Invalid operation type',
            });
        });
    });
});
