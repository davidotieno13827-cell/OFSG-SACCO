module.exports = {
    content: [
        './ofsg_platform/templates/**/*.html',
        './ofsg_platform/**/templates/**/*.html',
        './index.html'
    ],
    theme: {
        extend: {
            colors: {
                ofsg: {
                    maroon: 'var(--ofsg-maroon)',
                    green: 'var(--ofsg-green)',
                    dark: 'var(--ofsg-dark)'
                }
            }
        }
    },
    plugins: []
}
