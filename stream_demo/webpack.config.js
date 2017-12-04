var path = require('path');
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var AssetsPlugin = require('assets-webpack-plugin');

module.exports = {
    entry: {
        "main": "./assets/js/main.js"
    },
    output: {
        path: path.resolve(__dirname, 'static/dist'),
        publicPath: "/static/dist/",
        filename: '[name].js'
    },
    module: {
        loaders: [
            { test: /\.scss$/, loader: ExtractTextPlugin.extract('style-loader', 'css-loader?sourceMap!sass-loader?sourceMap')},
        ]
    },
    plugins: [
        new ExtractTextPlugin('styles/main-bundle.css'),
        new AssetsPlugin()
    ]
};