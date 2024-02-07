import redis from 'redis';

// create redis client
const client = redis.createClient();

// connect to redis server
client.on('connect', () => console.log('Redis client connected to the server'));

// handle connection errors
client.on('error', (err) => console.error(`Redis client not connected to the server: Error: ${err.message}`));
