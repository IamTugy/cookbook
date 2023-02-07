const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  const urls = ['/api', '/docs', '/redoc', '/openapi.json']
    urls.forEach(url => {
        app.use(
            url,
            createProxyMiddleware({
                target: 'http://localhost:8443',
                changeOrigin: true,
            })
        );
    });
};
