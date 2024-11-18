// api.test.js
const chai = require('chai');
const request = require('request');
const expect = chai.expect;

const BASE_URL = 'http://localhost:7865';

describe('Index page', () => {
    it('should return status 200', (done) => {
        request.get(`${BASE_URL}/`, (err, res, body) => {
            expect(res.statusCode).to.equal(200);
            done();
        });
    });

    it('should return correct message', (done) => {
        request.get(`${BASE_URL}/`, (err, res, body) => {
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });

    it('should handle unexpected routes with 404', (done) => {
        request.get(`${BASE_URL}/unknown`, (err, res, body) => {
            expect(res.statusCode).to.equal(404);
            done();
        });
    });
});
