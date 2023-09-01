const path = require('path');
const glob = require('glob');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    entry: {"index": './assets/pages/index.tsx',
            "login": './assets/pages/login.tsx'},
    plugins: [
      new HtmlWebpackPlugin({
        title: 'Output Management',
      }),
    ],
    output: {
        filename: '[name].js',  // output bundle file name
        path: path.resolve(__dirname, './react_static'),  // path to our Django static directory
        clean: true,
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