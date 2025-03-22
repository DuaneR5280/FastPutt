const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
    devServer: {
        port: 8080,
        allowedHosts: 'all',
        proxy: {
            '/api': {
                target: 'http://backend:8000',
                changeOrigin: true,
                pathRewrite: {
                    '^/api': ''
                }
            }
        }
    },
    // Optimize build output
    productionSourceMap: false,
    // Make HMR (Hot Module Replacement) work properly
    chainWebpack: config => {
        config.plugin('html').tap(args => {
            args[0].title = 'FastPutt'
            return args
        })
    },
    // Configure webpack for Vuetify 3
    configureWebpack: {
        resolve: {
            extensions: ['.js', '.vue', '.json']
        },
        module: {
            rules: [
                {
                    test: /\.s(c|a)ss$/,
                    use: [
                        'vue-style-loader',
                        'css-loader',
                        {
                            loader: 'sass-loader',
                            options: {
                                implementation: require('sass')
                            }
                        }
                    ]
                }
            ]
        }
    }
})
