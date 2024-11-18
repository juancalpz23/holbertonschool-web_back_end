// api.js
const express = require('express');
const app = express();
const PORT = 7865;

// Middleware for JSON body parsing
app.use(express.json());

// Welcome message
app.get('/', (req, res) => {
    res.send('Welcome to the payment system');
});

// Get payment methods
app.get('/available_payments', (req, res) => {
    const paymentMethods = {
        payment_methods: {
            credit_cards: true,
            paypal: false,
        },
    };
    res.json(paymentMethods);
});

// Login with username
app.post('/login', (req, res) => {
    const { userName } = req.body;
    if (!userName) {
        return res.status(400).send('Missing userName');
    }
    res.send(`Welcome ${userName}`);
});

// Cart route
app.get('/cart/:id(\\d+)', (req, res) => {
    const cartId = req.params.id;
    res.send(`Payment methods for cart ${cartId}`);
});

// Start server
app.listen(PORT, () => {
    console.log(`API available on localhost port ${PORT}`);
});

module.exports = app;
