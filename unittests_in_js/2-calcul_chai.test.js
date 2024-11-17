let chai;
let expect;

before(async () => {
    // Dynamically import chai
    chai = await import('chai');
    expect = chai.expect;
});

const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
    describe('SUM', () => {
        it('should return the sum of two rounded numbers', () => {
            expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
            expect(calculateNumber('SUM', -1.4, -4.5)).to.equal(-5);
            expect(calculateNumber('SUM', 0, 0)).to.equal(0);
        });
    });

    describe('SUBTRACT', () => {
        it('should return the difference of two rounded numbers', () => {
            expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
            expect(calculateNumber('SUBTRACT', -1.4, -4.5)).to.equal(3);
            expect(calculateNumber('SUBTRACT', 0, 0)).to.equal(0);
        });
    });

    describe('DIVIDE', () => {
        it('should return the division of two rounded numbers', () => {
            expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
            expect(calculateNumber('DIVIDE', -1.4, 0.5)).to.equal(-1);
        });

        it('should return "Error" when dividing by 0', () => {
            expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
            expect(calculateNumber('DIVIDE', -1.4, 0)).to.equal('Error');
        });
    });

    describe('Invalid type', () => {
        it('should throw an error for invalid operation type', () => {
            expect(() => calculateNumber('MULTIPLY', 1.4, 4.5)).to.throw('Invalid operation type');
        });
    });
});
