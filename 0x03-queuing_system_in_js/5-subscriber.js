import redis from 'redis';

const subscriber = redis.createClient();

subscriber.on('error', (error) => console.error(`Redis subscriber not connected to the server: ${error.message}`));
subscriber.on('connect', () => console.log('Redis subscriber connected to the server'));

subscriber.subscribe('holberton school channel');

subscriber.on('message', (channel, message) => {
    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe('holberton school channel', () => {
            subscriber.quit();
        });
    }
    console.log(message);
});
