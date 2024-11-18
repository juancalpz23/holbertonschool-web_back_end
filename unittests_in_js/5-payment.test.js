// 5-payment.test.js
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', () => {
    let consoleSpy;

    beforeEach(() => {
        // Spy on console.log before each test
        consoleSpy = sinon.spy(console, 'log');
    });

    afterEach(() => {
        // Restore the spy after each test
        consoleSpy.restore();
    });

    it('should log "The total is: 120" for inputs 100 and 20', () => {
        sendPaymentRequestToApi(100, 20);

        // Verify console.log behavior
        sinon.assert.calledOnce(consoleSpy);
        sinon.assert.calledWithExactly(consoleSpy, 'The total is: 120');
    });

    it('should log "The total is: 20" for inputs 10 and 10', () => {
        sendPaymentRequestToApi(10, 10);

        // Verify console.log behavior
        sinon.assert.calledOnce(consoleSpy);
        sinon.assert.calledWithExactly(consoleSpy, 'The total is: 20');
    });
});
