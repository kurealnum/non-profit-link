const path = require('path');

module.exports = {
    entry:'./assets/ts/index.tsx',
    output: {
        filename: 'index-bundle.js',  // output bundle file name
        path: path.resolve(__dirname, './static'),  // path to our Django static directory
    },
};