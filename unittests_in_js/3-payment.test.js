// 3-payment.test.js
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
    let spy;

    beforeEach(() => {
        // Set up the spy before each test
        spy = sinon.spy(Utils, 'calculateNumber');
    });

    afterEach(() => {
        // Restore the original function after each test
        spy.restore();
    });

    it('should call Utils.calculateNumber with SUM and the provided arguments', () => {
        sendPaymentRequestToApi(100, 20);

        // Validate the spy's behavior
        sinon.assert.calledOnce(spy);
        sinon.assert.calledWithExactly(spy, 'SUM', 100, 20);
    });
});
