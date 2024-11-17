// 4-payment.test.js
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', () => {
    let calculateStub;
    let consoleSpy;

    beforeEach(() => {
        // Stub Utils.calculateNumber to always return 10
        calculateStub = sinon.stub(Utils, 'calculateNumber').returns(10);

        // Spy on console.log to verify the log output
        consoleSpy = sinon.spy(console, 'log');
    });

    afterEach(() => {
        // Restore the stub and spy to their original behavior
        calculateStub.restore();
        consoleSpy.restore();
    });

    it('should stub Utils.calculateNumber and verify console.log output', () => {
        sendPaymentRequestToApi(100, 20);

        // Verify the stub behavior
        sinon.assert.calledOnce(calculateStub);
        sinon.assert.calledWithExactly(calculateStub, 'SUM', 100, 20);

        // Verify the console.log output
        sinon.assert.calledOnce(consoleSpy);
        sinon.assert.calledWithExactly(consoleSpy, 'The total is: 10');
    });
});
