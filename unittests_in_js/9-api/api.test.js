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
});

describe('Cart page', () => {
    it('should return status 200 when :id is a number', (done) => {
        request.get(`${BASE_URL}/cart/12`, (err, res, body) => {
            expect(res.statusCode).to.equal(200);
            expect(body).to.equal('Payment methods for cart 12');
            done();
        });
    });

    it('should return 404 when :id is NOT a number', (done) => {
        request.get(`${BASE_URL}/cart/hello`, (err, res, body) => {
            expect(res.statusCode).to.equal(404);
            done();
        });
    });

    it('should return 404 for missing :id', (done) => {
        request.get(`${BASE_URL}/cart/`, (err, res, body) => {
            expect(res.statusCode).to.equal(404);
            done();
        });
    });
});
