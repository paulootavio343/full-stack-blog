const cacheName = 'blog-cache-v2';
const urlsToCache = [
    '/',
    '/static/about.txt',
    '/static/android-chrome-192x192.png',
    '/static/android-chrome-512x512.png',
    '/static/apple-touch-icon.png',
    '/static/favicon-16x16.png',
    '/static/favicon-32x32.png',
    '/static/favicon.ico',
    '/static/site.webmanifest',
    '/static/assets/css/base.css',
    '/static/assets/css/cookie-consent.css',
    '/static/assets/css/footer.css',
    '/static/assets/css/home-content.css',
    '/static/assets/css/home-trending.css',
    '/static/assets/css/navbar.css',
    '/static/assets/css/post-content.css',
    '/static/assets/fonts/Montserrat/Montserrat-SemiBold.ttf',
    '/static/assets/fonts/Montserrat/OFL.txt',
    '/static/assets/fonts/Open_Sans/LICENSE.txt',
    '/static/assets/fonts/Open_Sans/OpenSans-Regular.ttf',
    '/static/assets/icons/about.txt',
    '/static/assets/icons/calendar_month_dark.svg',
    '/static/assets/icons/calendar_month.svg',
    '/static/assets/icons/call.svg',
    '/static/assets/icons/category.svg',
    '/static/assets/icons/chevron_left_white.svg',
    '/static/assets/icons/chevron_left.svg',
    '/static/assets/icons/chevron_right_white.svg',
    '/static/assets/icons/chevron_right.svg',
    '/static/assets/icons/mail.svg',
    '/static/assets/icons/pin_drop.svg',
    '/static/assets/icons/profile_icon_dark.svg',
    '/static/assets/icons/profile_icon.svg',
    '/static/assets/js/cookie-consent.js',
    '/static/assets/js/home-slide.js',
    '/static/assets/js/infinite.min.js',
    '/static/assets/js/jquery.waypoints.min.js',
    '/static/assets/js/menu.js',
    '/static/assets/js/service-worker-registration.js',
];

self.addEventListener('install', event => {
    // Perform install steps
    event.waitUntil(
        caches
            .open(cacheName)
            .then(cache => {
                cache.addAll(urlsToCache);
            })
            .then(() => self.skipWaiting())
    );
});

self.addEventListener('activate', event => {
    // Remove old caches
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cache => {
                    if (cache !== cacheName) {
                        return caches.delete(cache);
                    }
                })
            );
        })
    );
});

self.addEventListener('fetch', event => {
    // Cache and network fallback
    event.respondWith(
        fetch(event.request).catch(() => caches.match(event.request))
    )
});
