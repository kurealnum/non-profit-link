const path = require('path');

module.exports = {
    entry:'./assets/pages/index.tsx',
    output: {
        filename: 'index-bundle.js',  // output bundle file name
        path: path.resolve(__dirname, './static'),  // path to our Django static directory
    },
    resolve: {
      extensions: ['.ts', '.tsx']
    },
    module: {
        rules: [
          {
            test: /\.(ts|tsx)$/,
            exclude: /node_modules/,
            loader: "babel-loader",
            options: { presets: ["@babel/preset-env", "@babel/preset-react", "@babel/preset-typescript"] }
          },
          {
            test: /\.(png|jpe?g|gif|svg)$/i,
       
            use: "file-loader",
          }
        ]
      }
};