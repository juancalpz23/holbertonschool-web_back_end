// 6-payment_token.test.js
const getPaymentTokenFromAPI = require('./6-payment_token');
const { expect } = require('chai');

describe('getPaymentTokenFromAPI', () => {
    it('should resolve with correct data when success is true', (done) => {
        getPaymentTokenFromAPI(true)
            .then((response) => {
                expect(response).to.be.an('object');
                expect(response).to.have.property('data', 'Successful response from the API');
                done(); // Call done to indicate the test is complete
            })
            .catch((err) => done(err)); // Ensure any errors fail the test
    });
});
